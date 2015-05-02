import sched, time
from threading import Timer
# bad
#s= sched.scheduler(time.time, time.sleep)
def print_time():
    print "From print_time", time.time()

def print_some_time():
    print time.time()
    Timer(5, print_time, ()).start()
    Timer(10,print_time, ()).start()
    time.sleep(11)
    print time.time()

if __name__ == '__main__':
    print_some_time()
