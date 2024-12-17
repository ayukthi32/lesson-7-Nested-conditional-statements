#activity2
medical_cause = input("Do you hv a medical cause enter Y or N: ")
attendance = int(input("Enter your attendance:"))

if medical_cause=='Y':
    print("Youe are allowed")
else:
    if attendance>=75 :
        print("You are allowed")
    else :
        print("You are not allowed")
