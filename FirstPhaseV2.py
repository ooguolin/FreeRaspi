# coding=utf-8
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
# import pyaudio
# import wave
print 'hi'
from amadeus import Flights
# CHUNK_SIZE = 1024
flights = Flights('GSzQprGAxBxZfvjhTk1qev1xIu5sZQro')
resp = []
def flightinspirationsearch(ori,date,price):
#string origin in airport codes
#string date in YYYY-MM-DD--YYYY-MM-DD
#int pric
    global resp
    resp = flights.inspiration_search(
    origin=ori,
    departure_date=date,
    max_price=price)
    print "Origin " + resp["origin"]
    print "Currency " + resp["currency"]
    print ""
    a = resp["results"]
    print type(a)
    print len(a)
   
    for i in range(len(a)):
        print "Departure Date "+ resp["results"][i]["departure_date"]
        print "Price " + resp["results"][i]["price"]
        print "Destination " + resp["results"][i]["destination"]
        print "Airline " + resp["results"][i]["airline"]
        print "Return Date " + resp["results"][i]["return_date"]
        print ""

# def play_wav(wav_filename, chunk_size=CHUNK_SIZE):
#     '''
#     Play (on the attached system sound device) the WAV file
#     named wav_filename.
#     '''

#     try:
#         print 'Trying to play file ' + wav_filename
#         wf = wave.open(wav_filename, 'rb')
#     except IOError as ioe:
#         sys.stderr.write('IOError on file ' + wav_filename + '\n' + \
#         str(ioe) + '. Skipping.\n')
#         return
#     except EOFError as eofe:
#         sys.stderr.write('EOFError on file ' + wav_filename + '\n' + \
#         str(eofe) + '. Skipping.\n')
#         return

#     # Instantiate PyAudio.
#     p = pyaudio.PyAudio()

#     # Open stream.
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#         channels=wf.getnchannels(),
#         rate=wf.getframerate(),
#                     output=True)

#     data = wf.readframes(chunk_size)
#     while len(data) > 0:
#         stream.write(data)
#         data = wf.readframes(chunk_size)

#     # Stop stream.
#     stream.stop_stream()
#     stream.close()

#     # Close PyAudio.
#     p.terminate()
flightinspirationsearch("BKK","2016-11-25--2016-11-30",800)
text_to_speech = TextToSpeechV1(
    
    password='XrUBzlYfOnDT',
    username='b72398ec-b801-498a-a1ac-86e21e6d3bbd',
    x_watson_learning_opt_out=True)  # Optional flag

print(json.dumps(text_to_speech.voices(), indent=2))

with open(join(dirname(__file__), 'output.wav'), 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize('The cheapest flight to America is ' + resp["results"][1]["price"], accept='audio/wav', voice="en-US_AllisonVoice"))

print(json.dumps(text_to_speech.pronunciation('Watson', pronunciation_format='spr'), indent=2))

print(json.dumps(text_to_speech.customizations(), indent=2))

# print(json.dumps(text_to_speech.create_customization('test-customization'), indent=2))

# print(text_to_speech.update_customization('YOUR CUSTOMIZATION ID', name='new name'))

# print(json.dumps(text_to_speech.get_customization('YOUR CUSTOMIZATION ID'), indent=2))

# print(json.dumps(text_to_speech.get_customization_words('YOUR CUSTOMIZATION ID'), indent=2))

# print(text_to_speech.add_customization_words('YOUR CUSTOMIZATION ID',
#                                              [{'word': 'resume', 'translation': 'rɛzʊmeɪ'}]))

# print(text_to_speech.set_customization_word('YOUR CUSTOMIZATION ID', word='resume',
#                                             translation='rɛzʊmeɪ'))

# print(json.dumps(text_to_speech.get_customization_word('YOUR CUSTOMIZATION ID', 'resume'), indent=2))

# print(text_to_speech.delete_customization_word('YOUR CUSTOMIZATION ID', 'resume'))

# print(text_to_speech.delete_customization('YOUR CUSTOMIZATION ID'))
