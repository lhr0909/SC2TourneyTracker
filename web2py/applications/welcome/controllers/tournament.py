# coding: utf8
#
def index(): 
    db = DAL('mssql://cheungkt:mechanes5@whale.cs.rose-hulman.edu/SC2tracker')
    return dict(message="hello from tournament.py")
