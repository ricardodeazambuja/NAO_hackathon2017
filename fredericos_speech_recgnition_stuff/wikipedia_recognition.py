#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import wikipedia
import speech_recognition as sr
from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559)
tts.say("Hello Frederico!")

# obtain audio from the microphone
r = sr.Recognizer()
while(True):
	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)

	# recognize speech using Sphinx
	'''try:
	    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
	except sr.UnknownValueError:
	    print("Sphinx could not understand audio")
	except sr.RequestError as e:
	    print("Sphinx error; {0}".format(e)) '''

	# recognize speech using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    mystring = r.recognize_google(audio)
	    print("Google Speech Recognition thinks you said " + mystring)
	except sr.UnknownValueError:
	    mystring = "Google Speech Recognition could not understand audio"
	    print(mystring)
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	'''
	# recognize speech using Google Cloud Speech
	GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
	try:
	    print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
	except sr.UnknownValueError:
	    print("Google Cloud Speech could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Cloud Speech service; {0}".format(e))

	# recognize speech using Wit.ai
	WIT_AI_KEY = "INSERT WIT.AI API KEY HERE" # Wit.ai keys are 32-character uppercase alphanumeric strings
	try:
	    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
	except sr.UnknownValueError:
	    print("Wit.ai could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Wit.ai service; {0}".format(e)) '''

	# recognize speech using Microsoft Bing Voice Recognition
	BING_KEY = "ca50a7d62c984432a4f7bcee3f4067c3" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
	try:
	    mycrosoftstring = r.recognize_bing(audio, key=BING_KEY)
	    print("Microsoft Bing Voice Recognition thinks you said " + mycrosoftstring)
	except sr.UnknownValueError:
	    print("Microsoft Bing Voice Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

	'''
	# recognize speech using Houndify
	HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE" # Houndify client IDs are Base64-encoded strings
	HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE" # Houndify client keys are Base64-encoded strings
	try:
	    print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
	except sr.UnknownValueError:
	    print("Houndify could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Houndify service; {0}".format(e))

	# recognize speech using IBM Speech to Text
	IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
	IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE" # IBM Speech to Text passwords are mixed-case alphanumeric strings
	try:
	    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
	except sr.UnknownValueError:
	    print("IBM Speech to Text could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from IBM Speech to Text service; {0}".format(e)) '''

	'''tts.say("Google thinks you said: " + str(mystring))
	tts.say("Mycrosoft thinks you said: " + str(mycrosoftstring))
	tts.say("I, personally, have no idea.") '''
	strstr = str(mystring)
	mystr = str(mycrosoftstring)
	if 'hello' in strstr:
		tts.say('Well, hello to you too!')	
	else:
		try:
		  # create proxy on ALMemory
		  memProxy = ALProxy("ALMemory","snap.local",9559)

		  #insertData. Value can be int, float, list, string
		  memProxy.insertData("myValueName1", "myValue1")

		  #getData
		  print "The value of myValueName1 is", memProxy.getData("myValueName1")

		  memProxy.raiseEvent("My event", str(mystring))
		  try:
			lastthing = strstr.split("about")[-1]
		  	thingtolookfor = (wikipedia.summary(lastthing, sentences=1))
		  	tts.say(str(thingtolookfor.encode('ascii', 'ignore')))
		  except:
			lastthing = mystr.split("about")[-1]
			thingtolookfor = (wikipedia.summary(lastthing, sentences=1))
		  	tts.say(str(thingtolookfor.encode('ascii', 'ignore'))
)
		except RuntimeError,e:
		  # catch exception
		  print "error insert data", e
