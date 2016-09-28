def insertIntoBox(word):
    output = ""

    output += "-" * ( len(word) + 4 ) + "\n" # repeat dash `len(word)` (lenght of the word) times and add 4 for "padding"
    output += "| %s |\n" % (word)
    output += "-" * ( len(word) + 4 ) + "\n"

    return output

def transformToLowercase(word):
    return word.lower()

def transformToUppercase(word):
    return word.upper()

def mirror(word):
    return word[::-1]

def repeat(word):
    output = ""
    isUpperCase = False

    times = input("How many times should it be repeated? ")

    for i in range(1, int(times) + 1):
        if isUpperCase:
            output += transformToUppercase(word)
        else:
            output += transformToLowercase(word)

        isUpperCase = not isUpperCase

    return output


def run():
    word = input("Enter a word: ")

    print("""
1) Display in a Box - display the word in an ascii art box
2) Display Lower-case - display the word in lower-case e.g. hello
3) Display Upper-case - display the word in upper-case e.g. HELLO
4) Display Mirrored - display the word with its mirrored word e.g. Hello | olleH
5) Repeat - ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case
""")

    option = int(input("Your option: "))

    if option == 1:
        print(insertIntoBox(word))
    elif option == 2:
        print(transformToLowercase(word))
    elif option == 3:
        print(transformToUppercase(word))
    elif option == 4:
        print(mirror(word))
    elif option == 5:
        print(repeat(word))
    else:
        print("You can only choose between options 1, 2, 3, 4 and 5.")

run()
