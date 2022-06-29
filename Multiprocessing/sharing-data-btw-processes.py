import multiprocessing

def calc_square(numbers, result, v):
    v.value = 5
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i',3)  # Data will be shared using this array
    v = multiprocessing.Value('d', 0) # Values are defined like this 
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v))

    p.start()
    p.join()

    print(result[:])
    print(v.value)



'''
Output:
[4, 9, 25]
5.0

'''