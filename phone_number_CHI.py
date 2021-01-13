def func(words, numbers):
    dic = {
        'a': 2,
        'b': 2,
        'c': 2,
        'd': 3,
        'e': 3,
        'f': 3,
        'g': 4,
        'h': 4,
        'i': 4,
        'j': 5,
        'k': 5,
        'l': 5,
        'm': 6,
        'n': 6,
        'o': 6,
        'p': 7,
        'q': 7,
        'r': 7,
        's': 7,
        't': 8,
        'u': 8,
        'v': 8,
        'w': 9,
        'x': 9,
        'y': 9,
        'z': 9
    }

    converted_words = []
    for word in words:
        converted_word = ''
        for letter in word:
            converted_word += str(dic.get(letter))
        converted_words.append(converted_word)

    output_lst = []

    for i in range(0, len(converted_words)):
        if converted_words[i] in numbers:
            output_lst.append(words[i])
    return output_lst


numbers = '3662277'
words = ['foo','bar','baz','foobar','emo','cap','car','cat']
output = ['bar','cap','car','emo','foo','foobar']

func(words, numbers)
