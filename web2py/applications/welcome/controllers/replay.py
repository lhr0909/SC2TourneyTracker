# coding: utf8
def index(): return dict(message="hello from replay.py")

def upload():
	form = SQLFORM(db.Replay)
	if form.process().accepted:
		response.flash = "Replay Uploaded"
	elif form.errors:
		response.flash = "form has errors"
	return dict(form=form)