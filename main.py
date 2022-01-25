'''
Simple chat program with Bits, a simple chatbot made in python named Bits for casual user
interaction.
Project created for Code2College Elite101 class and internship/interview preperation.
'''
##Library and Modeles used for the chatbot project
import random
import os
import time
import sys

bot = "Bits"

#Every bot input and user input(Key:Bot , Value:User)
each_chat_history = {"Bot": [], "User": []}

#Overall chat history
overall_chat_history = list()


#Add each respective chats to the history of both the bot and the user individually
def add_chat(chat):

    if chat[0:4] == 'Bits':
        each_chat_history["Bot"].append(chat)

    else:
        each_chat_history["User"].append(chat)


#Add overall chat in order
def add_overall(chat):

    overall_chat_history.append(chat)


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
    res = [f"I like that", f"{thing} it is!", "For sure!!"]
    return random.choice(res)


#stored phrases for the bot to say accordingly
greet = ['Hey!', 'Aloha', 'Hello', 'Greetings', 'Whats going on?']

#jokes
jokes = [
    "Can you jump? I'm kidding, I know you can since your a human.",
    "Are you a mouse? No that cant be, your talking to me",
    "Im scary. No, trust me, I am friendly. Just want to let you know. Dont feel bad",
    "I am a hacker.Noo. Just playing with you.Sorry I kinda scared you there.."
]

#bot topics to-do
subject = ['PROFILE', 'JOKES', 'MOTIVATIONAL QUOTES']

#jokes with bot responses
jokes_with_answers = {
    "Why did the golfer bring two pairs of pants?":
    "In case he got a hole in one.",
    "My friends bakery burnt down yesterday": "Now his business is toast.",
    "Why did it take so long for the pirates to learn the Alphabet?":
    "They got stuck at C.",
    "Parallel lines have so much in common": "It’s a shame they’ll never meet",
    "Why was the picture sent to jail?": "It was framed LOL."
}

#motivational quotes
motivation = [
    '“All our dreams can come true, if we have the courage to pursue them.” – Walt Disney',
    '“The secret of getting ahead is getting started.” – Mark Twain',
    '“It’s hard to beat a person who never gives up.” – Babe Ruth',
    '“We need to accept that we won’t always make the right decisions, that we’ll screw up royally sometimes – understanding that failure is not the opposite of success, it’s part of success.” – Arianna Huffington',
    '“Whatever you are, be a good one.” ― Abraham Lincoln',
    '“Smart people learn from everything and everyone, average people from their experiences, stupid people already have all the answers.” – Socrates'
]


##########################################################################################
#################################  MAIN BOT CHAT  ########################################
##########################################################################################
def bot_chat():

    #greeting dialogue by the bot
    start = bot + ":" + random.choice(
        greet
    ) + ", welcome to Bits chat service. My name is Bits, and I am a chatbot made in python!\n"
    start2 = bot + ":I am not powered by artificial intelligence, but I can still talk and act like human.\n"
    start3 = bot + ":Before we can chat, I want to get to know more about you!\n"
    start4 = bot + ":Whats your name?\n"

    #Introduction, greeting
    typing_effect(start)
    add_chat(start)
    add_overall(start)
    time.sleep(1)
    typing_effect(start2)
    add_chat(start2)
    add_overall(start2)
    time.sleep(1)
    typing_effect(start3)
    add_chat(start3)
    add_overall(start3)
    time.sleep(1)
    typing_effect(start4)
    add_chat(start4)
    add_overall(start4)
    time.sleep(1)

    #Ask the user for more input, then use that in your response
    name = input()
    typing_effect(
        bot +
        f":Hello {name}, nice to meet you. I am Bits, as I mentioned before haha! That is a very unique name you have there."
    )
    add_chat(
        bot +
        f":Hello {name}, nice to meet you. I am Bits, as I mentioned before haha! That is a very unique name you have there."
    )
    add_overall(
        bot +
        f":Hello {name}, nice to meet you. I am Bits, as I mentioned before haha! That is a very unique name you have there."
    )

    typing_effect(bot +
                  f":How old are you {name} ? Im curios.If you dont mind")
    add_chat(bot + f":How old are you {name} ? Im curios. If you dont mind")
    add_overall(bot + f":How old are you {name} ? Im curios. If you dont mind")

    typing_effect(
        bot +
        ":If you dont want to tell me. You can say 'I prefer not to say' or 'I dont want to say' etc.."
    )
    add_chat(
        bot +
        ":If you dont want to tell me. You can say 'I prefer not to say' or 'I dont want to say' etc.."
    )
    add_overall(
        bot +
        ":If you dont want to tell me. You can say 'I prefer not to say' or 'I dont want to say' etc.."
    )

    user_input = input()
    age = user_input
    add_chat("You: " + str(age))
    add_overall("You: " + str(age))

    #Check and process users age input
    if 'not' in user_input or 'dont' in user_input:

        typing_effect(
            bot +
            ":Ohh its ok then. I wont do anything with it dont worry. Im just a chatbot."
        )
        add_chat(
            bot +
            ":Ohh its ok then. I wont do anything with it dont worry. Im just a chatbot."
        )
        add_overall(
            bot +
            ":Ohh its ok then. I wont do anything with it dont worry. Im just a chatbot."
        )

        typing_effect(bot + ":Just wondering...")
        add_chat(bot + ":Just wondering...")
        add_overall(bot + ":Just wondering...")

    else:

        if int(age) > 30 and int(age) < 110:

            typing_effect(
                bot +
                ": Dang.Your getting pretty old.Life goes fast.By the way...")
            add_chat(
                bot +
                ": Dang.Your getting pretty old.Life goes fast.By the way...")
            add_overall(
                bot +
                ": Dang.Your getting pretty old.Life goes fast.By the way...")

        elif int(age) <= 29 and int(age) > 8:

            typing_effect(
                bot +
                f": Nice. Your getting started. I really dont have an age, but whoever created me can easily tell you. By the way..."
            )
            add_chat(
                bot +
                f": Nice. Your getting started. I really dont have an age, but whoever created me can easily tell you. By the way..."
            )
            add_overall(
                bot +
                f": Nice. Your getting started. I really dont have an age, but whoever created me can easily tell you. By the way..."
            )

        else:

             typing_effect(bot + ": Wow, your young.That's good.")
             add_chat(bot + ": Wow, your young.That's good.")
             add_overall(bot + ": Wow, your young.That's good.")

        ##Jokes stored in a list are said by the bot and then asks user what to do##
        typing_effect(bot + ":" + random.choice(jokes))
        add_chat(bot + ":" + random.choice(jokes))
        add_overall(bot + ":" + random.choice(jokes))
        typing_effect(bot + ": Anyways lol..")
        add_chat(bot + ": Wow, your young.That's good.")
        add_overall(bot + ": Wow, your young.That's good.")
        typing_effect(bot + f": What do you want me to do for you?")
        add_chat(bot + ": Wow, your young.That's good.")
        add_overall(bot + ": Wow, your young.That's good.")

        print(
            "--Subject I can talk about--\n-Jokes-\n-Profile-\nMotivational Quotes"
        )

        choice = input()
        add_chat("You :" + choice)
        add_overall("You :" + choice)

        #If the user does not type in a provided option of what the bot gave, then say that is not an option
        #Continue asking until a valid input is inputted
        while not subject.__contains__(choice.upper()):

            typing_effect(bot + ":Sorry, I cant do that.")
            print("--Subject I can talk about--\n-Jokes-\n-Profile-\nMotivational Quotes")

            choice = input()
            add_chat("You :" + choice)
            add_overall("You :" + choice)

        typing_effect(generate_response(user_input))
        add_chat(generate_response(user_input))
        add_overall(generate_response(user_input))

        #Bot options for what the user can do

		#Get a joke from the list o jokes and randomize and ouput respective answers to the user.
        if choice.upper() == 'JOKES':

            typing_effect(bot + ':Want to hear a cool joke?')
            add_chat(bot + ':Want to hear a cool joke?')
            add_overall(bot + ':Want to hear a cool joke?')
            typing_effect(bot + ':Get ready.....')
            add_chat(bot + ':Get ready.....')
            add_overall(bot + ':Get ready.....')

            current_joke = random.choice(list(jokes_with_answers))
            typing_effect(bot + ":" + current_joke)
            add_chat(bot + ":" + current_joke)
            add_overall(bot + ":" + current_joke)

            typing_effect(bot + ":" + jokes_with_answers.get(current_joke))
            add_chat(bot + ":" + jokes_with_answers.get(current_joke))
            add_overall(bot + ":" + jokes_with_answers.get(current_joke))

            typing_effect(bot + ":Oh. oh, here is another one..")
            add_chat(bot + ":Oh. oh, here is another one..")
            add_overall(bot + ":Oh. oh, here is another one..")

            time.sleep(0.6)

            current_joke = random.choice(list(jokes_with_answers))
            typing_effect(bot + ":" + current_joke)
            add_chat(bot + ":" + current_joke)
            add_overall(bot + ":" + current_joke)

            time.sleep(0.6)
            typing_effect(bot + ":" + jokes_with_answers.get(current_joke))
            add_chat(bot + ":" + jokes_with_answers.get(current_joke))
            add_overall(bot + ":" + jokes_with_answers.get(current_joke))

            typing_effect(
                bot +
                ": Haha. This is making me laugh. What about you? Is it funny for you?"
            )
            add_chat(
                bot +
                ": Haha. This is making me laugh. What about you? Is it funny for you?"
            )
            add_overall(
                bot +
                ": Haha. This is making me laugh. What about you? Is it funny for you?"
            )

            user_input = input()
            add_chat("You :" + user_input)
            add_overall("You :" + user_input)

            #Capitalize and check for case sensetivity in the user input
         

            if user_input.upper() == 'YES':

                typing_effect(bot +
                              "I knew it would. This is what it is all about")
                add_chat(bot + "I knew it would. This is what it is all about")
                add_overall(bot +
                            "I knew it would. This is what it is all about")

            elif 'no' in user_input or 'not' in user_input in user_input:

                typing_effect(
                    bot +
                    "Aww. Let me give you one more and see if it will make you laugh!!"
                )
                add_chat(
                    bot +
                    "Aww. Let me give you one more and see if it will make you laugh!!"
                )
                add_overall(
                    bot +
                    "Aww. Let me give you one more and see if it will make you laugh!!"
                )

                #get a random joke
                current_joke = random.choice(list(jokes_with_answers))

                typing_effect(bot + ":" + current_joke)
                add_chat(bot + ":" + current_joke)
                add_overall(bot + ":" + current_joke)
                typing_effect(bot + ":" + jokes_with_answers.get(current_joke))
                add_chat(bot + ":" + jokes_with_answers.get(current_joke))
                add_overall(bot + ":" + jokes_with_answers.get(current_joke))

            else:

                typing_effect(bot + ": I guess that may be a yes. LOL!")
                add_chat(bot + ": I guess that may be a yes. LOL!")
                add_overall(bot + ": I guess that may be a yes. LOL!")

        elif choice.upper() == 'PROFILE':

            ##Build a user profile##
            typing_effect(
                bot +
                ':Well. It seems you want me to make a profile of yourself')
            add_chat(
                bot +
                ':Well. It seems you want me to make a profile of yourself')
            add_overall(
                bot +
                ':Well. It seems you want me to make a profile of yourself')

            typing_effect(
                bot +
                ":Luckily, I already know some more things about you, but I want to get to know more."
            )
            add_chat(
                bot +
                ":Luckily, I already know some more things about you, but I want to get to know more."
            )
            add_overall(
                bot +
                ":Luckily, I already know some more things about you, but I want to get to know more."
            )

            typing_effect(bot + ":Lets start off with..")
            add_chat(bot + ":Lets start off with..")
            add_overall(bot + ":Lets start off with..")
            typing_effect(bot + ":--What is your favorite hobby?--")
            add_chat(bot + ":--What is your favorite hobby?--")
            add_overall(bot + ":--What is your favorite hobby?--")

            hobby = input()
            add_chat("You :" + hobby)
            add_overall("You :" + hobby)

            typing_effect(bot + ":I like that")
            add_chat(bot + ":I like that")
            add_overall(bot + ":I like that")

            typing_effect(bot + ":What is your favorite food?")
            add_chat(bot + ":What is your favorite food?")
            add_overall(bot + ":What is your favorite food?")

            food = input()
            add_chat("You :" + food)
            add_overall("You :" + food)

            typing_effect(bot + ":What is your favorite coding lanaguage?")
            add_chat(bot + ":What is your favorite coding lanaguage?")
            add_overall(bot + ":What is your favorite coding lanaguage?")

            code = input()
            add_chat("You :" + code)
            add_overall("You :" + code)

            typing_effect(bot + ":Perfect")
            add_chat(bot + ":Perfect")
            add_overall(bot + ":Perfect")

            typing_effect(bot +
                          ":What is your height?(Enter in x ft x inches for")
            add_chat(bot + ":What is your height?(Enter in x ft x inches for")
            add_overall(bot +
                        ":What is your height?(Enter in x ft x inches for")

            height = input()
            add_chat("You :" + height)
            add_overall("You :" + height)

            typing_effect(bot + ":Interesting")
            add_chat(bot + ":Interesting")
            add_overall(bot + ":Interesting")

            typing_effect(
                bot + ':What is your birth symbol(Capricron, Sgittarius ..)')
            add_chat(bot +
                     ':What is your birth symbol(Capricron, Sgittarius ..)')
            add_overall(bot +
                        ':What is your birth symbol(Capricron, Sgittarius ..)')

            symbol = input()
            add_chat("You :" + symbol)
            add_overall("You: " + symbol)

            typing_effect(bot + ':Finally...')
            add_chat(bot + ':Finally...')
            add_overall(bot + ':Finally...')

            typing_effect(bot + ':Where was your birthplace')
            add_chat(bot + ':Where was your birthplace')
            add_overall(bot + ':Where was your birthplace')

            birth_place = input()
            add_chat("You: " + birth_place)
            add_overall("You: " + birth_place)

            typing_effect(bot + ":Profile is being created and formatted")
            add_chat(bot + ":Profile is being created and formatted")
            add_overall(bot + ":Profile is being created and formatted")

            #Loading animation effect on the console
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

                print(
                    f"===============\n{name}'s profile\nAge: {age} years old\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n"
                )

                add_chat(
                    f"Profile created by the user\n===============\n{name}'s profile\nAge: {age} years old\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n"
                )

                add_overall(
                    f"Profile created by the user\n===============\n{name}'s profile\nAge: {age} years old\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n"
                )

                typing_effect("Here is your profile.Keep it if you want")

                print(
                    f"===============\n{name}'s profile\nAge: {age} years old\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n"
                )

            else:

                print(
                    f"===============\n{name}'s profile\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n"
                )

                add_chat(
                    f"Profile created by the user\n===============\n{name}'s profile\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n"
                )

                add_overall(
                    f"Profile created by the user\n===============\n{name}'s profile\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n"
                )

                typing_effect("Here is your profile.Keep it if you want")

                print(
                    f"===============\n{name}'s profile\nFavorite hobby: {hobby}\nFood:{food}\nCoding language: {code}\nHeight:{height}\nBirth symbol: {symbol}\nBirth PLace: {birth_place}\n=============\n\n"
                )

            print("Enter Y or N to determine if you want to save your profile")
            yes_no = input()
            add_chat("You: " + yes_no)
            add_overall("You: " + yes_no)

            if yes_no == 'Y':

                typing_effect(bot + ":Take care of it. It was my pleasure :)")
                add_chat(bot + ":Take care of it. It was my pleasure :)")
                add_overall(bot + ":Take care of it. It was my pleasure :)")

            elif yes_no == 'N':

                typing_effect(bot + ":I'll keep it.")
                add_chat(bot + ":I'll keep it.")
                add_overall(bot + ":I'll keep it.")

            time.sleep(1)

        elif choice.upper() == 'MOTIVATIONAL QUOTES':

            typing_effect(
                bot + ":Here is a motivational quote to start up your day!")
            add_chat(bot +
                     ":Here is a motivational quote to start up your day!")
            add_overall(bot +
                        ":Here is a motivational quote to start up your day!")

            typing_effect(bot + random.choice(list(motivation)) +
                          "\n\nSomething powerful")
            add_chat(bot + random.choice(list(motivation)) +
                     "\n\nSomething powerful")
            add_overall(bot + random.choice(list(motivation)) +
                        "\n\nSomething powerful")
            time.sleep(1.3)

    ##Ending##
    typing_effect(
            bot +
            ":Ahh I really wanted to keep chatting but the time has come to go for me to go. "
        )
    add_chat(
            bot +
            ":Ahh I really wanted to keep chatting but the time has come to go for me to go. "
        )
    add_overall(
            bot +
            ":Ahh I really wanted to keep chatting but the time has come to go for me to go. "
        )
    typing_effect(
            bot +
            ':It has been a pleasure to talk with a human really interesting and cool.'
        )
    add_chat(
            bot +
            ':It has been a pleasure to talk with a human really interesting and cool.'
        )
    add_overall(
            bot +
            ':It has been a pleasure to talk with a human really interesting and cool.'
        )
    typing_effect(
            bot +
            ':Maybe next time you can find me to chat again anytime. Im here for any service.'
        )
    add_chat(
            bot +
            ':Maybe next time you can find me to chat again anytime. Im here for any service.'
        )
    add_overall(
            bot +
            ':Maybe next time you can find me to chat again anytime. Im here for any service.'
        )
    typing_effect(bot + ":Goodbye!!")
    add_chat(bot + ":Goodbye!!")
    add_overall(bot + ":Goodbye!!")

    ##Extras for user to view history
    ##Ask to view history or no(exit)
    time.sleep(1)
    print(
            "View or search history or exit\n==Bot==\n==User==\n==General==\nSearch==\n==EXIT==Enter 1,2,3, or 4 for each option")


    option = input()
    os.system("clear")

    if option == '1':

            print('Chat for the Bot')
            time.sleep(3)
            os.system("clear")
            for i in range(len(each_chat_history['Bot'])):

                print(each_chat_history['Bot'][i] + "\n\n")

    elif option == '2':

            print(f'Chat for the User{name}')
            time.sleep(3)
            os.system("clear")
            for i in range(len(each_chat_history['User'])):

                print(each_chat_history['User'][i] + "\n\n")

    elif option == '3':

            time.sleep(1)
            
            search = input("Would you like to search for a keyword or no?: ")
            os.system('clear')

            if 'Yes' in search  or 'yes' in search:

				#SEARCH for keyword or phrase
                 keyword = input("Enter a phrase or word to search: ")

				 #search every chat instance
                 for chat in range(len(overall_chat_history)):
 
                   for i in range(len(overall_chat_history[chat])):

                       if overall_chat_history[chat][i] == "You: " + keyword:
                        overall_chat_history[chat][i] =""
                        overall_chat_history[chat][i] ="---\033[1m" + keyword + "\033[0m---"

						

                
                 for i in range(len(overall_chat_history)):
                        print(overall_chat_history[i] + "\n")
               

					
	
################################################################################################################
#################################  MAIN METHOD TO RUN THE WHOLE SCRIPT  ########################################
################################################################################################################
if __name__ == "__main__":
    bot_chat()
