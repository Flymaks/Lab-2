from csv import reader
import xml.etree.ElementTree as et

def xml():
    tree = et.parse("currency.xml")
    root = tree.getroot()
    Value = []
    CharCode = []
    attributes = root.attrib
    for i in range(len(root)):
        for t in root[i].iter("Value"):
            Value.append(t.text)
        for t in root[i].iter("CharCode"):
            CharCode.append(t.text)
    print(f"Values: {Value}")
    print(f"CharCode: {CharCode}")

def publishiers():
    publishiers = set()
    c = 0
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        with open('result.txt', 'w') as output:
            for row in table:
                if c > 0:
                    publishiers.add(row[4])
                c +=1
            print(publishiers)

def popular():
    downloads = [[] * k for k in range(9500)]
    c = 0
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        with open('result.txt', 'w') as output:
            for row in table:
                if c > 0:
                    downloads[c] = [int(row[5]), row[1]]
                c += 1
        downloads.sort(reverse=True)
        for i in range(20):
            print(downloads[i][1])

def file():
    c = 0
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        with open('result.txt', 'w') as output:
            for row in table:
                c += 1
                if c % 450 == 0:
                    output.write(f'{c // 450} {row[2]}. {row[1]} - {row[3]}\n')

def len_name():
    flag = 0
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        with open('result.txt', 'w') as output:
            for row in table:
                if len(row[1]) > 30:
                    flag += 1
            if flag == 0:
                print('Ничего не найдено.')
            else:
                print(f'Найдено {flag} результатов с названием длиннее 30 символов.')

def author():
    while True:
        search_author = input("Введите автора:")
        flag2 =  0
        if search_author == '0':
            break
        c = 0
        with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
            table = reader(csvfile, delimiter=';')
            with open('result.txt', 'w') as output:
                for row in table:
                    if row[2] == search_author:
                        print(row[2], row[1])
                        flag2 += 1
            print(f'Найдено {flag2} результатов {search_author}')

if __name__ ==  "__main__":
    author()
    # xml()
    # publishiers()
    # file()
    # len_name()
    #popular()
    