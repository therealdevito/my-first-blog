numere = [1,2,3,4,5,6,2]
numere.append(16)
numere.pop(6)
numere.sort()
print(numere)

if 3 < 2: # a simple comparator
    print ('it frking works')
else: 
    print ('it frking doesn\'t work')

name = 'andrei' # a more complex one
if name == 'george':
    print('hey geo')
elif name == 'vasile':
    print('hi vasi')
else:
    print('hi andrei')

def hi(name):
    print('hi ' + name + '!')

men = ['andrei', 'vasile', 'gheorghe', 'ionut']
for name in men:
    hi(name)
for i in range(1,10):
    print(i)


