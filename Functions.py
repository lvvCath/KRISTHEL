import datetime
from googletrans import Translator, LANGUAGES
import requests
import random
from bs4 import BeautifulSoup

def isContain(text, lst):
	for word in lst:
		if word in text:
			return True
	return False

# FUNCTION: Greet ==============================================================
class DateTime:
	def currentTime(self):
		time = datetime.datetime.now()
		x = " A.M."
		if time.hour>12: x = " P.M."
		time = str(time)
		time = time[11:16] + x
		return time

	def currentDate(self):
		now = datetime.datetime.now()
		day = now.strftime('%A')
		date = str(now)[8:10]
		month = now.strftime('%B')
		year = str(now.year)
		result = f'{day}, {date} {month}, {year}'
		return result

def greet():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		greet = "Good Morning! "
	elif hour >= 12 and hour < 18:
		greet = "Good Afternoon! "
	else:
		greet = "Good Evening! "
	return greet

def chat(text):
	dt = DateTime()
	output = ""
	if isContain(text, ['good']):
		output = greet()
	elif isContain(text, ['time']):
		output = "Current Time is: " + dt.currentTime()
	elif isContain(text, ['date', 'today', 'day', 'month']):
		output = "Current Date is: " + dt.currentDate()
	return output


# FUNCTION: Translator ==============================================================
def lang_translate(text, language):
	print("Text>>", text)
	print("Text>>", language)
	if language in LANGUAGES.values():
		translator = Translator()
		output = translator.translate(text, src='en', dest=language)
		return output
	else:
		return "None"

# DICTIONARY =========================================================================
def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] # 'css-1gyuw4i eh475bn0' for less relevant synonyms

# TOSS A COIN / ROLL A DICE ==========================================================
def generate(query):
	if isContain(query, ['dice', 'die']) and isContain(query, ['roll', 'throw']):
		result = "You got " + str(random.randint(1, 6))
		return result
	elif isContain(query, ['coin']) and isContain(query, ['flip', 'toss']):
		p = random.randint(-10, 10)
		if p > 0:
			return "You got Head"
		else:
			return "You got Tail"
	else:
		print("Not Available")
	return
