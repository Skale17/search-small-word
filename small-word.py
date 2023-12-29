
while True:
    text = input('введите текст для поиска кратчайшего слова ')
    word=text.split()
    word.sort(key=len)
    print('кратчайшее слово', word[0])
