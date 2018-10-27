import os
from multiprocessing import Process, Pipe
from time import sleep

def ponger(p, s):
    count = 0
    while count < 10:
        msg = p.recv()
        print('Process {} for message {}'.format(os.getpid(), msg))
        sleep(.5)
        p.send(s)
        count += 1

if __name__ == '__main__':
    # a tuple of connection. first is input end, second object is output end
    # parent object --> ]=======================[ --> child object
    parent, child = Pipe()
    proc = Process(target=ponger, args=(child, 'ping'))
    # parent process runs in original python process
    # child process runs in its own new python process
    proc.start()
    parent.send('pong')
    ponger(parent, 'pong')
    proc.join()
