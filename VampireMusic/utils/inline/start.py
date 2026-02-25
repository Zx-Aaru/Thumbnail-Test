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


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"], callback_data="help_pannel"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
    ]
    return buttons

# Pichli baar wala start_panel (Ise bhi check kar lein)
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_3"], callback_data="help_pannel"),
        ],
    ]
    return buttons
    
