from Updater import Updater
import os, sys, platform

def fileparts(fn):
    (dirName, fileName) = os.path.split(fn)
    (fileBaseName, fileExtension) = os.path.splitext(fileName)
    return dirName, fileBaseName, fileExtension


def imageHandler(bot, message, chat_id, local_filename):
	# send message to user
	bot.sendMessage(chat_id, "Hi, please wait until the image is ready")
	# set matlab command
	if 'Linux' in platform.system():
		matlab_cmd = 'matlab'
	else:
		matlab_cmd = '"C:\\Program Files\\MATLAB\\R2014b\\bin\\matlab.exe"'
	# set command to start matlab script "edges.m"
	cmd = matlab_cmd + " -nodesktop -nosplash -r \"edges(\'" + local_filename + "\'); quit\""
	print(cmd)
	# lunch command
	os.system(cmd)
	# send back the manipulated image
	dirName, fileBaseName, fileExtension = fileparts(local_filename)
	new_fn = os.path.join(dirName, fileBaseName + '_ok' + fileExtension)
	bot.sendImage(chat_id, new_fn, "")



if __name__ == "__main__":
	bot_id = '128366843:AAHovviK9AQDbcWJkM9JkqDAt8B5oLUUCQI'
	updater = Updater(bot_id)
	updater.setPhotoHandler(imageHandler)
	updater.start()