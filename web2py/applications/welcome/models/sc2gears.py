import os
import subprocess
import shlex
from xml.dom.minidom import parseString
from time import sleep

requestFolder = request.folder.replace('\\', '/').replace(" ", "\\ ")
path = os.path.join(requestFolder, 'static/Sc2gears/')

store_path = os.path.join(requestFolder, 'uploads/replay_info/')

info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

#Partially working, needs more code to proceed
def parseReplay(fileName):
	args = shlex.split(path + "Sc2gears-win.cmd --print-game-info --xml-output " + requestFolder + 'uploads/' + fileName + " > " + store_path + fileName + '.xml')
	#return args
	subprocess.Popen(args, startupinfo=info)
	winner = None
	sleep(3)
	xmlString = ''.join((open(request.folder.replace('\\', '/') + 'uploads/replay_info/' + fileName + ".xml").readlines())[2:])
	doc = parseString(xmlString)
	map = doc.getElementsByTagName('mapName')[0].childNodes[0].data
	winner = doc.getElementsByTagName('winners')[0].childNodes[0].data
	players = doc.getElementsByTagName('type')
	playerIDs = set()
	winnerID = None
	for player in players:
		playerProfile = player.getAttribute('fullName').encode('ascii', 'ignore').split('/')
		playerRegion = playerProfile[1].lower()
		playerID = playerProfile[3]
		playerSplitter = playerProfile[2]
		playerName = playerProfile[0]
		profileURL = 'http://' + playerRegion + '.battle.net/sc2/en/profile/' + playerID + '/' + playerSplitter + '/' + playerName + '/'
		try:
			playerIDs.add(db(db.Player.BattlenetURL == profileURL).select()[0]['id'])
		except:
			return "Replay Error! Please Re-submit!"
		if playerName == winner:
			winnerID = db(db.Player.BattlenetURL == profileURL).select()[0]['id']
	return map, playerIDs, winnerID