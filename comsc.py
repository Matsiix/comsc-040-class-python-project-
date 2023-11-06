seed_color = input("What color is the seed (red, blue, or green)?\n").lower()
    #added a .lower() to so it catches the capitals, not a perfect "fix", obviously


#supposed to check if u actually put numbers/letters
if seed_color.isalpha() == True:
    #checks if it has alphabet characters and not numbers
    soil_moisture = input("Is the soil wet or dry?\n").lower()
    if soil_moisture.isalpha() == True:
        #checks if it has alphabet characters and not numbers
        try:
            #the only way i know how to check if it's an actual int without it crashing immediately
            temperature = int(input("What is the soil temperature?\n"))
        except ValueError:
            input("One or more of your inputs are invalid, press enter to close.\n")
            #just the message that says "hey you have invalid inputs," it is repeated for all the "errors."
            quit()
            #quit isn't the most amazing practice, and i prefer break, but unless i move things around and put everything into a loop, it's the best bet
            #otherwise it'll just crash anyway
    else: 
        input("One or more of your inputs are invalid, press enter to close.\n")
        quit()
elif seed_color.isalpha() == False:
    #this probably isn't the best solution, but i don't have enough knowledge of oher solutions that would be not so time consuming
    input("One or more of your inputs are invalid, press enter to close.\n")
    quit()


if seed_color == "red":
    #A red seed will grow into a flower when planted in soil temperatures above 75°
    if temperature > 75:
        if soil_moisture == "wet":
    #planting the red seed in wet soil will produce a sunflower, otherwise a dandelion
            print("Sunflower")
        elif soil_moisture == "dry":
            print("Dandelion")
    else:
        print("Mushroom")

if seed_color == "blue":
    #A blue seed will grow into a flower when planted in soil temperatures ranging from 60° to 70°
    if 60 <= temperature <= 70:
        if soil_moisture == "wet":
    #planting the blue seed in wet soil will produce a daisy, otherwise a rose
            print("Daisy")
        elif soil_moisture == "dry":
            print("Rose")
    else:
        print("Mushroom")

if seed_color == "green":
    #A green seed will grow into a flower when planted in soil temperatures above 65
    if temperature > 65:
        if soil_moisture == "wet":
    #planting the green seed in wet soil will produce a carnation, otherwise a lily
            print("Carnation")
        elif soil_moisture == "dry":
            print("Lily")
    else:
        print("Mushroom")
