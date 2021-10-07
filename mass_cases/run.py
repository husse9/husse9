import csv
import os

submitter = "Energimarknadsinspektionen"
caseName = "HG"

with open('data.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        #print(row)
        
        strList = row
        print (strList)
        #ändrar i filen settings
        with open('create-cases.settings', 'r') as file :
            filedata = file.read()
            filedata = filedata.replace(submitter, strList[2])
            submitter = strList[2]
            #print(filedata)
        with open('create-cases.settings', 'w') as file:
            file.write(filedata)

        #ändrar i filen case.txt
        with open('case.txt', 'r') as file :
            filedata2 = file.read()
            filedata2 = filedata2.replace(caseName, strList[1])
            caseName = strList[1]
            #print(filedata)
        with open('case.txt', 'w') as file:
            file.write(filedata2)

        
        os.system("createCases.bat")



# Replace the target string

