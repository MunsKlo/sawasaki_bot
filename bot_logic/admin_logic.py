from bot_logic import conditionsHandler


def get_right_guild(guilds):
    for guild in guilds:
        if guild.name == '5465616d':
            return guild

    return conditionsHandler.error
