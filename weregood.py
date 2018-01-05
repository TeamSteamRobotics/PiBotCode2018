import pigpio
import curses
scr=curses.initscr()
pi=pigpio.pi()
input1 = 27
input2 = 17
while True:
	key=scr.getch()
	if (key == ord('w')):
		pi.set_PWM_dutycycle(4,255)
		pi.write(input1, 1)
                pi.write(input2, 0)
		print('w')
	elif (key == ord('s')):	
		pi.set_PWM_dutycycle(4,128)
                pi.write(input1, 0)
                pi.write(input2, 1)
		print('s')
	else:
		pi.set_PWM_dutycycle(4,0)
		print('stop')

