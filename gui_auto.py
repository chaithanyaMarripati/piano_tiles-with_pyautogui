import pyautogui as gui 
gui.PAUSE=0
while True:
	im=gui.screenshot()
	if im.getpixel((633,662))==(17,17,17):
		gui.click((633,662))
	if im.getpixel((734,662))==(17,17,17):
		gui.click((734,662))
	if im.getpixel((835,662))==(17,17,17):
		gui.click((835,662))
	if im.getpixel((940,662))==(17,17,17):
		gui.click((940,662))