import random

scripts={
    "introduction":"Your points are counted against your score as morality points, You will be given the results at the end. Pick your choices wisely",
    "encounter1intro":" Day 1 \n Your wake in a lounge chair inside a white corridor you look to your left then right and spot a man in formal scrubs by a desk, you panic for you can not seem to spot your daughter",
    "encounter1pt1":"gets out of the chair and stands which allows to look over the desk and see her at the vending machine,  she was struggling to put a dollar you gave her in the machine you walked and help her the doctor you saw earlier taps your shoulder and starts to talk about your wife's condition. Your face drops you look to your wife's death bed through the window and all you can think about is how am i going to tell Sara"
}

gameState={
    "score":0,
    "difficulty":0,
    "playerName":"null",
    "moralCompass":0
}

def ask_for_name():
    Player1 = (input("What do you desire to name yourself :\n"))
    return Player1

def start_button():
    startbutton = (input("Welcome to my suivival horror game set in the post apocaliptic world where the sun is dying and your only hope for you and your daughter Sara is to make it too the last Spacecruiser set to leave \n press 1 to start\n"))
    if startbutton== "1":
        return True
    else:
        start_button()

def pick_difficulty():
    Difficulty = input (" To choose difficulty input a number \n Easy: 1 \n Hard: 2 \n Very Hard: 3 \n ")
    return Difficulty


def encounter2():
    pass

def part3_1_encounter1():
    print ("You are make your way through the crowd and once you make it too your car you realise you dont have your keys and deduce that you lost it in the panic you see a old lady struggling to open her car, you wont be able to make it on foot becuase it is a few days away. You know what you have to do but you don't know if you have the strength to do it")
    userOption = input("Pick a action by giving a number \n Option 1 : steal the old ladies car \n Option 2 : decide to walk \n ")
    if userOption== "1":
        print(" ")
        print (" You see an opptunity and take you do have a daughter to look after. After you snatch the keys out the hands of the old women you put Sara in the car and drive but the car break down so you take the rest on foot.")
        print(" ")
        gameState["moralCompass"]+=1
        #add 1 to the moral Compass
        encounter2()
    elif userOption=="2":
        print(" ")
        print (" You put Sara on your back and start walking about 5 miles in you see an abandoned bus with food, which stops her from complaining about the hunger you look in the ignition and see somebody left the keys. You thank God and make your way home.")
        encounter2()
    else:
        print("invalid input")
        part3_1_encounter1()

def part3_2_encounter1():
    print (" You run to the exit luckly no one is around you make your way to the car and see an old women struggling to open her car you put Sara in the car and think weather to help her")
    userOption = input("Pick a action by giving a number \n Option 1 : Help the old lady  \n Option 2 : Just go and leave her, you have your own problems \n ")

    if userOption== "1":
        print(" ")
        print (" You help the old lady and she thanks you by giving Sara her neckless saying that it was her mothers and she has no kids so its better off with her .")
        print(" ")
        encounter2()
    elif userOption== "2":
        print(" ")
        print (" You drive off and see her being mugged.")
        print (" ")
        gameState["moralCompass"]+=1
        encounter2()
    else:
        print("invalid input")
        part3_2_encounter1()

    pass
    

def part2_encounter1():
    print (" you take a minute to gather your senses and in the shock i dont realise the atmospheric change in the room the TV gets louder and i can see its the news reporters in viable distress the headline reads * The Sun is dying Evacuate to your nearest spacecruiser, You have 5days * you look agian in disbelief.  You grab saras hand and take a quick picture of the nearest one shown on screen.")
    userOption = input("Pick a action by giving a number \n Option 1 : Run for the nearest exit while carrying your daughter\n Option 2 : calmly leave the room while holding her hand  \n Option 3 : Stay and watch the Tv \n ")
    if userOption == ("1"):
        print(" ")
        print ("While running to the exit people spot you and part to panic for the exit your keys fall out your pocket you decide to leave them and run. You enter the ahllway and its full of people ")
        print(" ")
        part3_1_encounter1()
    elif userOption== ("2"):
        print(" ")
        print (" You quickly but calmly leave the room succfully and are able too reach the hallway")
        print(" ")
        part3_2_encounter1()
    elif userOption == ("3"):
        print(" ")
        print (" You carry on watching the news report and see that Sara is gone you check the shes crying next to her mother, seeing sara like that makes you loes all your hope in life. \n GAME OVER ")
        print(" ")
    else:
        print("invalid input")
        part2_encounter1()
 
def encounter1():
    print (scripts["encounter1intro"]) #part1
    userOption = input("Pick a action by giving a number \n Option 1 : get out of chair \n Option 2 : Look around somemore \n Option 3 : Go back too sleep \n ")
    
    if userOption== "1":
        print(" ")
        
        print (str(gameState["playerName"])+" "+ scripts["encounter1pt1"])
        
        part2_encounter1()
        
        print("")

    elif userOption== "2":
        pass
    elif userOption== "3":
        pass
    else:
        print("invalid input")
        encounter1()

#function is used to begin the introduction and take the difficulty the user wants
def intro_one():
    print (scripts["introduction"])
    difficulty= pick_difficulty()
    gameState['difficulty']=difficulty
    encounter1()

#preparts the start of the game by waiting for a OK signal aka 1 and the users name if no name is provided the game cannot begin
def start_game():
    if start_button():
        pass
    
    Player1= ask_for_name()

    if len(Player1)<=0:
        start_game()
    else:
        gameState['playerName']=Player1
        intro_one()
        


#runs the game
start_game()