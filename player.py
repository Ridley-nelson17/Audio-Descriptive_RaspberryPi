""" 
Title: player.py

Copyright

Author: Ridley Nelson

Purpopse: Interacts witrh the GPIO pins, when the physical pin 2 is shorted, the python program will run aplay (a music plsyer.)
"""

#send_signal(signal.SIGSTOP)from time import sleep
import RPi.GPIO as GPIO
import subprocess, random, os, time

# Ignore warnings from the GPIO board
GPIO.setwarnings(True)

# Use the physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Set pin 3 to be an input and initial value to be pulled up (on)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create a list of the Audio file(s)
audio_files = ['accessibility_test.wav']
audio_file_durations = ['648']

# Aplay file loop booleans
afl = [False]

# Create a counter of how many times someone presses a button
playerd_counter = [0, 0, 0]

while True:
	if GPIO.input(3) == False:
		if afl[0] == False:
			selected_choice = 0
			# Play the audio file
			subprocess.Popen(['aplay', '-qid', audio_file_durations[0], audio_files[0]], stdin=subprocess.PIPE)
			
			# Set aplayer playing boolean to True
			afl[0] = True
			
			# Print details to the console
			print("Physical pin 3, BCM pin 2, Blue button -- activated")
			
			# Sleep 3 seconds to prevent spamming and overload of the system
			time.sleep(3)
	elif GPIO.input(5) == False:
		print('Physical pin 5, BCM pin 3, Yellow button -- activated')
	elif GPIO.input(7) == False:
		# If aplayer is playing, make it false
		if afl[0]: afl[0] = False
		
		# Kill aplayer
		subprocess.call(['killall', 'aplay'])
		
		print('Physical pin 7, BCM pin 4, Gray button -- activated')
		
		# Add a sleep duration to prevent overload of the system
		time.sleep(0.5)
