import subprocess
from time import sleep

def checkTemp():
    val = subprocess.Popen(["/opt/vc/bin/vcgencmd", "measure_temp"], stdout=subprocess.PIPE)
    return val

def main():
    temp = checkTemp()
    print(temp);

if __name__ == '__main__':
    main();
