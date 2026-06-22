def count_words(st):
    """ 
    Подсчет слов в тексте.
    
    Дано предложение, необходимо подсчитать, 
    сколько раз встречается каждое слово.
    """

    words = st.split()
    count = set(((word, words.count(word)) for word in words))
    for i in count:
        print(*i)

count_words(input())