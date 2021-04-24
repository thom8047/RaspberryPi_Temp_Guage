import subprocess
from time import sleep

def checkTemp():
    return subprocess.Popen(["/opt/vc/bin/vcgencmd", "measure_temp"], stdout=subprocess.PIPE)

def main():
    temp = checkTemp()
    print(temp);

if __name__ == '__main__':
    main();