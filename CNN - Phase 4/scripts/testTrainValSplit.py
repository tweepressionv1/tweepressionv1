import os
import random


# Paths to Folders
pathtest = "../data/test/"
pathtrain = "../data/train/"
pathval = "../data/val/"

pathreg = "../data/reg/"
pathdep = "../data/dep/"

# Train - tr, Test - te, Val - v
# Reg - r, Dep - d


# Initializing Counts
trr = 0
trd = 0
ter = 0
ted = 0
vr = 0
vd = 0

def fourDigString(num):
    if(num < 10):
        return "000" + str(num)
    if(num < 100):
        return "00" + str(num)
    if(num < 1000):
        return "0" + str(num)
    return str(num)

os.system("ls -1 " + pathdep + "> dep.txt")
with open("dep.txt","r") as depReader:
    content = depReader.readlines()
    for i in range(len(content)):
#    for i in range(50):
        print(content[i][:-1])
        if(content[i][-4:] == "jpg\n"):
            filename = content[i][:-1]
            randnum = random.randint(1,100)
            if(randnum <= 60):
                trd += 1
                stringdig = fourDigString(trd)
                newfilename = stringdig + "dep.jpg"
                os.system("cp " + pathdep + filename + " " + pathtrain + "/dep/" + newfilename)
            if(randnum <= 80 and randnum > 60):
                vd += 1
                stringdig = fourDigString(vd)
                newfilename = stringdig + "dep.jpg"
                os.system("cp " + pathdep + filename + " " + pathval + "/dep/" + newfilename)
            if(randnum > 80):
                ted += 1
                stringdig = fourDigString(ted)
                newfilename = stringdig + "dep.jpg"
                os.system("cp " + pathdep + filename + " " + pathtest + "/dep/" + newfilename)



os.system("ls -1 " + pathreg + "> reg.txt")
with open("reg.txt","r") as regReader:
    content = regReader.readlines()
    for i in range(len(content)):
        if(content[i][-4:] == "jpg\n"):
            filename = content[i][:-1]
            randnum = random.randint(1,100)
            if(randnum <= 60):
                trr += 1
                stringdig = fourDigString(trr)
                newfilename = stringdig + "reg.jpg"
                os.system("cp " + pathreg + filename + " " + pathtrain + "/reg/" + newfilename)
            if(randnum <= 80 and randnum > 60):
                vr += 1
                stringdig = fourDigString(vr)
                newfilename = stringdig + "reg.jpg"
                os.system("cp " + pathreg + filename + " " + pathval + "/reg/" + newfilename)
            if(randnum > 80):
                ter += 1
                stringdig = fourDigString(ter)
                newfilename = stringdig + "reg.jpg"
                os.system("cp " + pathreg + filename + " " + pathtest + "/reg/" + newfilename)
