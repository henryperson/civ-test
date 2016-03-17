#!/usr/bin/env python

import sys
import os
import getpass

try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

try:
	import requests
except ImportError:
	print("ERROR: You need to 'pip install requests'")
	sys.exit()

def getSavePath():
	MAC = r"/Users/{user}/Documents/Aspyr/Sid Meier's Civilization 5/Saves/hotseat/(GMR) Play this one!.Civ5Save"
	WINDOWS = r"C:\Users\{user}\Documents\My Games\Sid Meier's Civilization 5\Saves\hotseat\(GMR) Play this one!.Civ5Save"
	username = getpass.getuser()
	
	if (os.path.exists(MAC.format(user=username))):
		return MAC.format(user=username)
	elif (os.path.exists(WINDOWS.format(user=username))):
		return WINDOWS.format(user=username)
	else:
		# To hardcode your save path, edit this variable:
		hardcoded_path = ""
		# Then delete the following two lines, and uncomment the last one
		print("Could not get path to your save file!")
		sys.exit()
		# return hardcoded_path

# Available here: http://multiplayerrobot.com/Download
AUTH_KEY = "IF6P0UINUC9U"
SAVE_PATH = getSavePath()

# Don't change these
GAME_ID = "22032"
USER_IDS = "76561198025032328_76561198041667942_76561198036882752_76561198059690428_76561198086637460"
GET_FILE_URL = "http://multiplayerrobot.com/api/Diplomacy/GetLatestSaveFileBytes"
GET_TURN_URL = "http://multiplayerrobot.com/api/Diplomacy/GetGamesAndPlayers"
POST_URL = "http://multiplayerrobot.com/api/Diplomacy/SubmitTurn"

root = tk.Tk()


def main():	
	root.title("Download or Upload?")
	dButton = tk.Button(root, text='Download', width=25, command=download)
	uButton = tk.Button(root, text='Upload', width=25, command=upload)
	dButton.pack()
	uButton.pack()
	root.mainloop()


def download():
	root.destroy()

	parameters = {'authKey': AUTH_KEY, 'gameID': GAME_ID}
	print("Making request...")
	r = requests.get(GET_FILE_URL, params = parameters)

	print("Writing save file...")
	with open(SAVE_PATH, 'wb') as f:
		f.write(r.content)
	print("Done.")
	sys.exit()


def upload():
	root.destroy()
	# print("Upload currently not supported!")
	
	turn_params = {'playerIDText': USER_IDS, 'authKey': AUTH_KEY}
	
	for i in range(5):
		print("Getting turn id (try {})...".format(i))
		r = requests.get(GET_TURN_URL, params = turn_params)
		if len(r.json()['Games']) > 0:
			break
	
	try:
		turn_id = r.json()['Games'][0]['CurrentTurn']['TurnId']
	except IndexError:
		print("Unable to reach server to find turn id. Please try again.")
		sys.exit()

	data = open(SAVE_PATH, 'rb').read()
	parameters = {'authKey': AUTH_KEY, 'turnId': turn_id}
	print("Posting file...")
	r = requests.post(POST_URL, params = parameters, data = data)
	print(r.json())

	sys.exit()


main()

