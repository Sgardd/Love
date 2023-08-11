#author nouman
import os
import sys
import datetime
#______________def__________#
def clear():
	os.system('clear')
	def p(x):
		print(x)
#______________def END ______#
logo=("""\033[1;97m
███╗   ██╗ ██████╗ ██╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗
████╗  ██║██╔═══██╗██║   ██║████╗ ████║██╔══██╗████╗  ██║
██╔██╗ ██║██║   ██║██║   ██║██╔████╔██║███████║██╔██╗ ██║
██║╚██╗██║██║   ██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║ ╚████║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

\nMY BEST FRIEND KHADIM AND HAMZA
  888\033[1;32m       NS
\033[1;37m--------------------------------------------------
[~] Author   : NOUMAN
[~] Facebook : UNKNOWN
[~] Tool     : Free
[~] Version  : 0.1
\033[1;37m---------------------------------------------""")
clear()
print (logo)
print(35*'_') 
a = int(input("Enter your age: "))
print("Your age is:", a)
if(a>18):
   print("You can love")
   print("Yes")
else:
	print("You cannot love")
	print("No")
	print("Yah!")
	
num = int(input("Enter the value of num: "))
if (num > 0):
   print("Number is negative.")
elif (num == 0):
	print("Number is zero.")
elif(num == 999):
	print("The number is special.")
else:
	print("Number is positive.")
	print("I an happy now")
	
a = input("entr sellct method: ")
print("My name is",a)
x = input("Enter first number: ")
y = input("Enter second number: ")
print(x + y)
print(int(x) * int(y))


	
	

	