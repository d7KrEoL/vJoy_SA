#Just simple python script I use to friend all my devices with gtasa. It's not well-coded, but it's working well for me.
#So if someone needs solution - here's the one, will be appreciate if someone optimise or rewrite this, cz python is not my primary lang=)
def update():
	global IsCobra;
		
	if (joystick[controldev].x < 10000 and joystick[controldev].y > -10000):
		vJoy[0].x = joystick[controldev].x*20;
		if (vJoy[0].x < 200): vJoy[0].x = vJoy[0].x * 1.1;
	else:
		vJoy[0].x = joystick[controldev].x*60;
	if (joystick[controldev].y < 30000 and joystick[controldev].y > -30000):
		vJoy[0].y = joystick[controldev].y*20;
	else:		
		vJoy[0].y = joystick[controldev].y*60;
	
	vJoy[0].z = trackIR.yaw*500;
	if (trackIR.pitch < 130):
		vJoy[0].rz = trackIR.pitch*300;
	else:
		vJoy[0].rz = trackIR.pitch*700;
	
	if joystick[throttledev].x < -500: keyboard.setKeyDown(Key.W);
	else: keyboard.setKeyUp(Key.W);
	if joystick[throttledev].x > 500: keyboard.setKeyDown(Key.S);
	else: keyboard.setKeyUp(Key.S);
	
	if joystick[pedaldev].z < -300: keyboard.setKeyDown(Key.Q);
	else: keyboard.setKeyUp(Key.Q);
	if joystick[pedaldev].z > 300: keyboard.setKeyDown(Key.E);
	else: keyboard.setKeyUp(Key.E);	
	
	if IsCobra > 0:
		if joystick[controldev].getDown(6): 
      keyboard.setPressed(Key.RightControl);
		else: 
      keyboard.setKeyUp(Key.RightControl);
		if keyboard.getPressed(Key.NumberPadSlash): IsCobra = 0;
	else:
		if keyboard.getPressed(Key.NumberPadSlash): IsCobra = 1;
	
	
	vJoy[0].setButton(0, joystick[controldev].getDown(0));
	vJoy[0].setButton(1, joystick[controldev].getDown(1));
	vJoy[0].setButton(2, joystick[controldev].getDown(15));
	vJoy[0].setButton(3, joystick[controldev].getDown(9));
	vJoy[0].setButton(4, joystick[controldev].getDown(10));
	
	
	
if starting:
  #Here you should enter names of devices you have in your PC
	controldev = "Defender COBRA M5 USB Joystick";
	pedaldev = "VPC Rudder Pedals";
	throttledev = "Flight Throttle Quadrant";
	global NUM8;
	NUM8 = 0;
	global NUM2;
	NUM2 = 0;
	global IsCobra;
	IsCobra = 0;	


update()
