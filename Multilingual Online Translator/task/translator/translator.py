import requests
from bs4 import BeautifulSoup

url = "https://context.reverso.net/translation/"
ef = "english-french/"
fe = "french-english/"


def display_results(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    words = soup.find_all('span', {'class': 'display-term'})
    word_list = []
    for w in words:
        word_list.append(w.text)

    sentences = soup.find('section', {'id': 'examples-content'}).findAll('span', {'class': 'text'})
    sentence_list = []
    for s in sentences:
        sentence_list.append(s.text.strip())

    print(word_list)
    print(sentence_list)


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
        print("200 OK")
        print("Translations")
        display_results(page)
    else:
        print("Something went wrong. Perhaps bad input. Try again.")
        main()


if __name__ == "__main__":
    main()
