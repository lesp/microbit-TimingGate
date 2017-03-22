from microbit import *
while True:
    if pin0.read_digital() == 0:
        start_time = running_time()
    elif pin1.read_digital() == 0:
        end_time = running_time()
        race_time = (end_time - start_time) / 1000
        print(race_time)
        sleep(500)