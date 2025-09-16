import threading

def print_num(n):
    rlck.acquire()
    
    if n != 0:
        t = threading.current_thread()
        print(t.name, ":", n)
        n -=1
        print_num(n)
    rlck.release()

rlck = threading.RLock()
th1 = threading.Thread(target=print_num, args= (8,))
th1.start()
th2 = threading. Thread(target=print_num, args=(5,))
th2.start()

th1.join()
th2.join()
