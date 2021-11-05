
egyik=input("Írj be egy számot : ")
egyik=int(egyik)
masik=int(input("Adj meg még egy számot: "))
masik=int(masik)
muvelet=input("Kérek egy művelett:ezek közül tudsz választani szorzás=*,osztás=/,összeadás=+,kivonás=- ")

if(muvelet == "*" ):
    print(egyik*masik)
elif(muvelet == "+"):
    print(egyik+masik)
elif(muvelet == "-"):
    print(egyik-masik)
elif(muvelet == "/"):
    print(egyik/masik)

else:
    print("hiba")





