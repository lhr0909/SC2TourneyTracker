# coding: utf8
#
def index(): 
    #db = DAL('mssql://cheungkt:mechanes5@whale.cs.rose-hulman.edu/SC2tracker')
    tournies = db.executesql('SELECT Name, ID FROM Tournament')
    return dict(tournament = tournies)
    
def show():
    
    tourny = db.executesql('SELECT * FROM Tournament WHERE ID = ' + str(request.args(0)))
    

    form = FORM(INPUT(_name = 'Join', _type = 'submit'))
    if form.accepts(request,session):
        response.flash = 'Joined the tournament'
    return dict(test = tourny,form = form)
