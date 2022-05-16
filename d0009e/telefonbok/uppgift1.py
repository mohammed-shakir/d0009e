# Main function
def Input():
    dictionary = {}

    # Re-run the script 
    while True:
        command = []
        inputs = input("telebok> ")

        # Divide the sentence into different sections
        split = inputs.split()

        # Append the diffrent parts into a list
        for i in split:
            command.append(i)

        # If the input is equivalent to one of the following words, run the function that is equal to the word
        if command[0] == 'add':
            add(dictionary, command)

        elif command[0] == 'lookup':
            lookup(dictionary, command)

        elif command[0] == 'alias':
            alias(dictionary, command)

        elif command[0] == 'change':
            change(dictionary, command)

        elif command[0] == 'save':
            save(dictionary, command)

        elif command[0] == 'load':
            dictionary = {}
            load(dictionary, command)

        # If input is "exit", stop the script
        elif command[0] == 'exit':
            return 0

        else:
            print("Command does not exist")

# Add a number to a given name
def add(dictionary, command):
    # Check if input is correct
    if len(command) < 3 or len(command) > 3:
        print("Invalid input")
        return 0

    # Check if the name exists
    elif command[1] in dictionary:
        print("Name already exist")
        return 0

    # Check if the number exist
    for i in dictionary:
        if command[2] == dictionary[i][0][1]:
            print("Number already exist")
            return 0

    # Put the name and the number in the dictionary
    list1 = [["nummer: ", command[2]],["alias: "]]
    dictionary.update({command[1]:list1})
    print(dictionary)

# Look up number of a given name
def lookup(dictionary, command):
    # Check if input is correct
    if len(command) < 2 or len(command) > 2:
        print("Invalid input")
        return 0

    # Check if dictionary is empty
    elif not dictionary:
        print("List is empty")
        return 0

    # Show the number of a given alias
    for i in dictionary:
        for j in range(len(dictionary[i][1])):
            if command[1] == dictionary[i][1][j]:
                print(dictionary[i][0][1])
                return 0

    # Show the number of a given name
    try:
        print(dictionary[command[1]][0][1])
    except:
        print("Name does not exist")

# Allows name to be searchable under other names
def alias(dictionary, command):
    # Check if input is correct
    if len(command) < 3 or len(command) > 3:
        print("Invalid input")
        return 0
    
    keys = []
    for key in dictionary.keys():
        keys.append(key)

    for i in keys:
        if command[2] == i:
            print("Name already exists")
            return 0

    # Search for the alias name and put the alias in the dictionary
    for i in dictionary:
        for j in range(len(dictionary[i][1])):
            if command[1] == dictionary[i][1][j]:
                dictionary[i][1].append(command[2])
                return 0

    # Search for the key name and put the alias in the dictionary
    try:
        dictionary[command[1]][1].append(command[2])
    except:
        print("Name does not exist")

# Change the number of a given name
def change(dictionary, command):
    # Check if input is correct
    if len(command) < 3 or len(command) > 3:
        print("Invalid input")
        return 0
    
    for i in dictionary:
        if command[2] == dictionary[i][0][1]:
            print("Number already exist")
            return 0

    # Search for the alias name and change the number of the alias
    for i in dictionary:
        for j in range(len(dictionary[i][1])):
            if command[1] == dictionary[i][1][j]:
                dictionary[i][0][1] = command[2]
                return 0

    # Search for the key name and change the number of the key
    try:
        dictionary[command[1]][0][1] = command[2]
    except:
        print("Name does not exist")

# Save dictionary to a file
def save(dictionary, command):
    # Check if input is correct
    if len(command) < 2 or len(command) > 2:
        print("Invalid input")
        return 0

    # Save dictionary to a txt file
    with open(command[1], "w") as text_file:
        for i in dictionary:
            key = i
            nummber = dictionary[i][0][1]
            text_file.write(nummber+";"+key+";\n")

# Load file as a dictionary
def load(dictionary, command):
    # Check if input is correct
    if len(command) < 2 or len(command) > 2:
        print("Invalid input")
        return 0

    n = 0
    # Read the txt file and convert it to a dictionary
    with open(command[1], "r") as text_file:
        row = text_file.read()
        # Differentiate between key and value
        split = row.split(";")
        # Update dictionary
        for i in split:
            n += 1
            if n%2 != 0:
                list1 = [["nummer: ", i],["alias: "]]
            else:
                dictionary.update({i:list1})

Input()