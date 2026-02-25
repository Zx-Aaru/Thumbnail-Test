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
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ADD ME IN YOUR GROUP ➕",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📩 HELP AND COMMANDS 📩", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="📢 UPDATES", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="🎧 SUPPORT", url=config.SUPPORT_CHAT
            ),
        ],
        [
            InlineKeyboardButton(
                text="👤 OWNER", url=f"tg://openmessage?user_id={config.OWNER_ID}"
            ),
        ],
    ]
    return buttons
