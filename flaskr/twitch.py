import os
from flask import Blueprint, request, render_template
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio
# https://pytwitchapi.dev/en/stable/
# https://pytwitchapi.dev/en/stable/modules/twitchAPI.eventsub.html

twitch_blueprint = Blueprint("twitch_blueprint", __name__)

@twitch_blueprint.route('/', methods =["GET", "POST"])
def authUser():
    if request.method == "POST":
       id = request.form.get("id")
       username = request.form.get("username")
       authID = request.form.get("authID")
       return id + username + authID
    return render_template("index.html")


async def twitch_example():
    # initialize the twitch instance, this will by default also create a app authentication for you
    twitch = await Twitch(os.environ.get("APP_TOKEN"), authenticate_app=False)
    # call the API for the data of your twitch user
    # this returns a async generator that can be used to iterate over all results
    # but we are just interested in the first result
    # using the first helper makes this easy.
    #await twitch.set_user_authentication('token', [], 'refresh_token')
    # print the ID of your user or do whatever else you want with it