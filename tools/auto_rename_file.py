#自動rename file 內的名字
import os


strDir=os.getcwd()+"/data/img/fall"
listFiles=os.listdir(strDir)
listFiles.sort()


for filename in listFiles:
    index = 1
    listFiles2 = os.listdir(strDir + "/"+filename)
    listFiles2.sort()
    
    for filename2 in listFiles2:

        strOldName=strDir + "/"+filename+"/"+filename2
        strNewName=strDir + "/"+filename+"/"+"%05d"%index+".jpg"
        print(strOldName,",",strNewName)
        index+=1
        os.rename(strOldName,strNewName)
