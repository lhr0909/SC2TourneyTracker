import os
import subprocess
import shlex

requestFolder = request.folder.replace('\\', '/').replace(" ", "\\ ")
path = os.path.join(requestFolder, 'static/Sc2gears/')

store_path = os.path.join(requestFolder, 'uploads/replay_info/')

info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

#Partially working, needs more code to proceed
def parseReplay():
	args = shlex.split(path + "Sc2gears-win.cmd --print-game-info --xml-output sample.SC2Replay > " + store_path + "sample.xml")
	#return args
	return subprocess.Popen(args, startupinfo=info)