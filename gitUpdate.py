import os

print("Backing up old install...")
os.system("cp -r ~/pythonPiper/ ~/pyPiperOld/")
print("Clearing old install...")
os.system("rm -rf ~/pythonPiper/")
os.system("git clone http://github.com/vexxation327/pythonPiper.git")
