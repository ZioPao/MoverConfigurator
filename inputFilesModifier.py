import steamclient
import os
import requests
from bs4 import BeautifulSoup

VR_TAG = '21978'


def __init__(self):
    steamvr_dir = "C:\\Users\\" + os.getlogin() + "\\Documents\\steamvr\\input\\"


def getInputFileName(game_id):
    input_file = "steam.app." + game_id + "_gamepad.json"
    return input_file


def modifyInputFile(input_file):
    # todo inserisci cose per json
    pass


# Returns a list of vr games in the user library
def getVrGames():
    users = steamclient.get_users()
    user = users[0]
    libraries = steamclient.get_libraries()
    games = user.games(libraries[:1])

    vr_games = list()
    for game in games:
        if checkIfVr(game.id):
            vr_games.append(game)

    return vr_games


def checkIfVr(game_id):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
    }
    URL = "https://steamdb.info/app/" + game_id
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #check per tag
    results = soup.find_all('a', class_='btn btn-sm btn-outline btn-tag')

    for r in results:
        if r.attrs.get('href')[5:-1] == VR_TAG:
            return True

    return False
