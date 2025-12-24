import re
from pyrogram import Client, filters

# Chats where filter is ON
BADWORD_CHATS = set()

# Text bad words
BAD_WORDS = [
    "sex", "porn", "nude", "xxx", "boobs", "pussy", "dick",
    "lund", "chod", "chutiya", "randi", "gaand", "bhosdi"
]

BADWORD_REGEX = re.compile(r"|".join(BAD_WORDS), re.IGNORECASE)

# Adult sticker keywords (pack name / emoji based)
ADULT_STICKER_WORDS = [
    "sex", "porn", "18+", "xxx", "nude", "hot", "adult", "nsfw"
]

ADULT_STICKER_REGEX = re.compile(
    r"|".join(ADULT_STICKER_WORDS), re.IGNORECASE
)


# ---------- ON / OFF COMMAND ----------
@Client.on_message(filters.command("badword") & filters.group)
async def badword_toggle(client, message):
    if not message.from_user:
        return

    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if member.status not in ("administrator", "creator"):
        return

    chat_id = message.chat.id
    text = message.text.lower()

    if "on" in text:
        BADWORD_CHATS.add(chat_id)
        await message.reply("✅ Bad Word + Nude Sticker Filter ON")
    elif "off" in text:
        BADWORD_CHATS.discard(chat_id)
        await message.reply("❌ Bad Word + Nude Sticker Filter OFF")
    else:
        await message.reply("Use: `/badword on` or `/badword off`")


# ---------- TEXT FILTER ----------
@Client.on_message(filters.group & filters.text)
async def badword_handler(client, message):
    try:
        chat_id = message.chat.id
        if chat_id not in BADWORD_CHATS:
            return

        if not message.from_user:
            return

        member = await client.get_chat_member(chat_id, message.from_user.id)

        text = message.text or ""

        # Command bypass
        if text.startswith(("/", "!", ".")):
            return

        if BADWORD_REGEX.search(text):
            await message.delete()

    except Exception:
        return


# ---------- STICKER FILTER (NUDE / ADULT) ----------
@Client.on_message(filters.group & filters.sticker)
async def sticker_filter(client, message):
    try:
        chat_id = message.chat.id
        if chat_id not in BADWORD_CHATS:
            return

        if not message.from_user:
            return

        member = await client.get_chat_member(chat_id, message.from_user.id)
        if member.status in ("administrator", "creator"):
            return

        sticker = message.sticker

        # Check emoji
        if sticker.emoji and ADULT_STICKER_REGEX.search(sticker.emoji):
            await message.delete()
            return

        # Check sticker set name
        if sticker.set_name and ADULT_STICKER_REGEX.search(sticker.set_name):
            await message.delete()
            return

    except Exception:
        return
