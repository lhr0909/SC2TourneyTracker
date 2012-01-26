# coding: utf8
# try something like
def index():
    db = DAL('mssql://cheungkt:mechanes5@whale.cs.rose-hulman.edu/SC2tracker')
    league = db.executesql('SELECT * FROM League')
    return dict(league=league)
