from .. import Riz, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://te.legra.ph/file/1812d88915cc11cdd2c8b.jpg"

Riz_Help = "ð¥ ð_ððð ð« ð¦ð£ðð  ð¥\n\n"
 
Riz_Help += f"__á´á´á´s á´á´ á´ÉªÊá´ÊÊá´ ÉªÉ´ ÊÉªá´¢á´á´Ê x sá´á´á´__\n\n"

Riz_Help += f" â§ ððð´ðð±ð¾ð ð²ð¼ð³ð â§\n\n"

Riz_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots\n\n"
 
Riz_Help += f" â§ ð»ð´ð°ðð´ ð²ð¼ð³ â§\n\n"

Riz_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
Riz_Help += f" â§ ðð¿ð°ð¼ ð²ð¼ð³ð â§\n\n"

Riz_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n\n"
 
Riz_Help += f"á´ÊÉªá´á´ Êá´Êá´á´¡ Êá´á´á´á´É´ Òá´Ê á´á´Êá´ ÉªÉ´Òá´.\n\n"

Riz_Help += f"Â© @R_0NE_xD | @R_ONE_HU_VRO\n"


@Riz.on(events.NewMessage(pattern=".help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Riz_Help,
                                  buttons=[
        [
        Button.url("á´ÊÊ á´á´á´s", "https://telegra.ph/Rðâð¼--Oá­-09-25-2")
        ],
        [
        Button.url("á´Êá´É´É´á´Ê", "https://t.me/R_0NE_xD")
        ] 
        ]
        )                                                         
