import speech_recognition as sr

def record():
	mic = sr.Microphone()
	# print(sr.Microphone.list_microphone_names())
	with mic as source:
		audio = r.listen(source)
	return audio


def audioOrRecord(fileName):
	if fileName:
		audio = sr.AudioFile(f'/Users/harrison/Downloads/{fileName}.wav')
		# audio = sr.AudioFile('/Users/harrison/Downloads/infinSpeech.aiff')
		# audio = sr.AudioFile('/Users/harrison/Downloads/OSR_us_000_0010_8k.wav')
	else:
		audio = record()
	return audio

def recognizeSpeech(currentSkip, fileName=None):
	# global(currentSkip)
	audio = audioOrRecord(fileName)
	if fileName:
		with audio as source:
			r.adjust_for_ambient_noise(source)
			audio = r.record(source, offset=currentSkip, duration=skip)

	# print("Hello!",type(audio), "\n")
	speech = r.recognize_google(audio)
	print(speech)
	return speech

if __name__ == "__main__":
	fileName = "thoughtInfinity"
	r = sr.Recognizer()
	skip = 10
	currentSkip = 4
	tryFlag = 1
	endTrying = 60
	while True:
		try:
			# text = ""
			text = recognizeSpeech(currentSkip, fileName) + '\n'
			currentSkip+=skip-1
			with open(f"{fileName}.txt", "a+") as f:
				f.write(text)#fileName))
			# if skip <= 10:
			# 	tryFlag = 1
			# else:
			# 	tryFlag = -1
			skip = 10
		except:
			# skip+=tryFlag
			skip+=1
			print("SKIP ERROR")
			if skip >= endTrying:
				end = input("Is this the end of the audio? (0 = no, otherwise yes)")
				if end == "0":
					endTrying+=60
				else:
					exit()

