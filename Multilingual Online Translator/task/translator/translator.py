import sys
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

        file.write("\n{} translations:\n".format(languages[j]))
        for w in words:
            file.write(w.text + "\n")
            break

        file.write("\n{} example:\n".format(languages[j]))

        sentences = soup.find('section', {'id': 'examples-content'}).findAll('span', {'class': 'text'})
        i = 1
        for s in sentences:
            file.write(s.text.strip())
            if i % 2 == 0:
                file.write("\n")
                break
            else:
                file.write(":\n")
            i += 1
        file.close()

    else:
        print("Something went wrong. Perhaps bad input. Try again.")

def main():


    args = sys.argv
    if len(args) != 4:
        print("This programm requires 3 arguments. Try again!")
        sys.exit(1)


    word = args[3]
    for k in range(1, len(languages)):
        if args[1].capitalize() == languages[k]:
            i = k
        if args[2].capitalize() == languages[k]:
            j = k

    if args[2] == "all":
        j = 0

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
