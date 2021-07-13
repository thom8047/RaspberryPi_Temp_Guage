import subprocess
from time import sleep

def checkTemp():
    return subprocess.getstatusoutput('vcgencmd measure_temp') 

def main():
    err, temp = checkTemp()
    if not(err):
        print(temp);

if __name__ == '__main__':
    main();
