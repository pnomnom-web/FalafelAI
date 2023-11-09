import os
from flask import Blueprint, request, render_template
from database import db
from models import User
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio
# https://pytwitchapi.dev/en/stable/
# https://pytwitchapi.dev/en/stable/modules/twitchAPI.eventsub.html

twitch_blueprint = Blueprint("twitch_blueprint", __name__)

#  ---------Testing functions---------
@twitch_blueprint.route('/users')
def printUsers():
    users = User.print_all_user()
    return render_template("show_users.html", users=users)

@twitch_blueprint.route('/', methods =["GET", "POST"])
def authUser():
    if request.method == "POST":
        id = request.form.get("id")
        username = request.form.get("username")
        authID = request.form.get("authID")

        data = User(id, username, authID)
        db.session.add(data)
        db.session.commit()
        return render_template("index.html")

    return render_template("index.html")
#  ---------Testing functions---------

async def twitch_example():
    # initialize the twitch instance, this will by default also create a app authentication for you
    twitch = await Twitch(os.environ.get("APP_TOKEN"), authenticate_app=False)
    # call the API for the data of your twitch user
    # this returns a async generator that can be used to iterate over all results
    # but we are just interested in the first result
    # using the first helper makes this easy.
    #await twitch.set_user_authentication('token', [], 'refresh_token')
    # print the ID of your user or do whatever else you want with it