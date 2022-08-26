import os.path, string
from os import path
#from cryptography.fernet import Fernet
target_folder1 = "Secret"
start_dir = ""
target_dir = []
dirs = []
alphabet = list(string.ascii_lowercase)

#Take all alphabet letters and test if such directory exists
#If so save dir letter to list and print dir path letter



for letter in alphabet:
    start_dir = letter



    if path.exists("%s:\\" %(start_dir)):
        print('%s:\\ ----> !!!Exists!!! \n' %(start_dir))
        target_dir.append(start_dir)
    else:
        print('%s:\\ ----> !!!Does not Exists!!! \n' %(start_dir))
# prints letters of available disks
for dick in target_dir:
     print("%s \n" %(dick))
        

#Check if folder exists in all known paths
for DIR in target_dir:
    for stuff in os.listdir("%s:\\" %(DIR)):
        if os.path.isdir('%s:\\%s' %(DIR,stuff)):

            print('%s:\\%s (Directory)\n' %(DIR.upper(),stuff))

            #check for permisions of directories
            if os.access('%s:\\%s' %(DIR, stuff), os.R_OK & os.X_OK):
            
                try:
                    for content in os.listdir('%s:\\%s\\' %(DIR, stuff)):
                        if os.path.isdir('%s:\\%s\\%s' %(DIR, stuff, content)):

                            print("    %s (Directory)" %(content))
                        else:
                            print("    %s (File)" %(content))

                except IOError:
                    print("%s:\\%s\\%s (Directory | No Permissions)" %(DIR, stuff, content))

            else:
                print("%s:\\%s\\%s (Directory | No Permissions)" %(DIR, stuff, content))

        else:
            print("%s:\\%s (File)\n" %(DIR.upper(),stuff))















#key = Fernet.generate_key()

'''
for a in os.listdir(""):
    print(a + "\n")
'''
