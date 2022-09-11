import requests
from bs4 import BeautifulSoup

url = "https://context.reverso.net/translation/"

languages = ["placeholder",
            "Arabic",
             "German",
             "English",
             "Spanish",
             "French",
             "Hebrew",
             "Japanese",
             "Dutch",
             "Polish",
             "Portuguese",
             "Romanian",
             "Russian",
             "Turkish"]


def display_results(page, i, j):
    soup = BeautifulSoup(page.content, 'html.parser')
    words = soup.find_all('span', {'class': 'display-term'})

    print("\n{} translations:".format(languages[j]))
    for w in words:
        print(w.text)

    print("\n{} examples:".format(languages[j]))

    sentences = soup.find('section', {'id': 'examples-content'}).findAll('span', {'class': 'text'})
    i = 1
    for s in sentences:
        print(s.text.strip(), end="")
        if i % 2 == 0:
            print("\n")
        else:
            print(":")
        i += 1

def main():


    print("Hello, welcome to the translator. Translator supports:")
    for i in range(len(languages)):
        print(i, ". ", languages[i], sep="")


    i = -1
    while True:
        language = input("Type the number of your language:")
        try:
            i = int(language)
            if i > 0 and i < len(languages) - 1:
                break
        except:
            pass
        print("bad input! try again")


    j = -1
    while True:
        language = input("Type the number of language you want to translate to:")
        try:
            j = int(language)
            if j > 0 and j < len(languages) - 1 and j != i:
                break
        except:
            pass
        print("bad input! try again")

    word = input("Type the word you want to translate:")
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url + languages[i].lower() + "-" + languages[j].lower() + "/" + word, headers=headers)
    if page.status_code == 200:
        display_results(page, i, j)
    else:
        print("Something went wrong. Perhaps bad input. Try again.")
        main()


if __name__ == "__main__":
    main()
