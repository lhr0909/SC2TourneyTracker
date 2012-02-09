# coding: utf8

@auth.requires_login()
def create():
	form = SQLFORM(db.Player)
	form.vars.Auth_User_ID = auth.user_id
	if form.process().accepted:
		response.flash = "New Profile Created!"
	elif form.errors:
		response.flash = "form has errors"
	return dict(form=form)
	
@auth.requires_login()	
def edit():
	record = db.Player(request.args(0))
	form = SQLFORM(db.Player, record)
	if form.process().accepted:
		response.flash = "New Profile Created!"
	elif form.errors:
		response.flash = "form has errors"
	return dict(form=form)
