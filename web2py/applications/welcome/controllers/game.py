# coding: utf8
# try something like
def index(): 
    pid = str(db(db.Player.Auth_User_ID == auth.user_id).select()[0]['id'])
    gids = db.executesql("SELECT GID from Game_to_Players where PID = " + pid)

    return dict(games = gids,pid = pid)
