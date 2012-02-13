# coding: utf8
@auth.requires_login()
def index():
	return dict(message="hello from replay.py")

@auth.requires_login()
def upload():
	form = SQLFORM(db.Replay)
	if form.process().accepted:
		response.flash = "Replay Uploaded"
	elif form.errors:
		response.flash = "form has errors"
	return dict(form=form)