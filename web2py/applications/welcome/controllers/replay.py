# coding: utf8
def index(): return dict(message="hello from replay.py")

def upload():
	gameID = request.args(0)
	form = SQLFORM(db.Replay)
	if form.process().accepted:
		replayID = form.vars.id
		map, playerIDs, winnerID = parseReplay(db(db.Replay.id == replayID).select()[0]['FileLocation'])
		if map == db(db.Map.id == db(db.Game.id == gameID).select()[0]['MapID']).select()[0]['Name']:
			playerCount = 0
			for record in db(db.Game_to_Players.GID == gameID).select():
				if record['PID'] not in playerIDs:
					break
				else:
					playerCount += 1
			if playerCount == len(playerIDs):
				db.executesql('EXEC [report_game_sp] ' + str(winnerID) + ", " + str(replayID) + ", " + str(gameID))
				response.flash = "Game Reported"
			else:
				response.flash = "Replay Error! Please re-submit!"
		else:
			response.flash = "Replay Error! Please re-submit!"
	elif form.errors:
		response.flash = "form has errors"
	return dict(form=form)