import os, random, time

movies_path = os.getcwd() #path of folder where all movies are stored
check = True
choice = False

def movieSelector(path):
    os.chdir(path)
    movies_list = os.listdir()
    number_of_movies = len(movies_list)
    
    selected_movie = random.randrange(0, number_of_movies)
    return movies_list[selected_movie]

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
        choice = True
        
    if (choice == True):
       os.chdir(name)
       files = os.listdir()
       subfiles = len(files)
       for x in range(0, subfiles):
           fileextension = os.path.splitext(files[x])[1]
           if (fileextension == ".mp4"):
               os.system(".\\" + files[x])
               os.system("exit")
               break
       break    
        
    letter = input("To Shutdown Press n/N or To run again press any key: ")
    if (letter == 'n' or letter == 'N'):
        check = False