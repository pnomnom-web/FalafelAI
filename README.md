
# Pet AI for Twitch
FalafelAI is based off of this rat bastard here holding a knife.
![Alt text](flaskr/static/IMG_7847.png)

He's here to make memes and chew gum. Still a wip project. Eventually we do want to incorporate OpenAI GPT-3 to give him a personality, but first we want to give him interactions with twitch alerts and channel point redeems.

## Set up your environment

1. Fork this repo to your own GitHub account
2. Clone this repo to your local machine using GitHub Desktop or Git CML

### **Windows**

**Giving script running privileges**

1. Open Powershell with administrator privileges
2. Run command: `Set-ExecutionPolicy RemoteSigned`
3. Enter `y` to accept Policy Change


**Installing Dependencies**

This is for providing virtual dependencies for the project. You need to manually install a .venv folder
1. `cd projectFolder`
2. Create a `.venv` in the project folder directory
3. Run `py -3 -m venv .venv`
4. Activate virtual python environment: `.venv\Scripts\activate`
5. Install dependencies: `pip install -r requirements.txt`

**To run project**
1. Execute `python .\flaskr\app.py`
2. Go to http://localhost:5000
3. Yipee

**You will need to manually close the project and rerun it again to have changes take place. I'll try to find a way to streamline the process so it changes when you save a file**

**Layout may be subject to change as there could be more python files**

## Main features (for now)
- Web app is ran locally initially. User will need to run the software to interact with the streaming software.
- A PNG/GIF that works similar to a PNGtuber, but also uses TTS to interact with the audience.
- Uses twitch API to react to channel point redeems, alerts (followers, subs, cheer, etc.).
- Can be outputted as a browser source to use in streaming software (OBS, SLOBS, Twitch Studio).

## Future Features
- Incorporate OpenAI GPT-3 (or 4) so that the PNG can have custom responses or respond to questions.
- Give the software access to the internet so users do not have to run it locally.
- Allow monitization to fund for OpenAI and hardware usage.
- Username + password to allow unique accounts for each user.