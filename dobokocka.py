import random
import time

dobas_input = int (input('Tippelj hanyast dobtam '))


for ciklus in range (6):
    x= random.randint(1,6)
if dobas_input == x :
    print (x, ':TALÁLT')
    nyert = True
else:
    print(x.'')
    time.sleep (0.2)
if nyert:
    print('***NYERTÉL***')
else:
    print('!!! VESZTETTÉL !!!')

