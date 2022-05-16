tupleList = []

# Meny
def Input():
    print("\nMenu for dictionary")
    print("1: Insert")
    print("2: LookUp")
    print("3: Exit")

    choise = input()

    # Om input är 1, kör insert functionen
    if choise == '1':
        insert()
    # Om input är 2, kör lookUp functionen
    elif choise == '2':
        lookUp()
    # Om input är 3, avsluta programmet
    elif choise == '3':
        return 0
    else:
        print("Input not valid")
    
    # Kör programmet igen
    Input()

# Lägg till ord
def insert():
    print("Word to insert: ")
    text = input()

    # Kontrollera om ordet finns redan
    for i in range(len(tupleList)):
        if text in tupleList[i]:
            print("Word already exist")
            return 0
    
    # Lägg ordet och beskrivningen i dictionary
    print("Description of word: ")
    definition = input()
    tupleList.append(tuple((text, definition)))

# Visa beskrivning på ordet
def lookUp():
    print("Word to lookup: ")
    keyWord = input()

    # Kontrollera om listan är tom
    if not tupleList:
        print("List is empty")
        return 0

    # Visa beskrivning på ordet
    for i in range(len(tupleList)):
        if tupleList[i][0] == keyWord:
            print(tupleList[i][1])
            return 0
    print("Word does not exist")

Input()