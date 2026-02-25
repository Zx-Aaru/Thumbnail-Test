# -----------------------------------------------
# 🔸 VampireMusic Project
# 🔹 Developed & Maintained by: Vampire Bots (https://github.com/TEAM-VAMPIRE-OP)
# 📅 Copyright © 2025 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by TEAM-VAMPIRE-OP
# -----------------------------------------------


from pyrogram.types import InlineKeyboardButton
import config
from VampireMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ADD ME IN YOUR GROUP ➕",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📩 HELP AND COMMANDS 📩", callback_data="help_pannel"
            ),
        ],
        [
            InlineKeyboardButton(
                text="📢 UPDATES", url=f"https://t.me/AarumiBots" # Apna channel link dalein
            ),
            InlineKeyboardButton(
                text="🎧 SUPPORT", url=f"https://t.me/AarumiChat" # Apna support group link dalein
            ),
        ],
        [
            InlineKeyboardButton(
                text="👤 OWNER", url=f"https://t.me/AarumiBots" # Apna username dalein
            ),
        ],
    ]
    return buttons
    
