from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == "__main__":
    t1 = time.time()
    p = Pool()
    result = p.map(f, range(100000))
    p.close()
    p.join()

    print("Pool took " + str(time.time()-t1))
    
    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(f(x))

    print("without Pool took " + str(time.time()-t2))




'''
Output:
Pool took 1.9169321060180664
without Pool took 5.701380968093872

'''