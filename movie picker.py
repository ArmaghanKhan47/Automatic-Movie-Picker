"""
Note:
    Features:
        1.Already suggested movie will not suggest again.
        2.Only run mp4 or mkv file.
        3.Can run movie automatically.
        4.Create playlist if multiple videos found in directory.
    
    Dependency:
        VLC Player must be installed in the computer and its vlc command-line tool must be working.
        
    Limitation:
        1.Only workes on Microsoft Windows.
        2.If selected directory contains subdirectories and subdirectories contains videos, this program will assume that directory doesnot contain any videos
    
    How To Set vlc command line tool:
        for vlc to work you have to create enviromental variable.
        
        VLC mostly installed in following path:
            C:\Program Files (x86)\VideoLAN\VLC
            
        Step 1:
            Right Click on 'This PC' icon -> Click on 'Propertise'.
        Step 2:
            Click on 'Advanced system setting' from left panel.
        Step 3:
            Click on 'Enviromental Variables' in 'Advanced' tab.
        Step 4:
            Double Click on 'Path' in 'User Variables for'.
        Step 5:
            Click on 'New' and copy paste the above path(line 19)
        Step 6:
            Click on 'OK' and now vlc command-line tool is set
        
"""
import os, random

movies_path = os.getcwd() #path of folder where all movies are stored
check = True
choice = False
multiple_videos = []
selected_index = []
error_msg = "Sorry unable to find any other movie"

#function to select movie
def movieSelector(path):
    os.chdir(path)
    movies_list = os.listdir()
    number_of_movies = len(movies_list)
    while True:
        if number_of_movies == len(selected_index):
            return error_msg
        while True:
            #verfing that selected index is previously selected or not
            selected_movie = random.randrange(0, number_of_movies)
            if selected_movie in selected_index:
                continue
            break
        name = movies_list[selected_movie]
        if not checkType(name):
            #it is file
            if not checkExt(name):
                #its not of suitable extension
                selected_index.append(selected_movie)
                continue
        elif not containsMovie(name):
            #it is directory and cannot contains any movie
            selected_index.append(selected_movie)
            continue
        selected_index.append(selected_movie)
        break
    return name

#function to check that selected name is a file or directory
def checkType(selected_name):
    if os.path.isdir(selected_name):
        return True
    elif os.path.isfile(selected_name):
        return False

#function to check extension
def checkExt(selected_name):
    fileextension = os.path.splitext(selected_name)[1]
    if fileextension == ".mp4" or fileextension == ".mkv":
        return True
    return False
    
#function to check that selected folder contains videos or not
def containsMovie(selected_name):
    #it assumes that selection is a directory
    os.chdir(selected_name)
    lis = os.listdir()
    for x in lis:
        if not checkType(x):
            if checkExt(x):
                return True
    return False
    
#function to start the movie
def startMovie(selected_name):
    if selected_name != error_msg:
        if checkType(selected_name):
            os.chdir(selected_name)
            files = os.listdir()
            subfiles = len(files)
            for x in range(0, subfiles):
                if checkExt(files[x]):
                    multiple_videos.append("\"" + files[x] + "\"")
            word = "vlc " + " ".join(multiple_videos)
            os.system(word)
        else:
            if checkExt(selected_name):
                print("Playing " + selected_name)
                os.system("vlc " + "\"" + selected_name + "\"")
    else:
        print(error_msg)

#Actual execution start here
print("Hi! I am here to help you in picking up the movie")
input("Press any key so that I can start helping right now")

while check:
    print("Getting Movies Name")
    print("Selecting the Movie")
    name = movieSelector(movies_path)
    print("Movie Selected")
    print("***")
    print(name)
    print("***")
    if name == error_msg:
        break
    print("Enjoy your time. I\'m pleased to help you")
    
    ans = input("Do you want me to start the movie press Y/y: ")
    if ans == 'Y' or ans == 'y':
        startMovie(name)
        
    letter = input("To Shutdown Press n/N or To run again press any key: ")
    if letter == 'n' or letter == 'N':
        check = False
