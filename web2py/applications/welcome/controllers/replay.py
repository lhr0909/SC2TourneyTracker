# coding: utf8
def index(): return dict(message="hello from replay.py")

def upload():
	gameID = request.args(0)
	form = SQLFORM(db.Replay)
	if form.process().accepted:
		replayID = form.vars.id
		map, playerIDs, winnerID = parseReplay(db(db.Replay.id == replayID).select()[0]['FileLocation'])
		if map == str(db.executesql("SELECT m.Name FROM Map m, Game g WHERE m.id = g.MapID AND g.id = " + gameID)[0][0]):
			playerCount = 0
			for record in db.executesql("SELECT * FROM Game_to_Players WHERE GID = " + gameID):
				if record[1] not in playerIDs:
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