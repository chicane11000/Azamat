text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

list = text.split()

print(list)

file = open('text3.txt', 'w')

for word in list:
	file.write(word)
