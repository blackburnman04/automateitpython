import os
import subprocess
import distro
import platform
import lin
import win
import logging



oscheck = platform.platform()
osversion = str(oscheck)
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s')


with open('distro.txt', 'w') as file: # write results of platform module to txt file
    file.write(osversion)

with open('distro.txt') as f: # open distro.txt file and read
        found = False
        for line in f:
            if "Linux" in line: # check if Linux is in distro.txt file
                lin.load()
                found = True
                logging.info('Linux was found as your OS, loading Linux GUI');
            if "Windows" in line: # check if windows if in distro.txt file
                win.load()
                found = True
                logging.info('Windows was found as your OS, loading Windows GUI');


