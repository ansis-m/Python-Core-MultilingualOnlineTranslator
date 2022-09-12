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


def write_results(word, i, j):

    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url + languages[i].lower() + "-" + languages[j].lower() + "/" + word, headers=headers)
    if page.status_code == 200:
        file = open(word + '.txt', 'a', encoding='utf-8')
        soup = BeautifulSoup(page.content, 'html.parser')
        words = soup.find_all('span', {'class': 'display-term'})

        # print("\n{} translations:".format(languages[j]))
        file.write("\n{} translations:\n".format(languages[j]))
        for w in words:
            # print(w.text)
            file.write(w.text + "\n")
            break

        # print("\n{} examples:".format(languages[j]))
        file.write("\n{} example:\n".format(languages[j]))

        sentences = soup.find('section', {'id': 'examples-content'}).findAll('span', {'class': 'text'})
        i = 1
        for s in sentences:
            file.write(s.text.strip())
            # print(s.text.strip(), end="")
            if i % 2 == 0:
                # print("\n")
                file.write("\n")
                break
            else:
                # print(":")
                file.write(":\n")
            i += 1
        file.close()

    else:
        print("Something went wrong. Perhaps bad input. Try again.")


def get_input(prompt):

    j = -1
    while True:
        language = input(prompt)
        try:
            j = int(language)
            if j >= 0 and j < len(languages) - 1:
                return j
        except:
            pass
        print("bad input! try again")

def main():

    print("Hello, welcome to the translator. Translator supports:")
    for i in range(1, len(languages)):
        print(i, ". ", languages[i], sep="")


    i = get_input("Type the number of your language:")
    j = get_input("Type the number of a language you want to translate to or '0' to translate to all languages:")
    word = input("Type the word you want to translate:")

    if j == 0:
        for k in range(1, len(languages)):
            if k != i:
                write_results(word, i, k)
    else:
        write_results(word, i, j)

    file = open(word + '.txt', 'r', encoding='utf-8')
    for line in file:
        print(line, end="")
    file.close()


if __name__ == "__main__":
    main()
