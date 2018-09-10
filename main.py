import signal
from sense_hat import SenseHat
from time import sleep
from set_color import set_color
from set_message import set_message

sense = SenseHat()
sense.clear()

white = (255,255,255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
brown = (165, 42, 42)
grey = (190, 190, 190)

color_presets = [white, red, green, blue, orange, yellow, cyan, magenta, brown, grey]
color = color_presets[0]

mode = ["joystick", "gyroscope", "voice"]
mode_index = 0

# Functions ----------------
def joystick_move_up(event):
	sense.clear()
def joystick_move_down(event):
	sense.clear()
def joystick_move_left(event):
	sense.clear()
def joystick_move_right(event):
	sense.clear()
def joystick_move_middle(event):
	global mode
	if event.action == "pressed":
		mode_index += 1
		if mode[mode_index] == "gyroscope" or mode[mode_index] == "voice":
			mode_index = 0

def clear():
	sense.clear()

def exit(signal, frame):
	clear()
	print("Bye!")
	sys.exit(0)

set_color()

# Main program -------------
if __name__ == '__init__':
	sense.stick.direction_up = joystick_move_up
	sense.stick.direction_down = joystick_move_down
	sense.stick.direction_left = joystick_move_left
	sense.stick.direction_right = joystick_move_right
	sense.stick.direction_middle = joystick_move_middle


	signal.signal(signal.SIGING, exit)
