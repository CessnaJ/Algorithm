word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    where = word.find(i)
    print(where, end=' ')