#activity4
print("Select your ride")
print("1. BIKE")
print("2. car")
choice = int(input("Enter your choice"))
if choice==1 :
    print("What type of bike do u prefer")
    print("1. Scooty")
    print("2. Scooter")
    choice2 = int(input("Enter your choice"))
    if choice2==1 :
        print("You have selected scooty")
    else :
        print("You have selected scooter")
elif choice==2 :
    print("What type of car do u prefer")
    print("1. Sedan")
    print("2. Honda")
    choice2 = int(input("Enter your choice"))
    if choice2==1 :
        print("You have selected Sedan")
    else :
        print("You have selected Honda")