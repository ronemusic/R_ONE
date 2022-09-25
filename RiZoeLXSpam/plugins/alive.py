from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph//file/1a2f427f5aa185b6f49f6.jpg"
  

          
rizoel = "✧ 𝐙𝐈𝐍𝐃𝐃𝐀 𝐇𝐔 𝐁𝐇𝐀𝐈 𝐓𝐔 𝐀𝐏𝐍𝐀 𝐊𝐀𝐀𝐌 𝐊𝐑 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **ʀɪᴢᴏᴇʟXsᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"
         
                                    
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=R ONE,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/R_0NE_xD"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/R_ONE_HU_VRO")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://t.me/R_ONE_HU_VRO")
        ]
        ]
        )
    
