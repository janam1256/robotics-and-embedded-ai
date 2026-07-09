file = open("data.txt", "w" )
file.write("Hello Janam\n")
file.write("Hi")
file.close()



file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
           