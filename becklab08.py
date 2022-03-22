import math
names = ["Euclid", "Archimedes", "Newton", "Descartes", "Fermat", "Turing", "Euler", "Einstein",
        "Boole", "Fibonacci", "Lovelace", "Noether", "Nash", "Wiles", "Cantor", "Gauss", "Plato"]
string = ''
for name in names:
    for i in range(0, len(name)):
        if i == (len(name)-1):
            fl_ll = str(name[0] + str(name[i]))
            string = string + fl_ll
print("1)", string)

stack = []
string = ''
list = ['Euclid']
j = 0
for name in names:
    for letter in name:
        stack.append(letter)
    for item in range(len(stack)):
        string = string + stack.pop()
    if j < len(names):
        names[j] = string
        string = ''
        j = j + 1
print("2)", names)


total_ch_cnt = 0
for name in names:
    total_ch_cnt = total_ch_cnt + len(name)
print("3)", total_ch_cnt)


vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U','u']
vowelCnt = 0
for name in names:
    j = 0
    while j < len(name):
        if name[j] in vowel:
            vowelCnt = vowelCnt + 1
        j = j + 1
consonant = total_ch_cnt - vowelCnt
print("4)", consonant)

nameLengthAverage = total_ch_cnt / len(names)
print("5)", round(nameLengthAverage, 2))


names.sort()
x = len(names) / 2
median = math.floor(x)
print("9)", names[median])

vowelNumber = total_ch_cnt - consonant
print("10)", vowelNumber)
