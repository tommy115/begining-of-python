import multiprocessing
import os

def do_this(what):
    whoami(what)

def whoami(what):
    print("process %s says: %s" % (os.getpid(), what))
    
if __name__ == '__main__':
    whoami("I'm main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this,
                                    args = ("I'm function %s" % n, ))
        p.start()

