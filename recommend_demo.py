from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
from time import sleep
from time import strftime
from time import localtime
import io
import urllib.request
import socket

#CREATE MAIN WINDOW
recommendGUI=Tk()
recommendGUI.title("Recommender GUI Window")
recommendGUI.geometry('600x800')
recommendGUI.wm_attributes("-transparentcolor", 'grey')

restaurants = ["McDonald's",
    "Wendy's",
    "Rathskeller Eatery",
    "Hardee's",
    "Outback Steakhouse",
    "Longhorns",
    "Mustard's Last Stand",
    "Chipotle",
    "Rain-Bo Island",
    "Panda Express",
    "Panera Bread",
    "Subway",
    "Amazing Food Place",
    "McDonald's but Expensive"]
ratings = [None] * 14

rest_count = 0

canvas = Canvas(recommendGUI, width = 600, height = 800)

#Button Functions
def pickOne():
    global rest_count
    global ratings
    if(rest_count <= 13):
        ratings[rest_count] = 1
    refresh()

def pickTwo():
    global rest_count
    global ratings
    if(rest_count <= 13):
        ratings[rest_count] = 2
    refresh()

def pickThree():
    global rest_count
    global ratings
    if(rest_count <= 13):
        ratings[rest_count] = 3
    refresh()

def pickFour():
    global rest_count
    global ratings
    if(rest_count <= 13):
        ratings[rest_count] = 4
    refresh()

def pickFive():
    global rest_count
    global ratings
    if(rest_count <= 13):
        ratings[rest_count] = 5
    refresh()

def pickSix():
    global rest_count
    global ratings
    if(rest_count <= 13):
        ratings[rest_count] = 6
    refresh()

def pickSeven():
    global rest_count
    global ratings
    if(rest_count <= 13):
        ratings[rest_count] = 7
    refresh()

def pickEight():
    global rest_count
    global ratings
    if(rest_count <= 13):
        ratings[rest_count] = 8
    refresh()

def pickNine():
    global rest_count
    global ratings
    if(rest_count <= 13):
        ratings[rest_count] = 9
    refresh()

def pickTen():
    global rest_count
    global ratings
    if(rest_count <= 13):
        ratings[rest_count] = 10
    refresh()

def refresh():
    global rest_count
    global ratings
    global dataFrame
    if(rest_count == 0):
        
        global imageHolder2
        imageHolder2.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Wendy's"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="3.4 Stars        $        7 minute drive"
                        )
        moreData.place(x=10,y=570)
        
    if(rest_count == 1):
        
        global imageHolder3
        imageHolder3=Label(recommendGUI, image=stillImage3)
        imageHolder3.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Rathskeller Eatery"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="3.7 Stars        $        2 minute drive"
                        )
        moreData.place(x=10,y=570)
        
    if(rest_count == 2):
        
        global imageHolder4
        imageHolder4=Label(recommendGUI, image=stillImage4)
        imageHolder4.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Hardee's"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="4.4 Stars        $        4 minute drive"
                        )
        moreData.place(x=10,y=570)
        
    if(rest_count == 3):
        
        global imageHolder5
        imageHolder5=Label(recommendGUI, image=stillImage5)
        imageHolder5.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Outback Steakhouse"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="4.2 Stars        $$       7 minute drive"
                        )
        moreData.place(x=10,y=570)
    
    if(rest_count == 4):
        
        global imageHolder6
        imageHolder6=Label(recommendGUI, image=stillImage6)
        imageHolder6.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Longhorn Steakhouse"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="4.0 Stars        $$      14 minute drive"
                        )
        moreData.place(x=10,y=570)
    
    if(rest_count == 5):
        
        global imageHolder7
        imageHolder7=Label(recommendGUI, image=stillImage7)
        imageHolder7.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Mustard's Last Stand"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="4.6 Stars        $        5 minute drive"
                        )
        moreData.place(x=10,y=570)
    
    if(rest_count == 6):
        
        global imageHolder8
        imageHolder8=Label(recommendGUI, image=stillImage8)
        imageHolder8.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Chipotle"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="3.6 Stars        $        8 minute drive"
                        )
        moreData.place(x=10,y=570)
    
    if(rest_count == 7):
        
        global imageHolder9
        imageHolder9=Label(recommendGUI, image=stillImage9)
        imageHolder9.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Rain-Bo Island"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="4.4 Stars        $        4 minute drive"
                        )
        moreData.place(x=10,y=570)
    
    if(rest_count == 8):
        
        global imageHolder10
        imageHolder10=Label(recommendGUI, image=stillImage10)
        imageHolder10.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Panda Express"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="4.0 Stars        $       12 minute drive"
                        )
        moreData.place(x=10,y=570)
    
    if(rest_count == 9):
        
        global imageHolder11
        imageHolder11=Label(recommendGUI, image=stillImage11)
        imageHolder11.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Panera Bread"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="4.1 Stars        $$      13 minute drive"
                        )
        moreData.place(x=10,y=570)
    
    if(rest_count == 10):
        
        global imageHolder12
        imageHolder12=Label(recommendGUI, image=stillImage12)
        imageHolder12.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Subway"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="4.0 Stars        $        8 minute drive"
                        )
        moreData.place(x=10,y=570)
    
    if(rest_count == 11):
        
        global imageHolder13
        imageHolder13=Label(recommendGUI, image=stillImage13)
        imageHolder13.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Amazing Food Place"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="4.0 Stars        $$$$$$$$     1 minute drive"
                        )
        moreData.place(x=10,y=570)
    
    if(rest_count == 12):
        
        global imageHolder14
        imageHolder14=Label(recommendGUI, image=stillImage14)
        imageHolder14.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="McDonald's But Expensive"
                    )
        dataFrame.place(x=250,y=0)
        
        moreData=Label(recommendGUI,
                        font=(60),
                        text="4.0 Stars        $$$$$      5 minute drive"
                        )
        moreData.place(x=10,y=570)
    
    if(rest_count == 13):
        
        global imageHolderFin
        imageHolderFin=Label(recommendGUI, image=stillImageFin)
        imageHolderFin.place(x=0,y=0)
        
        dataFrame=Label(recommendGUI,
                    font=(60),
                    text="Please wait..."
                    )
        dataFrame.place(x=250,y=0)
        ratingsFrame=Label(recommendGUI,
                    font=(60),
                    text = (str(ratings[0]) + '\n' + str(ratings[1]) + '\n' + str(ratings[2]) + '\n' 
                    + str(ratings[3]) + '\n' + str(ratings[4]) + '\n' + str(ratings[5]) + '\n' + str(ratings[6]) + '\n' 
                    + str(ratings[7]) + '\n' + str(ratings[8]) + '\n' + str(ratings[9]) + '\n' + str(ratings[10]) + '\n' 
                    + str(ratings[11]) + '\n' + str(ratings[12]) + '\n' + str(ratings[13]))
                    )
        ratingsFrame.place(x=550, y=100)
        
        # Create a client socket

        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

        # Connect to the server

        clientSocket.connect(("192.168.109.130",9090))

        # Send data to server

        data = (str(ratings[0]) + ',' + str(ratings[1]) + ',' + str(ratings[2]) + ',' 
        + str(ratings[3]) + ',' + str(ratings[4]) + ',' + str(ratings[5]) + ',' + str(ratings[6]) + ',' 
        + str(ratings[7]) + ',' + str(ratings[8]) + ',' + str(ratings[9]) + ',' + str(ratings[10]) + ',' 
        + str(ratings[11]) + ',' + str(ratings[12]) + ',' + str(ratings[13]) + ',' + str(clientSocket.getsockname()[0]));

        clientSocket.send(data.encode())

        # Receive data from server
        
        dataFromServer = clientSocket.recv(1024)

        # Print to the console

        print(dataFromServer.decode())
        
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(("192.168.109.1",9090))
        print(serverSocket.getsockname()[0])
        serverSocket.listen()

        (clientConnected, clientAddress) = serverSocket.accept()
        print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))

        dataFromClient = clientConnected.recv(1024)
        data_decode = dataFromClient.decode()
        data_decode = int(data_decode)
        
        print(data_decode)
        global imageHolderWh
        imageHolderWh=Label(recommendGUI, image=stillImageWh)
        imageHolderWh.place(x=0,y=0)
        
        resFrame=Label(recommendGUI,
                    font=(60),
                    text = (restaurants[data_decode])
                    )
        resFrame.place(x=250, y=300)
        
        clientConnected.send("Received.".encode())
        
    if(rest_count > 13):
        
        recommendGUI.destroy()
        
    rest_count += 1
    
#WIDGETS
    #entire frame
Frame=(recommendGUI)  

urllib.request.urlretrieve(
  'http://www.clker.com/cliparts/7/b/8/8/1433860761345476851blue-button-hi.png',
   "button.png")
   
bottomimg = Image.open("button.png")
bottomimg = bottomimg.resize((600, 400)) 

stillImageEx=ImageTk.PhotoImage(bottomimg)
imageHolderEx=Label(recommendGUI, image=stillImageEx)
imageHolderEx.place(x=0,y=500)

urllib.request.urlretrieve(
  'https://media-cdn.tripadvisor.com/media/photo-s/0e/89/cd/9b/looking-good.jpg',
   "mac.png")

imgtest = Image.open("mac.png")
imgtest = imgtest.resize((600, 600)) 

stillImage=ImageTk.PhotoImage(imgtest)
imageHolder=Label(recommendGUI, image=stillImage)
imageHolder.place(x=0,y=0)

dataFrame=Label(recommendGUI,
                font=(60),
                text="McDonalds"
                )
dataFrame.place(x=250,y=0)

moreData=Label(recommendGUI,
                font=(60),
                text="2.6 Stars        $        6 minute drive"
                )
moreData.place(x=10,y=570)
#Downloading extra images

urllib.request.urlretrieve(
          'https://dynl.mktgcdn.com/p/IqIuwfyfi12qOxK54MtSfQYHxfpxRFtNL8AMbSeNACk/1900x1068.jpg',
           "wendys.jpg")

img2 = Image.open("wendys.jpg")
img2 = img2.resize((600, 600)) 

stillImage2=ImageTk.PhotoImage(img2)
imageHolder2=Label(recommendGUI, image=stillImage2)

urllib.request.urlretrieve(
          'https://img.restaurantguru.com/rd40-Rathskeller-Eatery-and-Convenience-Store-design-2021-09.jpg',
           "rat.jpg")

img3 = Image.open("rat.jpg")
img3 = img3.resize((600, 600)) 

stillImage3=ImageTk.PhotoImage(img3)
imageHolder3=Label(recommendGUI, image=stillImage3)


urllib.request.urlretrieve(
          'https://dynl.mktgcdn.com/p/AU1k60F88Ivrf5J9bXbM-ZeVQjctgHvMYCN1rQbAppg/1080x720.jpg',
           "hardees.png")

img4 = Image.open("hardees.png")
img4 = img4.resize((600, 600)) 

stillImage4=ImageTk.PhotoImage(img4)
imageHolder4=Label(recommendGUI, image=stillImage4)

urllib.request.urlretrieve(
          'https://media-cdn.tripadvisor.com/media/photo-s/0e/63/d6/ff/outback-steakhouse.jpg',
           "outback.jpg")

img5 = Image.open("outback.jpg")
img5 = img5.resize((600, 600)) 

stillImage5=ImageTk.PhotoImage(img5)
imageHolder5=Label(recommendGUI, image=stillImage5)

urllib.request.urlretrieve(
          'https://media.longhornsteakhouse.com/en_us/images/marketing/LH_BuildingFront_599x430.jpg',
           "longhorn.jpg")

img6 = Image.open("longhorn.jpg")
img6 = img6.resize((600, 600)) 

stillImage6=ImageTk.PhotoImage(img6)
imageHolder6=Label(recommendGUI, image=stillImage6)

urllib.request.urlretrieve(
          'https://s3-media0.fl.yelpcdn.com/bphoto/DEAoVdK1uhlILvsaQY3RqQ/l.jpg',
           "mustard.jpg")

img7 = Image.open("mustard.jpg")
img7 = img7.resize((600, 600)) 

stillImage7=ImageTk.PhotoImage(img7)
imageHolder7=Label(recommendGUI, image=stillImage7)

urllib.request.urlretrieve(
          'https://cdn.winsightmedia.com/platform/files/public/2021-06/background/Chipotle-Shutterstock%20%281%29_1623272018.jpg?VersionId=G7Y52i7uyjx_CyHUtammhS3ydCs7qT5A',
           "chipotle.jpg")

img8 = Image.open("chipotle.jpg")
img8 = img8.resize((600, 600)) 

stillImage8=ImageTk.PhotoImage(img8)
imageHolder8=Label(recommendGUI, image=stillImage8)

urllib.request.urlretrieve(
          'https://s3-media0.fl.yelpcdn.com/bphoto/OQaVovtmgtj3AWOwy4Hcow/o.jpg',
           "rainbo.jpg")

img9 = Image.open("rainbo.jpg")
img9 = img9.resize((600, 600)) 

stillImage9=ImageTk.PhotoImage(img9)
imageHolder9=Label(recommendGUI, image=stillImage9)

urllib.request.urlretrieve(
          'https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_10/1685500/panda-express-lawsuit-nc-main-031021.jpg',
           "panda.jpg")

img10 = Image.open("panda.jpg")
img10 = img10.resize((600, 600)) 

stillImage10=ImageTk.PhotoImage(img10)
imageHolder10=Label(recommendGUI, image=stillImage10)

urllib.request.urlretrieve(
          'https://media-cdn.tripadvisor.com/media/photo-s/0a/22/8f/ac/panera-bread.jpg',
           "panera.jpg")

img11 = Image.open("panera.jpg")
img11 = img11.resize((600, 600)) 

stillImage11=ImageTk.PhotoImage(img11)
imageHolder11=Label(recommendGUI, image=stillImage11)

urllib.request.urlretrieve(
          'https://cdn.britannica.com/08/193908-050-66767D57/view-Subway-restaurant-Bangkok-Thailand.jpg',
           "subway.jpg")

img12 = Image.open("subway.jpg")
img12 = img12.resize((600, 600)) 

stillImage12=ImageTk.PhotoImage(img12)
imageHolder12=Label(recommendGUI, image=stillImage12)

urllib.request.urlretrieve(
          'https://d18mqtxkrsjgmh.cloudfront.net/public/2021-03/Eating%20More%20Ultraprocessed%20%E2%80%98Junk%E2%80%99%20Food%20Linked%20to%20Higher%20CVD%20Risk.jpeg',
           "amazing.jpg")

img13 = Image.open("amazing.jpg")
img13 = img13.resize((600, 600)) 

stillImage13=ImageTk.PhotoImage(img13)
imageHolder13=Label(recommendGUI, image=stillImage13)

stillImage14=ImageTk.PhotoImage(imgtest)
imageHolder14=Label(recommendGUI, image=stillImage14)

urllib.request.urlretrieve(
          'https://i.pinimg.com/originals/10/b2/f6/10b2f6d95195994fca386842dae53bb2.png',
           "load.png")

imgFin = Image.open("load.png")
imgFin = imgFin.resize((600, 600)) 

stillImageFin=ImageTk.PhotoImage(imgFin)
imageHolderFin=Label(recommendGUI, image=stillImageFin)

urllib.request.urlretrieve(
          'https://images-na.ssl-images-amazon.com/images/I/61BTSwXdIHL.png',
           "white.png")

imgWh = Image.open("white.png")
imgWh = imgWh.resize((600, 600)) 

stillImageWh=ImageTk.PhotoImage(imgWh)
imageHolderWh=Label(recommendGUI, image=stillImageWh)

#THE OMOR

#first row
buttonOne=Button(recommendGUI, text="      1      ", command=pickOne).place(x=75,y=650)
buttonTwo=Button(recommendGUI, text="      2      ", command=pickTwo).place(x=175,y=650)
buttonThree=Button(recommendGUI, text="      3      ", command=pickThree).place(x=275,y=650)
buttonFour=Button(recommendGUI, text="      4      ", command=pickFour).place(x=375,y=650)
buttonFive=Button(recommendGUI, text="      5      ", command=pickFive).place(x=475,y=650)

#second row
buttonSix=Button(recommendGUI, text="      6      ", command=pickSix).place(x=75,y=700)
buttonSeven=Button(recommendGUI, text="      7      ", command=pickSeven).place(x=175,y=700)
buttonEight=Button(recommendGUI, text="      8      ", command=pickEight).place(x=275,y=700)
buttonNine=Button(recommendGUI, text="      9      ", command=pickNine).place(x=375,y=700)
buttonTen=Button(recommendGUI, text="     10     ", command=pickTen).place(x=475,y=700)


#Handles closing of the window so the thread doesn't last forever
#If the thread doesn't have the time to die, it causes the camera to stop working
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        """
        #Stop thread loop
        stop_thread = True
        t1.stop()
        t1.join(timeout=5)
        
        #Give thread 5 seconds to die
        #MAKE SURE THIS TIME IS LARGER THAN THE TIME INTERVAL BETWEEN LIVE IMAGE CAPTURES
        #sleep(5)
        
        #Note: it seens like the camera can still occasioanlly crash even with this
        #safeguard for killing the thread in place. If the camera seems to randomly
        #stop working, restart the Pi.
        
        #Close window & serial connection
        ser.close()
        """
        recommendGUI.destroy()

#Handles window-closing event so thread has time to die
recommendGUI.protocol("WM_DELETE_WINDOW", on_closing)


#initialize the window
recommendGUI.wm_attributes("-transparentcolor", 'grey')
recommendGUI.mainloop()
