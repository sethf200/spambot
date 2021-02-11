import pyautogui, time
time.sleep(10)
f = open("beemovie", "r")
for word in f:
	pyautogui.typewrite(word, interval=0.02)
	pyautogui.press("enter")	
