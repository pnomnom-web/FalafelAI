
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio
# https://pytwitchapi.dev/en/stable/
# https://pytwitchapi.dev/en/stable/modules/twitchAPI.eventsub.html


async def twitch_example():
    # initialize the twitch instance, this will by default also create a app authentication for you
    twitch = await Twitch('iddji3s35i9mok9ruffgs7cyge1rxf', authenticate_app=False)
    # call the API for the data of your twitch user
    # this returns a async generator that can be used to iterate over all results
    # but we are just interested in the first result
    # using the first helper makes this easy.
    await twitch.set_user_authentication('token', [], 'refresh_token')
    # print the ID of your user or do whatever else you want with it

# run this example
asyncio.run(twitch_example())