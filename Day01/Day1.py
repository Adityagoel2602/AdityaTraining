import os

os.mkdir('VIPS')
os.chdir('VIPS')
for i in range(21):
    os.mkdir("Participants_"+str(i))
    os.chdir("Participants_"+str(i))
    for j in range(20):
        os.mkdir("Day_"+str(j))
    os.chdir("../")
