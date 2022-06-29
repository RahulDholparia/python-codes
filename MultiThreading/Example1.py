import time
import threading

def square(lst):
    square_arr = []
    for x in lst:
        time.sleep(0.5)
        square_arr.append(x*x)
    
    print(square_arr)

def cube(lst):
    cube_arr = []
    for x in lst:
        time.sleep(0.5)
        cube_arr.append(x*x*x)

    print(cube_arr)

arr = [1, 2, 3, 4]

t = time.time()

#square(arr)
#cube(arr)

t1= threading.Thread(target=square, args=(arr,))
t2= threading.Thread(target=cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Total time to execute : ",time.time()-t)