##############################
#  Markov Chain Discord Bot  #
#    Author Paul Gleason     #
##############################

# Imports
import discord
from discord import app_commands
from discord.ext import commands, tasks
from config import *
import os
import csv
import markov as marko
import markovify

bot = commands.Bot(command_prefix='$', intents = discord.Intents.all())

# try:
#     os.remove('parsed_data.txt')
#     print('Old training data deleted')
# except EnvironmentError as e:
#     print(e.strerror)

# Call markov code
markov = marko

# Class to store 'global' variables
class variables():
    def __init__(self):
        self.config_save = 0
        self.channels_total = {}
        self.working_channel = 0
        self.listening_channels = 'SET CHANNEL!'
        self.method = True
        self.model_json = ''
        self.talk = False

variabl = variables()

@bot.event
async def on_ready():
    print(f'I am ready {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# make the slash command
# @bot.tree.command(name="hello", description='Will say hello to you')
# async def hello(interaction: discord.Interaction):
#     if interaction.channel_id == variabl.working_channel:
#         # ephemeral = True
#         # This makes it so just the user show sends the command can see the message    
#         # await interaction.response.send_message(f"testing: {name}", ephemeral=True)
#         await interaction.response.send_message(f"Hey {interaction.user.mention}", ephemeral=True)
#     else:
#         await interaction.response.send_message(f'Please use: <#{str(variabl.working_channel)}>', ephemeral=True)

# Set channel the bot will responsed to
@bot.tree.command(name="set-channel", description='set channel so bot to respond to commands')
async def setchannel(interaction: discord.Interaction):
    # Check if user is the owner
    if str(interaction.user.id) == OWNER_ID:
        variabl.working_channel = interaction.channel_id
        print(f"channel is set to channel: {interaction.channel} ID: {variabl.working_channel}")
        await interaction.response.send_message(f"channel is set to channel: `{interaction.channel}`")
    else:
        print(f"{interaction.user} tried to change the channel!")
        await interaction.response.send_message(f"You aren't the owner of this bot...", ephemeral= True)

# Add or Remove channels from the listening pool
@bot.tree.command(name="listen", description='Add or Remove channels from the listening pool')
@app_commands.describe(state = 'add or remove', channel1 = 'channel 1', channel2 = 'channel 2', channel3 = 'channel 3', channel4 = 'channel 4', channel5 = 'channel 5', channel6 = 'channel 7', channel8 = 'channel 8')
@app_commands.choices(state = [app_commands.Choice(name='add',value='add'), app_commands.Choice(name='remove',value='remove')])
async def listen(interaction: discord.Interaction, state: str, channel1: discord.TextChannel, channel2: discord.TextChannel = None, channel3: discord.TextChannel = None, channel4: discord.TextChannel = None, channel5: discord.TextChannel = None, channel6: discord.TextChannel = None, channel7: discord.TextChannel = None, channel8: discord.TextChannel = None):
    if str(interaction.user.id) == OWNER_ID:
        if state == 'add':
            channels = [channel1, channel2, channel3, channel4, channel5, channel6, channel7, channel8]
            # loop through channels
            for channel in channels:
                # if channel has a channel continue
                if channel != None:
                    # add the to the channels_total dict with the key being channel name and the value being channel id
                    variabl.channels_total[channel.name] = channel.id

            print(variabl.channels_total)

            # clear listening_channels
            variabl.listening_channels = ''
            # Loop throught the channels_total values and add to the listening_channels
            for id in variabl.channels_total.values():
                variabl.listening_channels += f'• <#{str(id)}> \n'

            print(f"{bot.user} is now listening to \n{variabl.listening_channels}")
            await interaction.response.send_message(f"{bot.user} is now listening to \n{variabl.listening_channels}")
        elif state == 'remove':
            removed_channels = ''
            remove_channels = []
            channels = [channel1, channel2, channel3, channel4, channel5, channel6, channel7, channel8]

            for channel in channels:
                if channel != None:
                    for current_channel in variabl.channels_total.values():
                        if channel.id is current_channel:
                            removed_channels += f'• <#{str(channel.id)}> \n'
                            remove_channels.append(channel.name)

            # Deleting channels
            for channel in remove_channels:
                del variabl.channels_total[channel]

            # Clean the listening_channels var
            variabl.listening_channels = ''
            # Remaking listening_channels based off of the removed channels
            for id in variabl.channels_total.values():
                variabl.listening_channels += f'• <#{str(id)}> \n'

            await interaction.response.send_message(f'Channels that were removed: \n{removed_channels}\nChannels that are being listened to: \n{variabl.listening_channels}')
        else:
            await interaction.response.send_message('Please use `add` or `remove`.')
    else:
        print(f"{interaction.user} is trying to use me in {interaction.channel} and they aren't the owner.")
        await interaction.response.send_message(f"You're not the owner", ephemeral=True)

# Show channels that the bot is listening to
@bot.tree.command(name="listening", description="Add channels that training will listen to.")
async def listening(interaction: discord.Interaction):
    if variabl.working_channel == interaction.channel_id:
        print(f"{bot.user} is listening to \n{variabl.listening_channels}")
        await interaction.response.send_message(f"{bot.user} is listening to \n{variabl.listening_channels}")
    else:
        print(f"{interaction.user} is trying to use me in {interaction.channel}")
        await interaction.response.send_message(f'Please use: <#{str(variabl.working_channel)}>', ephemeral=True)

# Save/Import or Delete Variables
@bot.tree.command(name="change-vars", description="If input is `True` will save variables or import them. If `False` will delete the saves vars.")
@app_commands.describe(state = 'Save, Import, or Delete.')
@app_commands.choices(state = [app_commands.Choice(name='Save',value='save'), app_commands.Choice(name='Import',value='import'), app_commands.Choice(name='Delete',value='delete')])
async def varsconfig(interaction: discord.Interaction, state: str):
    vari_dict = {}
    if str(interaction.user.id) == OWNER_ID:
        # Import values
        if state == 'save':
            vari_dict = {'config_save': variabl.config_save, 'channels_total': variabl.channels_total, 'listening_channels': variabl.listening_channels}
            try:
                with open("config.csv", "w") as writer:
                    fieldnames = ['config_save', 'channels_total', 'listening_channels']        
                    dict_writer = csv.DictWriter(writer, fieldnames=fieldnames)
                    dict_writer.writeheader()
                    dict_writer.writerows(vari_dict)
            except EnvironmentError as e:
                print(e.strerror)
            print("Variables config was saved")
            await interaction.response.send_message(f"Variables config was saved")
        # Save values
        elif state == 'import':
            try:
                with open("config.csv", "r") as reader:
                    dict_reader = csv.DictReader(reader)
                    print(dict_reader)
            except EnvironmentError as e:
                print(e.strerror)
            print(vari_dict)
            print("Variables was imported")
            await interaction.response.send_message(f"Variables was imported")
        elif state == 'delete':
            os.remove("config.csv")
            print("Variables config was deleted")
            await interaction.response.send_message(f"Variables config was deleted")
    else:
        print(f"{interaction.user} tried to change vars!")
        await interaction.response.send_message(f"You aren't the owner of this bot...", ephemeral= True)

# Set markov algorithm to creators or markovify
@bot.tree.command(name="algorithm-selection", description="Will select my markov or markovify.")
@app_commands.describe(algorithm = "If creators will use my markov algorithm if markovify will use markovify.")
@app_commands.choices(algorithm = [app_commands.Choice(name='Creator',value='creator'), app_commands.Choice(name='Markovify',value='markovify')])
async def algorithm_function(interaction: discord.Interaction, algorithm: str):
    if variabl.working_channel == interaction.channel_id:
        variabl.method = algorithm

        if algorithm == 'creator':
            await interaction.response.send_message('Markov algorithm in use is the creators')
        if algorithm == 'markovify':
            await interaction.response.send_message('Markov algorithm in use is markovify')
    else:
        print(f"{interaction.user} is trying to use me in {interaction.channel}")
        await interaction.response.send_message(f'Please use: <#{str(variabl.working_channel)}>', ephemeral=True)

# Train bot using the selected listening channels
@bot.tree.command(name="train", description='train bot with history of listening channels')
@app_commands.describe(clean = "If True will delete previous training data.")
async def train(interaction: discord.Interaction, clean: bool):
    if variabl.working_channel == interaction.channel_id and len(variabl.channels_total) != 0 and  str(interaction.user.id) == OWNER_ID:
        try:
            if clean == True:
                os.remove('parsed_data.txt')
        except EnvironmentError as e:
                    print(e.strerror)
        
        await interaction.response.defer(thinking=True)

        message_contents = []
        # count = 1
        for id in variabl.channels_total.values():
            num = 0
            # async for _ in bot.get_channel(id).history(limit=None):
            #     count += 1
            async for message in bot.get_channel(id).history(limit=None):
                # print(message.content)
                # await interaction.response.send_message(f'Bot is on channel {bot.get_channel(id).name}: {num/count}%')
                num += 1
                print(f'{bot.get_channel(id).name} message: {num}')
                message_contents.append(message.content)

        if clean == False:
            with open('parsed_data.txt', 'a', encoding="utf-8") as all_messages:
                for line in message_contents:
                    if line != '' or line != '\n':
                        all_messages.write(line + '\n')
        else:
            with open('parsed_data.txt', 'w', encoding="utf-8") as all_messages:
                for line in message_contents:
                    if line != '' or line != '\n':
                        all_messages.write(line + '\n')
        
        # Creators Generation
        markov.generate('parsed_data.txt')

        # Markovify Generation
        corpus = open('parsed_data.txt', encoding='utf-8').read()
        # https://github.com/jsvine/markovify
        text_model = markovify.Text(corpus)
        variabl.model_json = text_model.to_json()
        print(variabl.model_json)
        
        print('Markov Chain has been generated')
        print(f"\nchannel history is in the terminal. The amount of messages used for training is: {len(message_contents)}\n")
        await interaction.followup.send(f"channel history is in the terminal nerd. The amount of messages used for training is: {len(message_contents)}")
    else:
        print(f"{interaction.user} is trying to use me in {interaction.channel} or they forgot /listen-add")
        interaction.response.send_message(f'Please use: <#{str(variabl.working_channel)}> or no channels are being listened to.', ephemeral=True)

# Build out training data from file without running train command
@bot.tree.command(name="generate", description='If you have your own training data file')
async def generate(interaction: discord.Interaction):
    if variabl.working_channel == interaction.channel_id and str(interaction.user.id) == OWNER_ID:
        # Creators Generation
        markov.generate('parsed_data.txt')

        # Markovify Generation
        corpus = open('parsed_data.txt', encoding='utf-8').read()
        # https://github.com/jsvine/markovify
        text_model = markovify.Text(corpus)
        variabl.model_json = text_model.to_json()
        print(variabl.model_json)
    else:
        print(f"{interaction.user} is trying to use me in {interaction.channel}")
        await interaction.response.send_message(f"You're not the owner of this bot", ephemeral=True)

# Output sentence based on training data
@bot.tree.command(name="mark", description='train bot with history of listening channels')
async def mark(interaction: discord.Interaction):
    #TODO add it so when the bot is talking you can't call mark
    if variabl.working_channel == interaction.channel_id:
        # DELETE LINE BELOW LATER
        # markov.generate('Masterhacker_bot\masterhacker_parsed_data.txt')
        
        if variabl.method == True:
            sentence = markov.markov_string()
        elif variabl.method == False:
            reconstituted_model = markovify.Text.from_json(variabl.model_json)
            sentence = reconstituted_model.make_short_sentence(300, 80)

        # print(f'Sentence is: {str(sentence)}')
        await interaction.response.send_message(f'{sentence}')
    else:
        print(f"{interaction.user} is trying to use me in {interaction.channel}")
        await interaction.response.send_message(f'Please use: <#{str(variabl.working_channel)}>', ephemeral=True)

# Loop for bot to talk every 15 seconds
@tasks.loop(seconds=15)
async def talking_func():
    print('talking')
    if variabl.method == True:
        sentence = markov.markov_string()
    elif variabl.method == False:
        reconstituted_model = markovify.Text.from_json(variabl.model_json)
        sentence = reconstituted_model.make_short_sentence(300, 100)

    await bot.get_channel(variabl.working_channel).send(sentence)

# Set bot to talk every 10 seconds
@bot.tree.command(name="talk", description="Will talk every 15 seconds")
@app_commands.describe(talking = "If True bot will talk every 15 seconds")
async def talk (interaction: discord.Interaction, talking: bool):
    if variabl.working_channel == interaction.channel_id:
        if talking == True:
            talking_func.start()
        elif talking == False:
            talking_func.stop()
        await interaction.response.send_message(F'Bot will now talk every 15 seconds: {talking}')
    else:
        print(f"{interaction.user} is trying to use me in {interaction.channel}")
        await interaction.response.send_message(f'Please use: <#{str(variabl.working_channel)}>', ephemeral=True)

# run the bot
bot.run(TOKEN)