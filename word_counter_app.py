import fileinput
x = input("Search_Word : ")
search_word = ""
for line in fileinput.input(files='input.txt'):
    search_word += line
search_word = search_word.split("\n")
print(search_word)
if x == "python" or x == "java" or x == "c" or x == "c++":
    x = x.capitalize()
if x == "php" or x == "Php" or x == "oop" or x == "Oop":
    x = x.upper()
if x in search_word:
    y = search_word.count(x)
    print(x, ">", y)
else:
    print(x, ">", "0")
