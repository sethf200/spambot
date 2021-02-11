import pyautogui, time
time.sleep(10)
f = open("beemovie", "r")
for word in f:
	pyautogui.press("/")
	pyautogui.typewrite(word, interval=0.05)
	pyautogui.press("enter")	
