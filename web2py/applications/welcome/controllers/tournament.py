# coding: utf8
#

from contrib.pymysql.converters import *

def index(): 
    #db = DAL('mssql://cheungkt:mechanes5@whale.cs.rose-hulman.edu/SC2tracker')
    tournies = db.executesql('SELECT Name, ID, Limit FROM Tournament')
    return dict(tournament = tournies)
    
@auth.requires_login()  
def show():
    tourny = db.executesql('SELECT * FROM Tournament WHERE ID = ' + str(request.args(0)))
    pids = db(db.Player.Auth_User_ID == auth.user_id).select()
    pnames = []
    for player in pids:
        pnames += db.executesql("SELECT InGameName FROM Player WHERE ID = "+str(player['id']))[0]
    form = FORM('Join as : ', SELECT(pnames,_name = "Player",requires=IS_IN_SET(pnames)),INPUT(_type='submit',_value='Join'))
    
    if form.accepts(request,session):
        playerName=str(form.vars['Player'])
        pid = db.executesql("SELECT ID FROM Player WHERE Auth_User_Id = " + str(auth.user_id) + " AND InGameName = '" + playerName+"'")[0]
        try:
           db.executesql('EXEC [player_to_tourney_sp] ' + str(pid[0]) + ", " + str(request.args(0)))
           response.flash = "Joined the tournament"
        except Exception, err:
           response.flash = "You already have an account in the tournament. You can only have 1 account in the tournament"

    return dict(tourny = tourny,form = form,v = form.vars)
    
@auth.requires_login()    
def create():
    mids = db.executesql("SELECT ID from Map_pool")
   
    mapPools = []
    for m in mids:
        mapPools += db.executesql("SELECT Name from Map_pool WHERE ID = " + str(m[0]))[0]
    form = FORM(DIV("Map Pool :" , SELECT(mapPools, _name = "mapPool",requires=IS_IN_SET(mapPools))), 
                               DIV("Name :" , INPUT(_name="name", requires=IS_NOT_EMPTY())),
                               DIV("Players :", INPUT(_name="players", requires=IS_NOT_EMPTY())),
                               DIV(INPUT(_type='submit',_value='Create')))
    if form.accepts(request,session):
        
        name = escape_string(str(form.vars['name']))
        if name.find(";") != -1 or name.find(",") != -1 or name.find("--") != -1 or name.find(" ") != -1 :
            response.flash = "Invalid Name"
        else:    
            mapPool = str(form.vars['mapPool'])
            players = escape_int(form.vars['players'])
            mapPoolID = str(db.executesql("SELECT ID FROM Map_pool WHERE Name = '"+mapPool + "'")[0][0])
        
            db.executesql("EXEC [dbo].[create_tournament_sp] " + name + " , " + mapPoolID + ', ' + str(auth.user_id) + ', ' + str(players))
            response.flash = "Tournament Create"
    return dict(form = form)
