import threading
import time

def square_number():
    for i in range(50):
        time.sleep(1)
        print(i*i)

def cube_number():
    for i in range(50):
        time.sleep(1.5)
        print(i*i*i)


#multiprocessing
t1=threading.Thread(target=square_number)
t2=threading.Thread(target=cube_number)
t=time.time()
#start
t1.start()
t2.start()

#join
t1.join()
t2.join()

#finished_time
finished_time=time.time()-t
print(finished_time)