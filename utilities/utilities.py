from random import choice

from emoji import emojize

import settings


def get_emoji(user_data):
    if "emoji" not in user_data:
        smile = choice(settings.USER_EMOJI)
        smile = emojize(smile, use_aliases=True)
        user_data["emoji"] = smile
    return user_data["emoji"]
