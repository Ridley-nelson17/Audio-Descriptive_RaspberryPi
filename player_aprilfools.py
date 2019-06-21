"""
Copyright...

Author: Ridley Nelson
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
audio_files = ['accessibility_test.wav', 'ben-fart.wav']
audio_file_durations = ['648', '5']
afl = [False, False]

# Fun for April Fools Day
april_fools = True

while True:
	if GPIO.input(3) == False:
		if afl[0] == False:
			selected_file = 0
			if afl[1] == False:
				if april_fools == True:
					selected_file = random.choice(audio_files)
					subprocess.Popen(['aplay', '-qi', audio_files[selected_choice]], stdin=subprocess.PIPE)
				else:
					selected_choice = 0
					subprocess.Popen(['aplay', '-qi', audio_files[0]], stdin=subprocess.PIPE)
				afl[0] = True
				subprocess.Popen(['aplay', '-d', audio_file_durations[selected_choice]], stdin=subprocess.PIPE)
				#subprocess.Popen(['aplay', '-qi', audio_files[0]], stdin=subprocess.PIPE)
				print("Physical pin 3, BCM pin 2, blue button -- activated")
				time.sleep(3.5)
	elif GPIO.input(5) == False:
		if afl[1] == False:
			if afl[0] == False:
				afl[1] = True
				subprocess.Popen(['aplay','-qi', random.choice(audio_files)], stdin=subprocess.PIPE)
				print("Physical pin 5, BCM pin 3, yellow button -- activated")
				time.sleep(3.5)
	elif GPIO.input(7) == False:
		if afl[0]: afl[0] = False
		if afl[1]: afl[1] = False
		subprocess.call(['killall', 'aplay'])
		print('Physical pin 7, BCM pin 4, gray button -- activated')
		time.sleep(0.5)
