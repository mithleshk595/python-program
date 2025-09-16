import time
import threading

def printMsg(msg, lck):
    lck.acquire()
    print("msg= ")
    print(msg, end="")
    time.sleep(0.5)
    print("")
    lck.release()

lck = threading.Lock()
th1 = threading.Thread(target= printMsg,args = ("what is this life....", lck))
th1.start()

th2 = threading.Thread(target=printMsg, args=("we have no time...", lck))
th2.start()

th3 = threading.Thread(target=printMsg, args=("to stand and stare", lck))
th3.start()

th1.join()
th2.join()
th3.join()



