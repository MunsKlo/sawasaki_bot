import bot_logic.conditionsHandler


def get_right_guild(guilds):
    for guild in guilds:
        if guild.name == '5465616d':
            return guild

    return bot_logic.conditionsHandler.error
