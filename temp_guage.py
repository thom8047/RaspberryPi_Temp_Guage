import subprocess
import time

def checkTemp():
    return subprocess.getstatusoutput('vcgencmd measure_temp') 

def main():
    while (True):
        print(time.time())
        err, temp = checkTemp()
        if not(err):
            print(temp);
        time.sleep(1)

if __name__ == '__main__':
    main();
