from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph//file/1a2f427f5aa185b6f49f6.jpg"
  

          
rizoel = "โง ๐๐๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐ โง\n\n"

rizoel += f"โโโโโโโโโโโโโโโโโโโโ\n"

rizoel += f"โฃโฃ **แดสแดสแดษด แด แดสsษชแดษด** : `3.9.6`\n"

rizoel += f"โฃโฃ **แดแดสแดแดสแดษด แด แดสsษชแดษด** : `{version.__version__}`\n"

rizoel += f"โฃโฃ **สแดษดแดXsแดแดแด แด แดสsษชแดษด**  : `{rizoelversion}`\n"

rizoel += f"โโโโโโโโโโโโโโโโโโโโ\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=R ONE,
                                  buttons=[
        [
        Button.url("แดสแดษดษดแดส", "https://t.me/R_0NE_xD"),
        Button.url("sแดแดแดแดสแด", "https://t.me/R_ONE_HU_VRO")
        ],
        [
        Button.url("โข สแดแดแด โข", "https://t.me/R_ONE_HU_VRO")
        ]
        ]
        )
    
