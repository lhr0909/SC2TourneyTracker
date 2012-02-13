# coding: utf8
#
def index(): 
    #db = DAL('mssql://cheungkt:mechanes5@whale.cs.rose-hulman.edu/SC2tracker')
    tournies = db.executesql('SELECT Name, ID FROM Tournament')
    return dict(tournament = tournies)
    
def show():
    
    tourny = db.executesql('SELECT * FROM Tournament WHERE ID = ' + str(request.args(0)))
    form = FORM(INPUT( _type = 'submit',_value="Join"))
    if form.process().accepted:
        response.flash = 'Joined the tournament!'
        pid = db(db.Player.Auth_User_ID == auth.user_id).select()[0]['id']
        #pid = db.executesql('SELECT ID FROM Player WHERE Auth_User_ID = ' + str(auth.user_id))
        db.executesql('EXEC [player_to_tourney_sp] ' + str(pid) + ", " + str(request.args(0)))
    return dict(tourny = tourny,form = form)


def join():
    
    playerID = auth.user.ID
    tournyID = request.args(0)
    #TODO: add tourny
    
    redirect(URL('show/'+request.args(0)))
    response.flash = 'Joined the tournament'
    return dict(pid = request.args(0), message = 'Joined the tournament')
