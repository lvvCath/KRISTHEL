import subprocess
import time
import json
import webbrowser
import pyscreenshot as ImageGrab
from difflib import get_close_matches
import random
from random import choice
from pynput.keyboard import Key, Controller


def isContain(text, lst):
	for word in lst:
		if word in text:
			return True
	return False

# FUNCTION: Window App Operations (Maximize, Minimize, Close, Move, Switch) =======================================
class WindowOpt:
	def __init__(self):
		self.keyboard = Controller()

	def openWindow(self):
		self.maximizeWindow()

	def closeWindow(self):
		self.keyboard.press(Key.alt_l)
		self.keyboard.press(Key.f4)
		self.keyboard.release(Key.f4)
		self.keyboard.release(Key.alt_l)

	def minimizeWindow(self):
		for i in range(2):
			self.keyboard.press(Key.cmd)
			self.keyboard.press(Key.down)
			self.keyboard.release(Key.down)
			self.keyboard.release(Key.cmd)
			time.sleep(0.05)

	def maximizeWindow(self):
		self.keyboard.press(Key.cmd)
		self.keyboard.press(Key.up)
		self.keyboard.release(Key.up)
		self.keyboard.release(Key.cmd)

	def moveWindow(self, query):
		self.keyboard.press(Key.cmd)

		if "left" in query:
			self.keyboard.press(Key.left)
			self.keyboard.release(Key.left)
		elif "right" in query:
			self.keyboard.press(Key.right)
			self.keyboard.release(Key.right)
		elif "down" in query:
			self.keyboard.press(Key.down)
			self.keyboard.release(Key.down)
		elif "up" in query:
			self.keyboard.press(Key.up)
			self.keyboard.release(Key.up)
		self.keyboard.release(Key.cmd)

	def switchWindow(self):
		self.keyboard.press(Key.alt_l)
		self.keyboard.press(Key.tab)
		self.keyboard.release(Key.tab)
		self.keyboard.release(Key.alt_l)

	def takeScreenShot(self):
		name = 'screenshots/AI-ss_' + str(random.randint(0, 1000000)) + '.png'
		image = ImageGrab.grab()
		image.show()
		image.save(name)


def winOpt(query):
	w = WindowOpt()
	if isContain(query, ['open']):
		w.openWindow()
	elif isContain(query, ['close']):
		w.closeWindow()
	elif isContain(query, ['mini']):
		w.minimizeWindow()
	elif isContain(query, ['maxi']):
		w.maximizeWindow()
	elif isContain(query, ['move', 'slide']):
		w.moveWindow(query)
	elif isContain(query, ['switch']):
		w.switchWindow()
	elif isContain(query, ['screenshot']):
		w.takeScreenShot()
	return

# FUNCTION: Tab Operations (New Tab, Close Tab, Switch Tab) =================================================
class TabOpt:
	def __init__(self):
		self.keyboard = Controller()

	def newTab(self):
		self.keyboard.press(Key.ctrl)
		self.keyboard.press('n')
		self.keyboard.release('n')
		self.keyboard.release(Key.ctrl)

	def closeTab(self):
		self.keyboard.press(Key.ctrl)
		self.keyboard.press('w')
		self.keyboard.release('w')
		self.keyboard.release(Key.ctrl)

	def switchTab(self):
		self.keyboard.press(Key.ctrl)
		self.keyboard.press(Key.tab)
		self.keyboard.release(Key.tab)
		self.keyboard.release(Key.ctrl)

	def switchPrevTab(self):
		self.keyboard.press(Key.ctrl)
		self.keyboard.press(Key.shift)
		self.keyboard.press(Key.tab)
		self.keyboard.release(Key.tab)
		self.keyboard.release(Key.shift)
		self.keyboard.release(Key.ctrl)

	def reopenTab(self):
		self.keyboard.press(Key.ctrl)
		self.keyboard.press(Key.shift)
		self.keyboard.press('t')
		self.keyboard.release('t')
		self.keyboard.release(Key.shift)
		self.keyboard.release(Key.ctrl)

def tabOpt(query):
	t = TabOpt()
	if isContain(query, ['new', 'open', 'another', 'create']):
		t.newTab()
	elif isContain(query, ['close', 'delete']):
		t.closeTab()
	elif isContain(query, ['switch', 'move', 'another', 'next', 'which']):
		t.switchTab()
	elif isContain(query, ['previous']):
		t.switchPrevTab()
	elif isContain(query, ['previous', 'tab']) and 'reopen' in query:
		t.switchPrevTab()
	else:
		return

# FUNCTION: Write and Save ==============================================================
class SystemTasks:
	def __init__(self):
		self.keyboard = Controller()

	def write(self, text):
		text = text[5:] + " "
		for char in text:
			self.keyboard.type(char)
			time.sleep(0.02)

	def select(self):
		self.keyboard.press(Key.ctrl)
		self.keyboard.press('a')
		self.keyboard.release('a')
		self.keyboard.release(Key.ctrl)

	def hitEnter(self):
		self.keyboard.press(Key.enter)
		self.keyboard.release(Key.enter)

	def delete(self):
		self.keyboard.press(Key.backspace)
		self.keyboard.release(Key.enter)

	def save(self, text):
		if "don't" in text:
			self.keyboard.press(Key.right)
		else:
			self.keyboard.press(Key.ctrl)
			self.keyboard.press('s')
			self.keyboard.release('s')
			self.keyboard.release(Key.ctrl)
		self.hitEnter()

def systemOpt(query):
	s = SystemTasks()
	if 'delete' in query:
		s.delete()
	elif 'save' in query:
		s.save(query)
	elif 'type' in query:
		s.write(query)
	elif 'select' in query:
		s.select()
	elif 'enter' in query:
		s.hitEnter()



# FUNCTION: Access System application & Websites ==============================================================
class AccessApp:
	def __init__(self):
		self.keyboard = Controller()

	def openApp(self, appName):
		program = ['notepad', 'mspaint', 'write', 'calc', 'control', 'cmd', 'SnippingTool']
		appName = appName.replace('paint', 'mspaint')
		appName = appName.replace('wordpad', 'write')
		appName = appName.replace('word', 'write')
		appName = appName.replace('calculator', 'calc')
		appName = appName.replace('control panel', 'control')
		appName = appName.replace('command prompt', 'cmd')
		appName = appName.replace('snipping tool', 'SnippingTool')
		try:
			print(appName[5:])
			if appName[5:] not in program:
				return False
			print("Entered")
			subprocess.Popen('C:\\Windows\\System32\\' + appName[5:] + '.exe')
		except:
			pass

	def open_website(self, query):
		data = json.load(open('otherfiles/websites.json', encoding='utf-8'))
		query = query.replace('open', '')
		if query in data:
			response = data[query]
		else:
			query = get_close_matches(query, data.keys(), n=2, cutoff=0.5)
			if len(query) == 0: return False
			response = choice(data[query[0]])

		webbrowser.open(response)

def accessApp(query):
	s = AccessApp()
	if isContain(query, ['notepad', 'paint', 'calc', 'word', 'control panel', 'command prompt', 'snipping tool']):
		return s.openApp(query)
	else:
		return s.open_website(query)



