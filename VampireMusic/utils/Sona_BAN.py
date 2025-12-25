from pyrogram import filters

def admin_filter():
    async def func(_, __, message):
        return bool(message.from_user and message.from_user.is_admin)
    return filters.create(func)
