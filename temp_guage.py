import subprocess
import time

def checkTemp():
    return subprocess.getstatusoutput('vcgencmd measure_temp') 

def main():
    while (True):
        time.sleep(1)
        
        err, temp = checkTemp()
        if not(err):
            print(time.ctime())
            print(temp);

if __name__ == '__main__':
    main();
