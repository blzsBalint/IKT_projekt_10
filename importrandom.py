import os
import random
import time
def clear():
    os.system('CLS')

for ismetles in range (10):
   dobas = random.randint (1,6)
   print(dobas)
   if dobas == 1 :
      print("/033[91m")
      print(r"""
       o__________o
      /         @/|
     /    @     /@|
    /@         /  |
   o__________o   |
   |          |   o
   |          |  /
   |     @    |@/
   |          |/
   o__________o
   """)
   elif dobas == 2 :
      print("/033[91m")
      print(r"""
    o__________o
   /@        @/|
  /          / |
 /@        @/  |
o__________o   |
|         @| @ o
|          |  /
|          | /
|@         |/
o__________o
  """)

   elif dobas == 3 :
      print("/033[91m")
      print(r"""
    o__________o
   /         @/|
  /          / |
 /@         /  |
o__________o   |
|         @| @ o
|          |  /
|     @    | /
|@         |/
o__________o
   
      """)
   elif dobas == 4 :
      print("/033[91m")
      print(r"""
    o__________o
   /         @/|
  /          / |
 /@         /  |
o__________o   |
|@        @| @ o
|          |  /
|          | /
|@        @|/
o__________o
  """)

   elif dobas == 5 :
      print("/033[91m")
      print(r"""
    o__________o
   /         @/|
  /     @    / |
 /@         /  |
o__________o   |
|@        @| @ o
|          |  /
|     @    | /
|@        @|/
o__________o
  """)

   elif dobas == 6 :
      print("/033[91m")
      print(r"""
    o__________o
   /         @/|
  /          / |
 /@         /  |
o__________o   |
|@        @| @ o
|@         |  /
|         @| /
|@        @|/
o__________o

  """) 
   time.sleep(1)
   clear()





  