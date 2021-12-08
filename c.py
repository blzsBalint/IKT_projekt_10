def temp (Cfok):
    if Cfok > 100:
        print ('kurva forró')
    elif Cfok == 100:
        print ('forrás pont')
    elif 79 < Cfok < 100:
        print ('forró')  
    elif 39 < Cfok < 80:
        print ('nagyon meleg')
    elif 19 < Cfok< 60:
        print ('meleg')
    elif 0 < Cfok < 40:
        print ('normál')
    elif 0 < Cfok < 20:
        print ('hideg')
    elif  Cfok == 0:
        print ('fagy pont')
    else:
        print('kurva hideg')
    

for igen in reversed (range (-20,121,1)):
    print (igen,end="")
    print(" °C ---> ",end="")
    temp(igen)
   

       


    

