import requests
from bs4 import BeautifulSoup

url = "https://context.reverso.net/translation/"
ef = "english-french/"
fe = "french-english/"


def display_results(page, language):
    soup = BeautifulSoup(page.content, 'html.parser')
    words = soup.find_all('span', {'class': 'display-term'})
    print("200 OK")
    print("\n{} translations:".format("French" if language == "fr" else "English"))
    for w in words:
        print(w.text)

    print("\n{} examples:".format("French" if language == "fr" else "English"))

    sentences = soup.find('section', {'id': 'examples-content'}).findAll('span', {'class': 'text'})
    i = 1
    for s in sentences:
        print(s.text.strip())
        if i % 2 == 0:
            print()
        i += 1

def main():

    language = ""
    while language != "en" and language != "fr":
        language = input("Type \"en\" if you want to translate from French into English, or \"fr\" if you want to translate from English into French:")

    word = input("Type the word you want to translate:")
    print("You chose {} as a language to translate {}.".format(language, word))

    headers = {'User-Agent': 'Mozilla/5.0'}
    if language == "en":
        address = url + fe + word
    else:
        address = url + ef + word
    page = requests.get(address, headers=headers)
    if page.status_code == 200:
        display_results(page, language)
    else:
        print("Something went wrong. Perhaps bad input. Try again.")
        main()


if __name__ == "__main__":
    main()
