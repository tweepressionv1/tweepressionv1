import os
import multiprocessing
import time
def doMed(path,name,dig,j):
	"""
	This method uses the med2image function for parsing .nii files to .jpg images
	The associated code can be found at https://github.com/FNNDSC/med2image
	"""
	os.system("med2image -i " + path + "/" + name[:-1] + " -s -1 -f -1 -o " + dig + "" + str(j) + ".jpg > trash.txt")
                
				
for i in range(1,20):
    dig = ""
    if i < 10:
        dig = "0" + str(i);
    else:
        dig = str(i);
    folderName = "sub-mdd" + dig
    print(folderName)
    #path is ../depMRI/{folderName}/func to get to the .nii's
    path = "../depMRI/" + folderName + "/func"
    os.system("ls " + path + " > "+ folderName + ".txt")
    with open(folderName + ".txt",'r') as f:
        content = f.readlines()
        for j in range(len(content)):
            name = content[j]
            print(name[:-1])
            if(name[-3:] == "ii\n"):
				# The med2image program has a bug where it doesn't stop, but it does finish. Thus we let it take 5 seconds (more than enough to parse) and then stop the command.
                p = multiprocessing.Process(target=doMed,name="doMed",args=(path,name,dig,j,))
                p.start()
                time.sleep(5)
                if p.is_alive():
                    p.terminate()
                p.join()
                time.sleep(5)
                os.system("mv *.jpg ../data/dep")
                os.system("rm *.jpg")	
				
				
"""				
for i in range(1,21):
    dig = ""
    if i < 10:
        dig = "0" + str(i);
    else:
        dig = str(i);
    folderName = "sub-control" + dig
    print(folderName)
    #path is ../regMRI/{folderName}/func to get to the .nii's
    path = "../regMRI/" + folderName + "/func"
    os.system("ls " + path + " > "+ folderName + ".txt")
    with open(folderName + ".txt",'r') as f:
        content = f.readlines()
        for j in range(len(content)):
            name = content[j]
            print(name[:-1])
            if(name[-3:] == "ii\n"):
                p = multiprocessing.Process(target=doMed,name="doMed",args=(path,name,dig,j,))
                p.start()
                time.sleep(5)
                if p.is_alive():
                    p.terminate()
                p.join()
                time.sleep(5)
                os.system("mv *.jpg ../data/reg")
                os.system("rm *.jpg")
"""
