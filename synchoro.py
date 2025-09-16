import threading

def factorial(n):
    lck.acquire()
    p= 0
    if n !=0:
        t = threading.current_thread()
        p = n * factorial(n -1)
        print(t.name, ":", n, "! =", p)
    else:
        p = 1
        lck.release()
        return p
    lck = threading.RLock()
    th1 = threading.Thread(target=factorial,args=(4,))
    th2 = threading.Thread(target=factorial,args= (6,))
    th1.startO()
    th2.start()
    th1.join()
    th2.join()
