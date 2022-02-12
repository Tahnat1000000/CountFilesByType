import os, time

dir_path = os.path.dirname(os.path.abspath(__file__))
filestype = []
typecounter = []

for root, dirs, files in os.walk(dir_path):
    if root is dir_path:
        for file in files:
            filetype = file.split(".")[len(file.split("."))-1]
            if not filestype.__contains__(filetype):
                filestype.append(filetype)
                typecounter.append(filetype)
                typecounter.append(1)
            else:
                typecounter[typecounter.index(filetype)+1] += 1

for index in range(len(typecounter))[::2]:
    print(typecounter[index] + ": " + str(typecounter[index+1]))


time.sleep(30)