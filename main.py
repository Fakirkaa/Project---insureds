from sys import exit
from insured import Insured
from insureds import Records_of_insured_persons

print("RECORDS_OF_INSURED_PERSONS")

insureds = []

continuation = "yes"
while (continuation=="yes"):
    """
    Smyčka k opakovanému výběru akce, dokud uživatel chce    
    """
    print("Choose  action: ")
    print("1 - Add  new insured ")
    print("2 - List all ")
    print("3 - Search insured ")
    print("4 - End ")
    action = int(input(""))

    if(action == 1):
        name = input("Enter the name of the insured \n")
        surename = input("Enter the surename of the insured \n")
        mistake = True
        while mistake:
            """
            Smyčka k ošetření případných chyb při vstupu - hlídá zadání čísla
            """
            try:
                age = int(input("Enter the age of the insured \n"))
                mistake = False
            except ValueError:
                print("Error, age must be a number: \n")
        mistake = True
        while mistake:
            try:
                phone = int(input("Enter the phone number of the insured \n"))
                mistake = False
            except ValueError:
                print("Error, must be a number: \n")
        insureds.append(Insured(name, surename,age,phone))
        print("Press enter to continue \n")

    elif(action ==2):
       for insured in insureds:
            print(insured)
    elif(action == 3):
        print("Search criteria: \n")
        print("Select an option: \n")
        print("1 - by name and surename  \n")
        print("2 - by phone number: \n")
        option = int(input(""))
        if(option == 1):
            search_name = input("Enter the name of the insured you are looking for \n")
            search_surename = input("Enter the surename of the insured you are looking for \n")
            for insured in insureds:
                if search_name == insured.name and search_surename == insured.surename:
                    print(insured)
        else:
           mistake = True
           while mistake:
                """
                 Smyčka k ošetření případných chyb při vstupu - hlídá zadání čísla
                """
                try:
                    serch_phone = int(input("Enter the phone number of the insured you are looking for \n"))
                    mistake = False
                except ValueError:
                    print("Error, must be a number: \n")
           for insured in insureds:
               if serch_phone == insured.phone:
                    print(insured)
    else:
        (action == 4)
        exit()

p1 = Insured(name, surename, age, phone)
print(list_all)


