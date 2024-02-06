import re

def remove_railway_station():
    with open("railways.txt", "r") as file1:
        lines = file1.readlines()
    with open("railways_new.txt", "w") as file:
        for line in lines:
            #Checks if line is more than 1 character long
            if len(line) > 2:
               file.write(re.sub(r"railway station", "", line))

def make_railway_a_list():
    with open("stations.txt", "r") as file:
        lines = file.readlines()
    with open("railways_new.txt", "w") as file:
        for line in lines:
            file.write(line.replace(" \n", "\",\""))


make_railway_a_list()