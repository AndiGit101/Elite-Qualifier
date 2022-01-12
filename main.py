import random
import os 
from random import randint 
import time
import sys
import os
from pynput.keyboard import Key as key
from pynput.keyboard import Controller as control
import math


'''
Simple chat program with Bits, a simple chatbot made in python named Bits for casual user
interaction.
Project created for Code2College Elite101 class and internship/interview preperation
'''

bot = "Bits"

#helper method to make the typing effect in the console, similar to how someone types.
def typing_effect(text):

	for chars in text:

		sys.stdout.write(chars)
		sys.stdout.flush()
		time.sleep(0.04)

	time.sleep(0.6)
	os.system("clear")	

	

#Generate a random response when the user inputs a subject to talk about
def generate_response(thing):
		res = [f"I like that" , f"{thing} it is!" , "For sure!!"]


		return random.choice(res)






#stored phrases for the bot to say accordingly
greet =['Hey!' , 'Aloha' , 'Hello', 'Greetings' , 'Whats going on?']

#jokes
jokes = ["Can you jump? I'm kidding, I know you can since your a human." , "Are you a mouse? No that cant be, your talking to me" , "Im scary. No, trust me, I am friendly. Just want to let you know. Dont feel bad" , "I am a hacker.Noo. Just playing with you.Sorry I kinda scared you there.."]

#bot topics to-do
subject =['PROFILE' , 'JOKES', 'MOTIVATIONAL QUOTES' ]

#jokes with bot responses
jokes_with_answers = {"Why did the golfer bring two pairs of pants?": "In case he got a hole in one." , "My friends bakery burnt down yesterday": "Now his business is toast." , "Why did it take so long for the pirates to learn the Alphabet?": "They got stuck at C." , "Parallel lines have so much in common": "It’s a shame they’ll never meet", "Why was the picture sent to jail?": "It was framed LOL." }

#motivational quotes
motivation = ['“All our dreams can come true, if we have the courage to pursue them.” – Walt Disney', '“The secret of getting ahead is getting started.” – Mark Twain' , '“It’s hard to beat a person who never gives up.” – Babe Ruth' , '“We need to accept that we won’t always make the right decisions, that we’ll screw up royally sometimes – understanding that failure is not the opposite of success, it’s part of success.” – Arianna Huffington' , '“Whatever you are, be a good one.” ― Abraham Lincoln' , '“Smart people learn from everything and everyone, average people from their experiences, stupid people already have all the answers.” – Socrates']


##########################################################################################
#################################  MAIN BOT CHAT  ########################################
##########################################################################################
def bot_chat():
	

	#base texting
	user_input = ''
	start = bot + ":" + random.choice(greet) +  ", welcome to Bits chat service. My name is Bits, and I am a chatbot made in python!\n"
	start2 = bot + ":I am not powered by artificial intelligence, but I can still talk and act like human.\n"
	start3 = bot + ":Before we can chat, I want to get to know more about you!\n"
	start4 = bot + ":Whats your name?\n"

	#Introduction, greeting
	typing_effect(start)
	time.sleep(1)
	typing_effect(start2)
	time.sleep(1)
	typing_effect(start3)
	time.sleep(1)
	typing_effect(start4)
	time.sleep(1)

	
	
	#Ask the user for more input, then use that in your response
	name= input()

	typing_effect(bot + f":Hello {name}, nice to meet you. I am Bits, as I mentioned before haha! That is a very unique name you have there.")	
	typing_effect(bot + f":How old are you {user_input} ? Im curios.If you dont mind")
	typing_effect(bot + ":If you dont want to tell me. You can say 'I prefer not to say' or 'I dont want to say' etc..")	
	user_input = input()
	age = user_input
			
	#Check and process users age input
	if 'not' in user_input or 'dont' in user_input:

		typing_effect(bot + ":Ohh its ok then. I wont do anything with it dont worry. Im just a chatbot.")
		typing_effect(bot + ":Just wondering...")
	else:

		if int(age) > 30 and int(age) < 110:

					typing_effect(bot + "Dang.Your getting pretty old.Life goes fast.By the way...")

		elif int(age) <=29 and int(age) > 8:

					typing_effect(bot + f"Nice. Your getting started. I really dont have an age, but whoever created me can easily tell you. By the way...")

		else:

			typing_effect(bot + "Wow, your young.That's good.")


	
		##Jokes stored in a list are said by the bot and then asks user what to do##
		typing_effect(bot + ":" +random.choice(jokes))	
		typing_effect(bot + "Anyways lol..")	
		typing_effect(bot + f"What do you want me to do for you?")

		print("--Subject I can talk about--\n-Jokes-\n-Profile-\nMotivational Quotes")
		choice = input()




		#If the user does not type in a provided option of what the bot gave, then say that is not an option
		#Continue asking until a valid input is inputted
		while not subject.__contains__(choice.upper()):

			typing_effect(bot + ":Sorry, I cant do that.")
			choice = input()
			print("--Subject I can talk about--\n-Jokes-\n-Profile-\nMotivational Quotes")
			

		typing_effect(generate_response(user_input))


		'''
		Options that the bot has for the user to do
		*Make Jokes
		*Give motivational quotes
		*Build a user profile
		'''
		if choice.upper() == 'JOKES':

				typing_effect(bot + ':Want to hear a cool joke?')
				typing_effect(bot + ':Get ready.....')

				current_joke = random.choice(list(jokes_with_answers))
				typing_effect(bot +  ":" +current_joke)
				typing_effect(bot + ":" +jokes_with_answers.get(current_joke))

				typing_effect(bot + ":Oh. oh, here is another one ")
				time.sleep(0.6)
				current_joke = random.choice(list(jokes_with_answers))
				typing_effect(bot + ":" + current_joke)
				time.sleep(0.6)
				typing_effect(bot + ":" + jokes_with_answers.get(current_joke))
				typing_effect(bot + "Haha. This is making me laugh. What about you? Is it funny for you?")

				user_input = input()

				if 'yes' in user_input or 'funny'in user_input or 'is' in user_input:

					typing_effect(bot + "I knew it would. This is what it is all about")
				elif 'no' in user_input or 'not' in user_input in user_input:

					typing_effect(bot + "Aww. Let me give you one more and see if it will make you laugh!!")

					#get a random joke
					current_joke = random.choice(list(jokes_with_answers))

					typing_effect(bot + ":" + current_joke)
					typing_effect(bot + ":" +jokes_with_answers.get(current_joke))


				else:

					typing_effect(bot + "I guess that may be a yes. LOL!")



		elif choice.upper() == 'PROFILE':

				##Build a user profile##
				typing_effect(bot + ':Well. It seems you want me to make a profile of yourself')
				typing_effect(bot + ":Luckily, I already know some more things about you, but I want to get to know more.")
				typing_effect(bot + ":Lets start off with..")
				typing_effect(bot + ":--What is your favorite hobby?--")

				hobby= input()

				typing_effect(bot + ":I like that")

				typing_effect(bot + ":What is your favorite food?")

				food = input()


				typing_effect(bot + ":What is your favorite coding lanaguage?")

				code = input()

				typing_effect(bot + ":Perfect")

				typing_effect(bot + ":What is your height?(Enter in x ft x inches for")

				height = input()

				typing_effect(bot + ":Interesting")	


				typing_effect(bot + ':What is your birth symbol(Capricron, Sgittarius ..)')

				symbol = input()

				typing_effect(bot + ':Finally...')
				typing_effect(bot + ':Where was your birthplace')

				birth_place = input()

				typing_effect(bot + ":Profile is being created and formatted")


				for i in range(3):
					print(".")
					time.sleep(0.7)
					os.system("clear")	
					print("..")
					time.sleep(0.7)
					os.system("clear")	
					print("...")
					time.sleep(0.7)
					os.system("clear")	

				

				##Format user profile and inlcude age or not based on original user input##
				if not age == ' ':

					print(f"===============\n{name}'s profile\nAge: {age} years old\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n")


					typing_effect("Here is your profile.Keep it if you want")
				

					print(f"===============\n{name}'s profile\nAge: {age} years old\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n")

					print("Enter Y or N to determine if you want to save your profile")

				else:

					print(f"===============\n{name}'s profile\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n")


					typing_effect("Here is your profile.Keep it if you want")
				

					print(f"===============\n{name}'s profile\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n")

					print("Enter Y or N to determine if you want to save your profile")



				yes_no = input()


				if yes_no == 'Y':

					typing_effect(bot + ":Take care of it. It was my pleasure :)")

				elif yes_no == 'N':

					typing_effect(bot + ":I'll keep it.")

				time.sleep(1)		

		elif choice.upper() == 'MOTIVATIONAL QUOTES':

				typing_effect(bot + ":Here is a motivational quote to start up your day!")
				typing_effect(bot + random.choice(list(motivation)) + "\n\nSomething powerful")
				time.sleep(1.3)



		##Ending##
		typing_effect(bot + ":Ahh I really wanted to keep chatting but the time has come to go for me to go. ")
		typing_effect(bot + ':It has been a pleasure to talk with a human really interesting and cool.')
		typing_effect(bot + ':Maybe next time you can find me to chat again anytime. Im here for any service.')
		typing_effect(bot + ":Goodbye!!")
			

		typing_effect()

################################################################################################################
#################################  MAIN METHOD TO RUN THE WHOLE SCRIPT  ########################################
################################################################################################################
if __name__ == "__main__":
	bot_chat()
