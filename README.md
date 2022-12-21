# Work in Progress!

# Python Markov Bot
Made by: Paul Gleason

### Requirements
* discord.py
* markovify
* numpy

## Commands
* `/algorithm` - Switch between creators algorithm or markovify (If algorithm is change you must retrain the bot).
    * `True`: will use the creators algorithm.
    * `False`: will use the markovify algorithm.
* `/change-vars` - (Work in Progress)
* `/listen` - Add or Remove channels from listening.
    * `add`: will add the channels in channel1-10 to the listening list.
    * `remove`: will remove the channels in channel1-10 to the listening list.
* `/listening` - Will display what channels are being listened to.
* `/mark` - Output sentence from training data.
* `/set-channel` - Set channel so bot can only be used in that channel.
* `/talk` - Give the ability for the bot to talk freely.
    * `True`: bot will talk in the /set-channel every 10 secondes.
    * `False`: bot can be used as normal.
* `/train` - Bot will read messages from listening channels and turn it into a data set for markov.
    * `True`: will remove previous training data (training data is deleted once bot is turned off). 
    * `False`: will appened new data onto the old data file.  

## Usage
1. Create a [Discord bot application](https://discordapp.com/developers/applications/)
2. Under the "Bot" section, enable the "Message Content Intent", and copy the token for later.
3. Setup and configure the bot using one of the below methods:

# Discord Size
1. Setup config with correct data.
    * Make a file called `config.py` and add the following.
    * You may need to enable devoloper mode to see Guild ID and User ID
    * `Token:` aquire from developer portal
    * `Guild_ID:` Right click server icon and select 
        * ![Guild ID Image](img/Guild_ID.png) 
    * `Owner_ID:` Right click user and select 
        * ![Owner ID image](img/Owner_ID.png)
    * Config File Example:
    ```
    TOKEN = 'jalqwerjnzxljfasdnotarealtoken'
    GUILD_ID = 'asjdlkfanotrealguildid'
    OWNER_ID = 'notrealownderidmewqior'
    ```

2. Configure bot channel:
    * User: `/set-channel`
    * Bot:
        * ![Set Channel](img/set-channel.png)

3. Configure channels for bot to listen to:
    * **To add channels**
    * User: `/listen add {Channels}`
    * Bot:
        * ![Channel Add](img/listen%20add.png)

    * **To remove channels**
    * User: `/listen remove {Channels}`
    * Bot:
        * ![Channel Remove](img/listen%20remove.png)

4. Choice algorithm:
    * **Creators Algorithm**
    * User: `/algorithm True`
    * Bot:
        * ![Creator Algorithm](img/algorithm%20true.png)

    * **Markovify Algorithm**
    * User: `/algorithm False`
    * Bot:
        * ![Markovify Algorithm](img/algorithm%20false.png)

5. Train Bot (depending on channel size this may take some time):
    * If running for the first time use or want to start over training set `True`

    * User: `/train True`
    * Bot:
        * ![Training Start](img/Train%20Start.png)
        * ![Training Output](img/training%20output.png)

    * If you already have trained the bot once you can use `False` to add (If going over channel from first training it will duplicated the data.)
    * User: `/train False`
    * Bot:
        * ![Training Output False](img/training%20output%20false.png)

6. Getting the bot to talk:
    * User: `/mark`
    * Bot:
        * ![Mark](img/mark.png)
    
7. OPTIONAL: if you could like the bot talk every 15 seconds:
    * User: `/talk True`
    * Bot:
        * ![True Talk](img/talk%20true.png)

    * **The bot may say 1 or 2 more messages before fully stopping**
    * User: `/talk False`
    * Bot:
        * ![False Talk](img/talk%20false.png)

## Setup
download repo

### Config
Make a file called `config.py` and add the following.
```
TOKEN = 'jalqwerjnzxljfasdnotarealtoken'
GUILD_ID = 'asjdlkfanotrealguildid'
OWNER_ID = 'notrealownderidmewqior'
```