# File handling in Python All
f = open("AyushOjha.txt", "w+")
f.write("My name is Ayush Ojha.\n")
f.write("Ayush Ojha is a God.\n")
f.write("Ayush Ojha plays various games.\n")
f.write("Ayush Ojha wants to do amazing things in file.\n")
f.write("Ayush Ojha is lazy af.\n")
f.write("Ayush Ojha spends his time wasting on nothing.\n")
f.close()

# Printing all the lines in text document.
f = open("AyushOjha.txt", "r")
print(f.read())
f.close()

# Finding the lines that start with Ayush and also printing with one other line
# that doesnt start with Ayush.
for line in open('AyushOjha.txt'):
    if line.startswith('Ayush'):
        print(line)
    else:
        print("Other one: " + line)
