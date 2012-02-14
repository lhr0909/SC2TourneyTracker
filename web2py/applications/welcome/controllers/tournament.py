# coding: utf8
#
def index(): 
    #db = DAL('mssql://cheungkt:mechanes5@whale.cs.rose-hulman.edu/SC2tracker')
    tournies = db.executesql('SELECT Name, ID, Limit FROM Tournament')
    return dict(tournament = tournies)
    
def show():
    if not auth.is_logged_in(): redirect(URL('default','user/login?_next=/' + request.application + '/default/index'))
    tourny = db.executesql('SELECT * FROM Tournament WHERE ID = ' + str(request.args(0)))
    pids = db(db.Player.Auth_User_ID == auth.user_id).select()
    pnames = []
    for player in pids:
        
        pnames += db.executesql("SELECT InGameName FROM Player WHERE ID = "+str(player['id']))[0]
    form = FORM('Join as : ', SELECT(pnames,_name = "Player",requires=IS_IN_SET(pnames)),INPUT(_type='submit',_value='Join'))
    if form.accepts(request,session):
        
        playerName=str(form.vars['Player'])
        pid = db.executesql("SELECT ID FROM Player WHERE Auth_User_Id = " + str(auth.user_id) + " AND InGameName = '" + playerName+"'")[0]
        inTourney = db.executesql("SELECT * FROM Players_in_Tournament WHERE PID = "+ str(pid[0]) + " AND TID = " + str(request.args(0)))
        if len(inTourney) > 0:
            response.flash = str(playerName) + " is already in the tournament!"
        else :
            db.executesql('EXEC [player_to_tourney_sp] ' + str(pid[0]) + ", " + str(request.args(0)))
            response.flash = "Joined the tournament"
        

    return dict(tourny = tourny,form = form,v = form.vars)
