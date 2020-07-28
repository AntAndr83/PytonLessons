vowels = 'aeiouy'
word = list(input("Введите буквы:").lower())
a = len([i for i in word if i in vowels])
print(a)
