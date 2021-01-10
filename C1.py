import random

Moralcompass = []
inventory = []

startbutton = (input("Welcome to my suivival horror game set in the post apocaliptic world where the sun is dying and your only hope for you and your daughter Sara is to make it too the last Spacecruiser set to leave \n press ENTER to start\n"))
print ("Your points are counted by the moarality actions you do in the game the more you have the worse the score, You will be given the results at the end. Pick your choices wisely")
Player1 = (input("What do you desire to name yourself :\n"))

Difficulty = input (" To choose difficulty input a number \n Easy: 1 \n Hard: 2 \n Very Hard: 3 \n ")

def sect1options():
    Sec1 = input("Pick a action by giving a number \n Option 1 : get out of chair \n Option 2 : Look around somemore \n Option 3 : Go back too sleep \n ")
    return Sec1

def part2op():
    Sec2OP = input("Pick a action by giving a number \n Option 1 : Run for the nearest exit while carrying your daughter\n Option 2 : calmly leave the room while holding her hand  \n Option 3 : Stay and watch the Tv \n ")
    return Sec2OP

def part301op():
    Sec301 = input("Pick a action by giving a number \n Option 1 : steal the old ladies car \n Option 2 : decide to walk \n ")
    return Sec301

def part302op():
    Sec302OP = input("Pick a action by giving a number \n Option 1 : Help the old lady  \n Option 2 : Just go and leave her, you have your own problems \n ")
    return Sec302OP

def sect2options():
    Sec2 = input("Pick a action by giving a number \n Option 1 : Pick up the Gun   \n Option 2 :Pick up the Map \n ")
    return Sec2

def Sec2op2():
    option2en2 = input(" Pick a action by giving a number \n Option 1 : Take the food and water   \n Option 2 : Take the Picture of your Wife \n ")
    return option2en2

def Sec2op3():
    option3en2 = input(" Pick a action by giving a number \n Option 1 : let her keep the toy and take some clothes out  \n Option 2 : Tell her its not important leave it \n ")
    return option3en2

def sect3options():
    Sec3 = input(" Pick a action by giving a number \n Option 1 : Take the dirt path   \n Option 2 : Stay in traffic   \n Option 3 : continue on foot \n ")
    return Sec3

def Sec3op2():
    option2en3 = input(" Pick a action by giving a number \n Option 1 : Drive through the swamp   \n Option 2 : Walk through the swamp with sara on your back \n ")
    return option2en3

def Sec3op3():
    option2en3 = input(" Pick a action by giving a number \n Option 1 : Bite his arm and run with Sara \n Option 2 : Reach for your Gun *IF YOU PCIKED THE GUN*\n ")
    return option2en3

def sect4options():
    Sect4 = input(" Pick a action by giving a number \n Option 1 : Go for his gun \n Option 2 : Let him take Sara \n ")
    return Sect4

def part302():
    print (" You run to the exit luckly no one is around you make your way to the car and see an old women struggling to open her car you put Sara in the car and think weather to help her")
    res = part302op()
    if res == ("1"):    
        print(" ")
        print (" You help the old lady and she thanks you by giving Sara her neckless saying that it was her mothers and she has no kids so its better off with her .")
        print(" ")
        encounter2()
    elif res == ("2"):
        print(" ")
        print (" You drive off and see her being mugged.")
        print (" ")
        Moralcompass.append(2)
        encounter2()
    else:
        ("invalid input")
    return Moralcompass

def part301():
    print ("You are make your way through the crowd and once you make it too your car you realise you dont have your keys and deduce that you lost it in the panic you see a old lady struggling to open her car, you wont be able to make it on foot becuase it is a few days away. You know what you have to do but you don't know if you have the strength to do it")
    Sec3O1 = part301op()
    if Sec3O1 == ("1"):    
        print(" ")
        print (" You see an opptunity and take you do have a daughter to look after. After you snatch the keys out the hands of the old women you put Sara in the car and drive but the car break down so you take the rest on foot.")
        print(" ")
        Moralcompass.append(3)
        encounter2()
    elif Sec3O1== ("2"):
        print(" ")
        print (" You put Sara on your back and start walking about 5 miles in you see an abandoned bus with food, which stops her from complaining about the hunger you look in the ignition and see somebody left the keys. You thank God and make your way home.")
        encounter2()
    else:
        ("invalid input")
    return Moralcompass

def part2():
    print (" you take a minute to gather your senses and in the shock i dont realise the atmospheric change in the room the TV gets louder and i can see its the news reporters in viable distress the headline reads * The Sun is dying Evacuate to your nearest spacecruiser, You have 5days * you look agian in disbelief.  You grab saras hand and take a quick picture of the nearest one shown on screen.")
    Sec2OP = part2op()
    if Sec2OP == ("1"):
        print(" ")
        print ("While running to the exit people spot you and part to panic for the exit your keys fall out your pocket you decide to leave them and run. You enter the ahllway and its full of people ")
        print(" ")
        part301()
    elif Sec2OP== ("2"):
        print(" ")
        print (" You quickly but calmly leave the room succfully and are able too reach the hallway")
        print(" ")
        part302()
    elif Sec2OP == ("3"):
        print(" ")
        print (" You carry on watching the news report and see that Sara is gone you check the shes crying next to her mother, seeing sara like that makes you loes all your hope in life. \n GAME OVER ")
        print(" ")
    else:
        ("invalid input")
    return part2
     
def encounter1():
    print (" Day 1 \n Your wake in a lounge chair inside a white corridor you look to your left then right and spot a man in formal scrubs by a desk, you panic for you can not seem to spot your daughter") #part1
    Sec1= sect1options()
    if Sec1== ("1"):
        print(" ")
        print (str(Player1)+ " gets out of the chair and stands allowing him to be able to look over the desk and see her at the vending machine,  she was struggling to put the dollar you gave her in the mahcine you walked and help her the doctor you saw earlier taps your shoulder and starts to talk anout your wifes condition. Your face drops you look to your wifes death bed through the window and all you can think about is *how am i going to tell Sara* ")
        print("")
        print(part2())
    elif Sec1== ("2"):
        print(" ")
        print ("You sit up and look around but seen nothing")
        print("look around some more")
        encounter1()
    elif Sec1== ("3"):
        print (" You go back to sleep and wake up to find sara missing you search everwhere but she is gone \n GAME OVER ")
    else:
        print("invalid input")

def en2part3():
    print (" You go in to Saras room and see that she has packed reponsibly and you are surprised, but wants to put her is struggling to pack her favorite oversized teddy. ")
    en2ops3 = Sec2op3()
    if en2ops3  == ("1"):    
        print(" ")
        print ("You decide the clothes are more inportant and leave the teddy, You take her and enter the car with sara and put it into gear")
        print(" ")
        moralpoint = 1
        Moralcompass.append(moralpoint)
        encounter3()
    elif en2ops3 == ("2"):
        print(" ")
        print (" You let her keep thr teddy, You take her and enter the car with sara and put it into gear")
        print (" ")
        encounter3()
    else:
        ("invalid input")
    return Moralcompass

def en2part2():
    print (" You then head for the kitchen and have a choice between water and food or a picture of your wife and the family. ")
    en2ops2 = Sec2op2()
    if en2ops2  == ("1"):    
        print(" ")
        print ("You decide the food and water supplies are more inportant and leave the picture.")
        print(" ")
        inventory.append("victual")
        en2part3()
    elif en2ops2 == ("2"):
        print(" ")
        print (" You remember all the good times together and dont want to forget her so you take the picture.")
        print (" ")
        inventory.append("Picture")
        en2part3()
    else:
        ("invalid input")
    return inventory


def encounter2():
    print ("You reach your home and start to pack but you know that you have a limited time and space to gather supplies, your first option is  weather to take a map or gun.")
    en2ops1 = sect2options()
    if en2ops1  == ("2"):    
        print(" ")
        print (" You pick up the map, it will come in handy for sure")
        print(" ")
        inventory.append("Map")
        en2part2()
        return inventory
    elif en2ops1 == ("1"):
        print(" ")
        print (" You pick up a gun and two magazines, just in case. ")
        print (" ")
        inventory.append("Gun")
        en2part2()
        return inventory
    else:
        ("invalid input")
    

def en3part102():
    print (" You walk down the path for days and it you finnaly see road throught the bushes, the compound is in sight.")
    encounter4()

def en3part3():
    print (" You take cover behind a abandoned vehicle but just before you can think of a plan, you get attacked from behind and as he chokes you realise you have to make a choice")
    Kaa = Sec3op3()
    if Kaa  == ("1"):    
        print(" ")
        print ("You bite a chunk out of his arm and while his distracted you run in to buses with a terrified Sara but not before youre back pack is torn from your back in last ditch effort by the man. You are able to make your way arround the man made check point and reach a path")
        print(" ")
        inventory.remove("Map")
        en3part102()
    elif Kaa == ("2"):
        if inventory[0] == ("Gun"):
            print(" ")
            print (" You reach for your gun and shoot the man in his head, and grab sara and run into the bushes but drop the gun")
            moralpoint = 5
            Moralcompass.append(moralpoint)
            inventory.remove("Gun") 
            print (" ")
            en3part102()
            return Moralcompass
        else:
            print ("*You dont have a Gun*")
            print (inventory)
            en3part3()
    else:
       ("invalid input")
    return inventory


def en3part1():
    print (" You think about the best way to cross the swamp, you have two options. Cross the swamp in the car so you dont have to leave behind any resources or cross on foot")
    en3ops2 = Sec3op2()
    if en3ops2  == ("1"):    
        print(" ")
        print (" You start to drive through the swamp and start to sink, you quickly make a move and unbuckle your and Saras belt. You scale the side of the car with her and make a jump for the safety of solid ground")
        print(" ")
        if inventory == ("victual"):
            inventory.remove("victual")
        if inventory == ("Picture"):
            inventory.remove("Picture")
        if inventory == ("Gun"):
            inventory.remove("Gun")
        if inventory == ("Map"):
            inventory.remove("Map")
        en3part102()
    if en3ops2 == ("2"):
        print(" ")
        if inventory[0] == ("Gun"): 
            print (" You start fill your backpack with the rest of Saras clothes and put the pistol in your jackets zip pocket. You then put Sara on your back and continue to walk, you feel yourself sinking deeper and deeper so you keep moving through the swamp untill it reaches your neck but just as soon as the mud starts to fill your mouth you start slowly raise up higher and higher untill the dirt path is in sight. You finnally make it but your covered in mud ")
        en3part102()
        if inventory[0] == ("map"):
            print (" You start fill your backpack with the map and the rest of Saras clothes. ")
            print (" ")
        en3part102()
    else:
        ("invalid input")
    return inventory

def encounter3():
    print (" Day 3 \n  its chaos a first but after the 2 days it calms down. You end up at traffic jam that wont move for a few days. You see a dirt path that could eithe take that or leave the vehicle, what do you choose. ")
    en3ops = sect3options()
    if en3ops == ("1"):
        print(" ")
        print (" You drive on to the dirt path which leads you through a brush and come across a swamp between you and the rest of the path.")
        print(" ")
        en3part1()
    elif en3ops == ("2"):
        print(" ")
        if inventory[1] == ("victual"):
            print (" You stay in the traffic for a few days and after driving on what was mostly pavement to go get arround all the vacant cars, the supplies you brought come in handy and when you make to the ship it is taking off you ask to let in but the gaurd says *No more passengers* you try and push through but you`re are tazed and pass out. When you wake the streets are empty and Sara is missing. All the ships left you failed. \n GAME OVER ")
        else:
           print (" You run out of supplies quickly and starve after failing to find more food. \n GAME OVER ")
        print(" ")
    elif en3ops == ("3"):
        print(" ")
        print (" You decide to make your way on foot as it is the most reliable, you make great progress at first but then you come accross man made check point you decide to stop and decide your next decision")
        print(" ")
        en3part3()
    else:
        ("invalid input")
    return inventory


def encounter4():
    print ("Day 5 \n  After finally making it to the compound through crowds of people and burning heaps. You get to the check point and are stopped by a security officer and taken to another room, he subtly demands a bribe but you have no money so you give him your wedding ring which then responds with *Thats not enough for the both of you*. You then know you only have two options either to attack him or just let Sara go alone.")
    en4ops = sect4options()
    if en4ops  == ("1"):    
        encounterfight()
    elif en4ops == ("2"):
        ending2()
    else:
        ("invalid input")


def healdifpla():
    if Difficulty == ("1"):
        UsertotalHp = (100)
        return UsertotalHp
    if Difficulty == ("2"):
        UsertotalHp = (80)
        return UsertotalHp
    if Difficulty == ("3"):
        UsertotalHp = (60)
        return UsertotalHp
        
def healdifenem():
    if Difficulty == ("1"):
        totguardHp= (95)
        return totguardHp  
    if Difficulty == ("2"):
        totguardHp= (95)
        return totguardHp  
    if Difficulty == ("3"):
        totguardHp= (95)
        return totguardHp


fight = True
enemHpnow = (healdifenem())
damage = 0
attack = False
strength = (random.randint(10,40))

def diff():
    if Difficulty == ("1"):
        chance = (10)
    if Difficulty == ("2"):
        chance = (5)
    if Difficulty == ("3"):
        chance = (4)
    return chance


def attackchance(attack):
    attack = random.randint(1,15)
    prob = diff()
    if attack >= prob:
        return True

def dmgnumchance(damage):
    damage = strength
    while True:
        print ("You hit and did " + str(damage) + " damage.")
        break
    return damage
    

def damagetoguard():
    enemHpnow = (healdifenem()) - damage
    return enemHpnow

def encounterfight():
    print ("You Go for his gun and are able to take it out his holster but not before he knocks it out your hads you find yourself in a fight to death")
    while fight:
        if healdifenem() > 0:
            inp = input("Pick a action by giving a number \n Option 1 : attack \n ").lower()
            if inp == ("1"):
                attackchance(attack)
                if True:
                    dmgnumchance(damage)
                    print ("His HP is at " + str(()))
                else:
                    print("The gaurd countered your move. \n ")
                    healdifpla() - strength
                    print ("Your HP is at " + (healdifpla()))
                        
        else:
            print("You get knocked back on to the floor and spot the gun that lost in the struggle, you reach for it and pummel him with the handle")
            ending1()
            break





def ending1():
    print (" You put on the gaurds uniform and use his keycard to board the ship, As you shoot off in to space you hold Sara tight and eatch the world get smaller and smaller. You think about all the things you had to do to get here and dont regret anything. \n End of Game ")
    print (Moralcompass)

def ending2():
    print (" You tell Sara that everything is going be okay and tell the gaurd to take her. You watch the ships fly off while thinking about the good times together, You think maybe there was another way but stop yourself from thing that becuase it woulf do harm them good. Your did what you had to and have no regrets.")
    if inventory[1] == ("Picture"):
        print (" You look at the picture of your wife, which reminds you of one time easier times you walk away with a smile. \n End of Game")
    print (Moralcompass)

def ending3():
    print (" The guard grabs the gun after beating you bloody you tell Sara everthing is going to be okay, after he shoots you  \n End of Game ")
    print (Moralcompass)
encounter1()