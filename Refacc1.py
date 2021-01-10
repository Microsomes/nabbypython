import random

scripts={
    "introduction":"Your points are counted against your score as morality points, You will be given the results at the end. Pick your choices wisely",
    "encounter1intro":" Day 1 \n Your wake in a lounge chair inside a white corridor you look to your left then right and spot a man in formal scrubs by a desk, you panic for you can not seem to spot your daughter",
    "encounter1pt1":"gets out of the chair and stands which allows to look over the desk and see her at the vending machine,  she was struggling to put a dollar you gave her in the machine you walked and help her the doctor you saw earlier taps your shoulder and starts to talk about your wife's condition. Your face drops you look to your wife's death bed through the window and all you can think about is how am i going to tell Sara",
}

gameState={
    "score":0,
    "difficulty":0,
    "playerName":"null",
    "moralCompass":0,
    "inventory":[]
}

def findInventoryItem(item):
    for n in gameState["inventory"]:
        if n==item:
            return True
    return False

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





def encounter3_part1_02():
    print (" You walk down the path for days and it you finnaly see road throught the bushes, the compound is in sight.")
    
    pass


def encounter3_part1():
    print (" You think about the best way to cross the swamp, you have two options. Cross the swamp in the car so you dont have to leave behind any resources or cross on foot")
    userOption = input(" Pick a action by giving a number \n Option 1 : Drive through the swamp   \n Option 2 : Walk through the swamp with sara on your back \n ")

    if userOption == "1":
        print(" ")
        print (" You start to drive through the swamp and start to sink, you quickly make a move and unbuckle your and Saras belt. You scale the side of the car with her and make a jump for the safety of solid ground")
        print(" ")
        if findInventoryItem("victual"):
            gameState["inventory"].remove("victual")

        if findInventoryItem("Picture"):
            gameState["inventory"].remove("Picture")

        if findInventoryItem("Gun"):
            gameState["inventory"].remove("Gun")

        if findInventoryItem("Map"):
            gameState["inventory"].remove("Map")
        
        encounter3_part1_02()
    elif userOption == "2":
        print(" ")
        if gameState["inventory"][0]=="Gun":
            print (" You start fill your backpack with the rest of Saras clothes and put the pistol in your jackets zip pocket. You then put Sara on your back and continue to walk, you feel yourself sinking deeper and deeper so you keep moving through the swamp untill it reaches your neck but just as soon as the mud starts to fill your mouth you start slowly raise up higher and higher untill the dirt path is in sight. You finnally make it but your covered in mud ")
            encounter3_part1_02()

        if gameState["inventory"][0]=="map":
            print (" You start fill your backpack with the rest of Saras clothes and put the pistol in your jackets zip pocket. You then put Sara on your back and continue to walk, you feel yourself sinking deeper and deeper so you keep moving through the swamp untill it reaches your neck but just as soon as the mud starts to fill your mouth you start slowly raise up higher and higher untill the dirt path is in sight. You finnally make it but your covered in mud ")
            print(" ")
            encounter3_part1_02()
    else:
        print("invalid input")
        encounter3_part1()



    pass

def encounter3_part3():
    print (" You take cover behind a abandoned vehicle but just before you can think of a plan, you get attacked from behind and as he chokes you realise you have to make a choice")
    userOption = input(" Pick a action by giving a number \n Option 1 : Bite his arm and run with Sara \n Option 2 : Reach for your Gun *IF YOU PCIKED THE GUN*\n ")

    if userOption == "1":
        print(" ")
        print ("You bite a chunk out of his arm and while his distracted you run in to buses with a terrified Sara but not before youre back pack is torn from your back in last ditch effort by the man. You are able to make your way arround the man made check point and reach a path")
        print(" ")

    pass

def encounter3():
    print (" Day 3 \n  its chaos a first but after the 2 days it calms down. You end up at traffic jam that wont move for a few days. You see a dirt path that could eithe take that or leave the vehicle, what do you choose. ")
    userOption = input(" Pick a action by giving a number \n Option 1 : Take the dirt path   \n Option 2 : Stay in traffic   \n Option 3 : continue on foot \n ")
    if userOption == "1":
        print(" ")
        print (" You drive on to the dirt path which leads you through a brush and come across a swamp between you and the rest of the path.")
        print(" ")
        encounter3_part1()
    elif userOption == "2":
        print(" ")
        if findInventoryItem("victual"):
            print (" You stay in the traffic for a few days and after driving on what was mostly pavement to go get arround all the vacant cars, the supplies you brought come in handy and when you make to the ship it is taking off you ask to let in but the gaurd says *No more passengers* you try and push through but you`re are tazed and pass out. When you wake the streets are empty and Sara is missing. All the ships left you failed. \n GAME OVER ")
        else:
            print (" You run out of supplies quickly and starve after failing to find more food. \n GAME OVER ")
        print(" ")
    elif userOption == "3":
        print(" ")
        print (" You decide to make your way on foot as it is the most reliable, you make great progress at first but then you come accross man made check point you decide to stop and decide your next decision")
        print(" ")
        encounter3_part3()
    else:
        print("invalid input")
        encounter3()

def encounter2_part3():
    print (" You go in to Saras room and see that she has packed reponsibly and you are surprised, but wants to put her is struggling to pack her favorite oversized teddy. ")
    userOption = input(" Pick a action by giving a number \n Option 1 : let her keep the toy and take some clothes out  \n Option 2 : Tell her its not important leave it \n ")

    if userOption == "1":
        print(" ")
        print ("You decide the clothes are more inportant and leave the teddy, You take her and enter the car with sara and put it into gear")
        print(" ")
        gameState["moralCompass"]+=1
        encounter3()
    elif userOption == "2":
        print(" ")
        print (" You let her keep thr teddy, You take her and enter the car with sara and put it into gear")
        print (" ")
        encounter3()
    else:
        print("invalid input")
        encounter2_part3()

def encounter2_part2():
    print (" You then head for the kitchen and have a choice between water and food or a picture of your wife and the family. ")
    userOption = input(" Pick a action by giving a number \n Option 1 : Take the food and water   \n Option 2 : Take the Picture of your Wife \n ")
    if userOption =="1":
        print(" ")
        print ("You decide the food and water supplies are more inportant and leave the picture.")
        print(" ")
        gameState["inventory"].append("victual")
        encounter2_part3()
    elif userOption =="2":
        print(" ")
        print (" You remember all the good times together and dont want to forget her so you take the picture.")
        print (" ")
        gameState["inventory"].append("Picture")
        encounter2_part3()
    else:
        print("invalid input")
        encounter2_part2()

def encounter2():
    print ("You reach your home and start to pack but you know that you have a limited time and space to gather supplies, your first option is  weather to take a map or gun.")
    userOption = input("Pick a action by giving a number \n Option 1 : Pick up the Gun   \n Option 2 :Pick up the Map \n ")

    if userOption == "1":
        print(" ")
        print (" You pick up a gun and two magazines, just in case. ")
        print (" ")
        gameState["inventory"].append("Gun")
        encounter2_part2()
    elif userOption== "2":
        print(" ")
        print (" You pick up the map, it will come in handy for sure")
        print(" ")
        gameState["inventory"].append("Map")
        encounter2_part2()


def part3_1_encounter1():
    print ("You are make your way through the crowd and once you make it too your car you realise you dont have your keys and deduce that you lost it in the panic you see a old lady struggling to open her car, you wont be able to make it on foot becuase it is a few days away. You know what you have to do but you don't know if you have the strength to do it")
    userOption = input("Pick a action by giving a number \n Option 1 : steal the old ladies car \n Option 2 : decide to walk \n ")
    if userOption== "1":
        print(" ")
        print (" You see an opptunity and take you do have a daughter to look after. After you snatch the keys out the hands of the old women you put Sara in the car and drive but the car break down so you take the rest on foot.")
        print(" ")
        gameState["moralCompass"]+=3
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
        gameState["moralCompass"]+=2
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