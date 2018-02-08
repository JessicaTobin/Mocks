import webbrowser  #found on StackOverflow in the comments after searching how to open url in python
from time import sleep
while True: #repeats the code
    print("This programme will give you song recommendations depending on your mood")#tells the user what it does
    mood=input("So what mood are you in?")#asks the question which allows the user to type an answer

    if mood=="happy" or "Happy": #if the user types happy then the programme prints the beneath code
        print ("I would recommend Girls by the 1975")
        sleep(1) #pauses the programme for 1 second
        webbrowser.open('https://www.youtube.com/watch?v=QkubQCI4Fxo')#continued opens the link I input
        
    
    elif mood=="sad" or "upset" or "Sad" or "Upset":
        option=input("Would you like a song to cheer you up or embrace the mood?")

        if option=="cheer up" or "Cheer up" or "Cheer Up" or "cheer" or "Cheer":
            print("I recommend In The Middle by Dodie Clark")
            sleep(1)
            webbreowser.open('https://www.youtube.com/watch?v=-1JbefiywEE') #new link opens

        elif option=="embrace the mood" or "Embrace the mood" or "embrace" or "Embrace" or "Embrace the Mood":
            print("I recommend 6/10 by Dodie Clark")
            sleep(1)
            webbreowser.open('https://www.youtube.com/watch?v=5Y8bl-zZy2s') #new link opens

    elif mood=="calm" or "Calm" or "relaxed" or "Relaxed":
        print("I'd recommend Cherry Wine by Hozier")
        sleep(1)
        webbreowser.open('https://www.youtube.com/watch?v=5I4iwiDK_lQ')  #new link opens

    elif mood=="nostalgic" or "Nostalgic":
        print ("I recommend Everyone Wants to Rule the World by Tears For Fears")
        sleep(1)
        webbreowser.open('https://www.youtube.com/watch?v=aGCdLKXNF3w') #new link opens
