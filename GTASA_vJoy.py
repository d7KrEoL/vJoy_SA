#Just simple python script I use to friend all my devices with singleplayer gtasa or samp. It's not well-coded, but it's working well for me.
#So if someone needs solution - here's the one, will be appreciate if someone optimise or rewrite this, cz python is not my primary lang=)
#Простой скрипт для vJoy, который я использую чтобы "подружить" мои устройства с игрой гта/самп. Здесь по большей части быдлокод, но мне хватает того что он работает
#Если кому-то ещё нужно готовое решение - то можете забрать его, буду так же рад, если у кого-нибудь дойдут руки до того чтобы оптимизировать, или вообще переписать этот код
def update():
	global IsCobra;

	#Joystick axis controls / Оси джойстика
	if (joystick[controldev].x < 10000 and joystick[controldev].y > -10000):
		vJoy[0].x = joystick[controldev].x*20;
		if (vJoy[0].x < 200): vJoy[0].x = vJoy[0].x * 1.1;
	else:
		vJoy[0].x = joystick[controldev].x*60;
	if (joystick[controldev].y < 30000 and joystick[controldev].y > -30000):
		vJoy[0].y = joystick[controldev].y*20;
	else:		
		vJoy[0].y = joystick[controldev].y*60;

	#TrackIR axis controls / Оси трекира
	vJoy[0].z = trackIR.yaw*500;
	if (trackIR.pitch < 130): vJoy[0].rz = trackIR.pitch*300;
	else: vJoy[0].rz = trackIR.pitch*700;

	#Throttle axis controls / Оси ручки управления двигателем, в игре как W S, потому что на данный момент нет информации есть ли в гта вообще возможность управлять тягой, как осью.
	if joystick[throttledev].x < -500: keyboard.setKeyDown(Key.W);
	else: keyboard.setKeyUp(Key.W);
	if joystick[throttledev].x > 500: keyboard.setKeyDown(Key.S);
	else: keyboard.setKeyUp(Key.S);

	#Pedal axis controls (in game it's QE for now, I just don't know if there any way to make it an axis) / Оси педалей, работают аналогично с РУД
	if joystick[pedaldev].z < -300: keyboard.setKeyDown(Key.Q);
	else: keyboard.setKeyUp(Key.Q);
	if joystick[pedaldev].z > 300: keyboard.setKeyDown(Key.E);
	else: keyboard.setKeyUp(Key.E);	

	#Joyckick hotkeys / Горячие клавиши джойстика
	if IsCobra > 0:
		if joystick[controldev].getDown(6): keyboard.setPressed(Key.RightControl);
		else: keyboard.setKeyUp(Key.RightControl);
		if keyboard.getPressed(Key.NumberPadSlash): IsCobra = 0;
	else:
		if keyboard.getPressed(Key.NumberPadSlash): IsCobra = 1;
	
	vJoy[0].setButton(0, joystick[controldev].getDown(0));
	vJoy[0].setButton(1, joystick[controldev].getDown(1));
	vJoy[0].setButton(2, joystick[controldev].getDown(15));
	vJoy[0].setButton(3, joystick[controldev].getDown(9));
	vJoy[0].setButton(4, joystick[controldev].getDown(10));
	
	
	
if starting:
  	#Here you should enter names of devices you have in your PC / Здесь вам нужно ввести название ваших устройств ввода
	controldev = "Defender COBRA M5 USB Joystick";#Joystick / Джойстик
	pedaldev = "VPC Rudder Pedals"; #Pedals / Педали
	throttledev = "Flight Throttle Quadrant";#Throttle / Ручка управления двигателем

	#Just variables
	global IsCobra;
	IsCobra = 0;	


update()
