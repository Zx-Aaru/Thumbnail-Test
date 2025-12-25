from pyrogram import filters

def admin_filter(_, __, message):
    if not message.from_user:
        return False
    try:
        member = message.chat.get_member(message.from_user.id)
        return member.status in ("administrator", "creator")
    except:
        return False

admin_filter = filters.create(admin_filter)
