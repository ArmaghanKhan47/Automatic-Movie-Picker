import os, random, time

movies_path = os.getcwd() #path of folder where all movies are stored
check = True
choice = False

#function to select movie
def movieSelector(path):
    os.chdir(path)
    movies_list = os.listdir()
    number_of_movies = len(movies_list)
    
    selected_movie = random.randrange(0, number_of_movies)
    return movies_list[selected_movie]

#function to check that selected name is a file or directory
def checkType(selected_name):
    if (os.path.isdir(selected_name)):
        result = True
    elif (os.path.isfile(selected_name)):
        result = False
    return result

#function to start the movie
def startMovie(selected_name):
    file_type = checkType(selected_name)
    
    if (file_type):
        os.chdir(selected_name)
        files = os.listdir()
        subfiles = len(files)
        for x in range(0, subfiles):
            fileextension = os.path.splitext(files[x])[1]
            if (fileextension == ".mp4" or fileextension == ".mkv"):
                os.system(".\\" + "\"" + files[x] + "\"")
                os.system("exit")
                break
    else:
        fileextension = os.path.splitext(selected_name)[1]
        if (fileextension == ".mp4" or fileextension == ".mkv"):
            os.system(".\\" + "\"" + selected_name + "\"")

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
