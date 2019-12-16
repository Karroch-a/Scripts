list = []

for n in range(9999):
	key = 'cafe'
	for i in range(len(str(n)) + len(key), 8):
		key += str(0)
	key += '{}\n'.format(n)
	list.append(key)

with open('Generator_OUTPUT.txt', 'w+') as file:
	file.writelines(list)