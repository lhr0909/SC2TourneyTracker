# coding: utf8
# try something like
def index(): 
    if not auth.is_logged_in(): redirect(URL('default','user/login?_next=/' + request.application + '/default/index'))
    players = db(db.Player.Auth_User_ID == auth.user_id).select()
    games = []
    for p in players:
        pid = p['id']
        games += db.executesql("SELECT GID from Game_to_Players where PID = " + str(pid))

    return dict(games = games)