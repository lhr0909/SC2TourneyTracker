# coding: utf8
# try something like
def index(): 
    if not auth.is_logged_in(): redirect(URL('default','user/login?_next=/' + request.application + '/default/index'))
    pid = str(db(db.Player.Auth_User_ID == auth.user_id).select()[0]['id'])
    gids = db.executesql("SELECT GID from Game_to_Players where PID = " + pid)

    return dict(games = gids,pid = pid)
