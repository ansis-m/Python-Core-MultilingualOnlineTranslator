
def main():

    language = ""
    while language != "en" and language != "fr":
        language = input("Type \"en\" if you want to translate from French into English, or \"fr\" if you want to translate from English into French:")

    word = input("Type the word you want to translate:")

    print("You chose {} as a language to translate {}.".format(language, word))

if __name__ == "__main__":
    main()
