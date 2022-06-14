import random as r
import string
from re import X
import pyautogui

###########################################       Made With <3       ###########################################
#########################################     By UGoingNoWhereBoy      #########################################



  
### the random values
signs = ("!@#$%^&*()")
numbers = ("1234567890")
letters = ("qwertyuiopasdfghjklzxcvbnm") + signs + numbers + ("QWERTYUIOPASDFGHJKLZXCVBNM")


class gen():
     def __init__(self):
          pass

     def  gen_password(self, length):
          password = ""
          for n in range(length):
               x = r.randint(0, 71)
               password += letters[x]
          return password


c = gen()

### change the value 5 to how many passwords you want to print 
for gen in range(10):
    #### change the value 16 to the length of the password you want 
    print(c.gen_password(16))


 
### To check out how secure is your Password : security.org/how-secure-is-my-password/