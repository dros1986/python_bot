from Updater import Updater

def imageHandler(bot, message, chat_id, local_filename):
	print(local_filename)

if __name__ == "__main__":
	bot_id = '128366843:AAHovviK9AQDbcWJkM9JkqDAt8B5oLUUCQI'
	updater = Updater(bot_id)
	updater.setPhotoHandler(imageHandler)
	updater.start()