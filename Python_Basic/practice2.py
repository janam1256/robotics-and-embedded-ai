file = open("important.txt", "r")
content = file.read()
print(content)
file.close()


file = open("janam.txt", "w")
file.write("Hello Guys")
file.close()

file = open("janam.txt", "r")
content = file.read()
print(content)
file.close()

