#   Features:
#   1.Already suggested movie will not suggest again
#   2.Only run mp4 or mkv file
#   3.Can run movie automatically
import os, random, time

movies_path = os.getcwd() #path of folder where all movies are stored
check = True
choice = False
selected_index = []
error_msg = "Sorry unable to find any other movie"

#function to select movie
def movieSelector(path):
    os.chdir(path)
    movies_list = os.listdir()
    number_of_movies = len(movies_list)
    
    if (number_of_movies == len(selected_index)):
        return error_msg
    
    while True:
        selected_movie = random.randrange(0, number_of_movies)
        if (selected_movie in selected_index):
            continue
        else:
            break
    
    name = movies_list[selected_movie]
    if (not (checkType(name))):
        #it is file
        if (not (checkExt(name))):
            #recursion
            name = movieSelector(path)
    
    if (not (selected_movie in selected_index)):
        selected_index.append(selected_movie)
    
    return name

#function to check that selected name is a file or directory
def checkType(selected_name):
    if (os.path.isdir(selected_name)):
        result = True
    elif (os.path.isfile(selected_name)):
        result = False
    return result

#function to check extension
def checkExt(selected_name):
    fileextension = os.path.splitext(selected_name)[1]
    if (fileextension == ".mp4" or fileextension == ".mkv"):
        result = True
    else:
        result = False
    
    return result
    
    
#function to start the movie
def startMovie(selected_name):
    if (selected_name != error_msg):
        if (checkType(selected_name)):
            os.chdir(selected_name)
            files = os.listdir()
            subfiles = len(files)
            for x in range(0, subfiles):
                if (checkExt(files[x])):
                    print("Playing " + files[x])
                    os.system(".\\" + "\"" + files[x] + "\"")
                    break
        else:
            if (checkExt(selected_name)):
                print("Playing " + selected_name)
                os.system(".\\" + "\"" + selected_name + "\"")
    else:
        print(error_msg)

#Actual execution start here
print("Hi! I am here to help you in picking up the movie")
input("Press any key so that I can start helping right now")

while check:
    print("Getting Movies Name")
    time.sleep(2)
    print("Selecting the Movie")
    time.sleep(2)
    print("Movie Selected")
    print("***")
    name = movieSelector(movies_path)
    print(name)
    print("***")
    print("Enjoy your time. I\'m pleased to help you")
    
    ans = input("Do you want me to start the movie press Y/y: ")
    if (ans == 'Y' or ans == 'y'):
        startMovie(name)
        
    letter = input("To Shutdown Press n/N or To run again press any key: ")
    if (letter == 'n' or letter == 'N'):
        check = False
