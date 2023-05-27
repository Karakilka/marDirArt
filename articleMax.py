def maxx_w(file):
    with open(file, encoding='utf-8') as text:
        words = text.read().split()
        max_len = len(max(words, key=len))
        sought_w = [word for word in words if len(word) == max_len]
        if len(sought_w) == 1:
            return sought_w[0]
        return sought_w


print(maxx_w('C:/Users/ulyan/pogrammy/article.txt'))