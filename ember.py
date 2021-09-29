nev= input ('Hogy hívnak ? ')
kor= int (input('Hány éves vagy ? '))
suly= int (input('Hány kg vagy ? '))
cm= int (input('Hány cm vagy ? '))



print ('Szia '+ nev + ' aki ', kor ,'éves', suly , 'kg', cm , 'cm magas ')
if(kor < 18):
   print('még suli idő van tanuljál')
else:
    print('menj már be nekem a dohiba')
if (cm < 190):
   print('te kerti törpe')
else:
    print('te büdös zsiráf')

if (suly > 80):
    print ( 'dagadt fasz')
else:
    print('  anoreksziás geci')    
