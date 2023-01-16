KRISTHEL AI VIRTUAL ASSISTANT
	= Desktop AI virtual assistant
	= Compatible in windows

FUNCTIONS:
	• AI Virtual Assistant name
		○ Keywords (word/s that should be found in the command): 
			= 'what\'s your name' OR 'what is your name' OR 'who are you' OR 'what are you'
		○ Sample Commands:
			= "What is your name?"
			= "Who are you?"

	• Greets back Good afternoon/morning/noon 
		○ Keywords: 
			= ('morning' OR 'evening' OR  'noon') AND 'good'
		○ Sample Commands:
			= "Good <afternoon/morning/noon>"

	• Current Date/Time
		○ Keywords: 'date' OR 'time'
		○ Sample Command:
			= "What is the current time?"
			= "What is the current date?"

	• Plays Youtube Video
		○ Keyword: 'play'
		○ Sample Command:
			= "Play <anything that can be search in youtube>"
		○ Note: will sleep after performing the command
			= Press mic to perform a new command

	• Search in Google
		○ Keyword: 'Google'
		○ Sample Command:
			= "search latest news in google"
			= "search technological institute of the Philippines in google"
		○ Note: will sleep after performing the command
			= Press mic to perform a new command

	• Dictionary (Definition of a word)
		○ Keywords: 'definition' OR 'meaning' OR 'define'
		○ Sample Command:
			= "what is the definition of science"

	• Tells a Joke
		○ Keywords: 'joke'
		○ Sample Command:
			= 'Tell me a joke'

	• Search in Wikipedia
		○ Keyword: 'wikipedia'
		○ Sample Command:
			= "search phililippines in wikipedia"

	• Translator
		○ Keyword 'translate'
		○ Sample Command:
			= User: "translate hello world"
			  Kristhel: "Which language to translate"
			  User: "french"

	• Toss a Coin and Roll a Die
		○ Keywords: 'coin' OR 'dice' OR 'die'
		○ Sample commands:
			= "Roll a die"
			= "Toss a coin"
			= "Flip a coin"
			= "throw a dice"

	• Basic Calculator
	   Basic Operations: +, -, /, *
	   Bitwise Operations: and, or, not, exclusive or, complement, right & left shift
	   Conversion: decimal to bin/hex/oct
	   Trigonometry: sin, cos, tan
	   factorial
		○ Keyword: 'calculate', 'compute'
		○ Sample Command: 
			= "<calculate/compute> 3 + 5"
			= "compute (not/complement of) 12"
			= "compute 25 <and/or> 12"
			= "compute <right/left> shift 37"
			= "compute <hexadecimal/octal/binary> 12"
			= "calculate cos 30"
			= "calculate factorial of 45"

	• Open Websites (see website.json file for the list of websites)
		○ Keyword: 'open'
		○ Sample Command: "Open <website>"
		○ Note: will sleep after performing the command
			= Press mic to perform a new command

	• Open Built-in System Program: notepad, mspaint, write, calc, control, cmd, SnippingTool
		○ Keyword:
			= 'open' AND ('notepad' OR 'paint' OR 'calc' OR 'word' OR 'control panel' OR 'command prompt' OR 'snipping tool')
		○ Sample Command: "Open <program>"
		○ Note: will sleep after performing the command
			= Press mic to perform a new command

	• Screenshot
		○ Keyword: 'screenshot'
		○ Sample Command: "Take a screenshot"
		○ Note: will sleep after performing the command
			= Press mic to perform a new command

	• Control Window: open, close, move, minimize/maximize
		○ Keyword: 'window'
		○ Sample commands:
			= "Close that"
			= "Move window to the <right/left/up/down>"
			= "Maximize window"
			= "Minimize window"
			= "Switch window"

	• Control Tab: new, minimize/maximize, move, switch(prev/next), reopen tab
		○ Keyword: tab'
			= "Open new Tab"
			= "Close tab"
			= "Switch Tab"
			= "Previous tab"
			= "Reopen tab"

	• Create File: type, select, save, delete, press enter
		○ Keywords: 'type' OR 'save' OR 'delete' OR 'select' OR 'press enter'
		○ Sample commands:
			= "Open notepad"
			  "type hello world"
			  "save file"
				□ "press enter" (to save the file)
				□ "close window" (cancel saving)
			= Closing notepad without saving
				□ "Close window"
				  "don’t save"
	
NOTE: see main() function to learn more about the details on what certain words should be best used to perform a successful command.
