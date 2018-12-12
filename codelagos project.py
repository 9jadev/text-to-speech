import pyttsx3

t ="Hello this is a simple python program to make a  ten item shopping list with text to speech and it is for the fulfilment of my code lagos python  class"
print(t)

def talk(text,rate):
    engine = pyttsx3.init()
    engine.say(text)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()

talk(t,0.9)

talk(" Enter your name dear valued customer ", 25)
name = input("Enter your name dear valued customer")
shopplist = []
count = 0

while (count < 11):
    talk(" Enter your Item dear customer ", 25)
    item = input(" Enter your Item dear customer ")
    shopplist.append(item)
    count = count + 1

t = "Thank you " +str(name)+ " for using this program your items are  "
talk(t,1)
print(t)

for item in shopplist:  
   talk(item,0.9)
   print(item)
    


    
    
