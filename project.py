#Libraries

import cv2
import numpy as np
import time
import RPi.GPIO as GPIO
import time



#To return the switch number
def switch():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
#GPIO connections
    GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)




    while True:
        button1 = GPIO.input(2)
        button2 = GPIO.input(3)
        button3 = GPIO.input(4)
        button4 = GPIO.input(5)
        button5 = GPIO.input(6)
        if button1 == False:
            print('Button 1 Pressed')
            time.sleep(0.2)
            return 1
        if button2 == False:
            print('Button 2 Pressed')
            time.sleep(0.2)
            return 2
                
        if button3 == False:
            print('Button 3 Pressed')
            time.sleep(0.2)
            return 3
            
        if button4 == False:
            print('Button 4 Pressed')
            time.sleep(0.2)
            return 4
        
        
        if button5 == False:
            print('Button 5 Pressed')
            time.sleep(0.2)
            return 5
            

#Function to display an image
def disp(img):
    cv2.namedWindow("Window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Window',img)
    cv2.waitKey(2000)


#Function to concatinate two images
def concat(img1,img2):
    return (np.concatenate((img1, img2), axis=0))
  

#Fucntion to open an image 
def openImage(n,i):
    if i==0:
        if(n==1 or n==49):
           img=cv2.imread('modem.jpg',1)
        elif n==2 or n==50:
            img=cv2.imread('satellite.jpg',1)
        elif n == 3 or n==51:
            img = cv2.imread('broadband.jpg', 1)
        elif n == 4 or n==52:
            img = cv2.imread('satm.jpg', 1)
        else:
            img=cv2.imread('tower.jpg',1)
        return img
    else :
        if n==1:
            img=cv2.imread('wifi.png',1)
        elif n==2:
            img=cv2.imread('nowifi.png',1)
        else:
            img=cv2.imread('initial.jpg',1)
        return img

#Function to check for the combination
def select(choice):
    if choice==(1,3) or choice==(3,1):
        print("Wifi !! Home")
        img=openImage(1,1)
        disp(img)
        time.sleep(2)
        cv2.destroyAllWindows()

    elif choice==(1,5) or choice==(5,1):
        print("Wifi !! Home")
        img = openImage(1, 1)
        disp(img)
        time.sleep(2)
        cv2.destroyAllWindows()

    elif choice==(2,4) or choice==(4,2):
        print("Wifi !! Forest")
        img = openImage(1, 1)
        disp(img)
        time.sleep(2)
        cv2.destroyAllWindows()

    else:
        print("No Internet :(")
        img = openImage(0, 1)
        disp(img)
        time.sleep(2)
        cv2.destroyAllWindows()
        
        
if __name__=="__main__":
    initial=openImage(3,1)
    disp(initial)
    choice1=switch()
    img1=openImage(choice1,0)
    disp(img1)
    choice2=switch()
    img2=openImage(choice2,0)
    img2=openImage(choice2,0)
    combine=concat(img1,img2)
    disp(combine)
    choice=(choice1,choice2)
    select(choice)


