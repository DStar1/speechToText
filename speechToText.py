import speech_recognition as sr

fileName = "thoughtInfinity"
r = sr.Recognizer()



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

def recognizeSpeech(fileName=None):
	audio = audioOrRecord(fileName)
	if fileName:
		with audio as source:
			r.adjust_for_ambient_noise(source)
			audio = r.record(source, offset=4, duration=30)

	# print("Hello!",type(audio), "\n")
	speech = r.recognize_google(audio)
	print(speech)
	return speech

# # print(speech)
while True:
	recognizeSpeech()

# with open(f"{fileName}.txt", "w") as f:
# 	f.write(recognizeSpeech())#fileName))

