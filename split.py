import random
import os
from os import listdir
import shutil
outer_path = "/Users/michaelmarsella/KanaMachine/kmnist/"
for dirc in listdir(outer_path+"/Hiragana73"):
    for i in range(200):
        pic = random.randint(1,1000)
        item = dirc + str(pic)+".png"
        filename = outer_path+"Hiragana73/"+dirc + "/" + item
        if os.path.exists(filename):
            dest_dir = outer_path+"test"+"/"+dirc
            if not os.path.isdir(dest_dir):
                os.mkdir(dest_dir)
            dest_file = dest_dir+"/"+item
            shutil.move(filename, dest_dir+"/"+item)