file = open('text.txt')
print(file.read(4))
print(file.read())

for line in file:
	print(line)
	