
with open("Mychoices.txt", 'w') as file:
        choices = file.writelines("MyChoices\n")
while True:
    with open("Mychoices.txt", 'r')as file:
        choices = file.readlines()

    choice = input("Enter your choice YES or NO :")+ "\n"
    choices.append(choice)

    with open ("Mychoices.txt", 'w') as file:
        file.writelines(choices)
    numofyes = choices.count("YES\n")
    percentage = numofyes / len(choices) * 100

    print(f"YES : {percentage}%")