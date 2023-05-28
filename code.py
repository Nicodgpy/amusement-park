print("welcome to the roller coaster")
height=int(input("how tall are you?"))
age=int(input("how old are you?"))

if height >120:
  print("can ride")
  if age >=18:
    print("it would be $12")
  else:
    print("it would be $7")
  
else:
  print("not ride")
