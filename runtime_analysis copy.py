import random as rd
import time as time

### Bubble Sort ###

def bubble_sort(arr):
    # create Flag, if it is false, a swap didnt occur and therefore the while loop can end
    swap_happened = True
    # we use len -1 because we dont need to compare the last element to anything
    while swap_happened:
        swap_happened = False
        for num in range(len(arr) -1):
            if arr[num] > arr[num+1]:
            # dynamically change the values of the array items 
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]


### Quicksort ###

def quicksort(arr):

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num  == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)


### Merge Sort ###

def merge_sort(arr1, arr2):
    sorted_arr = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        # print(f"Left index i is {i} and has value {arr1[i]}")
        # print(f"Right index j is {j} and has value {arr2[j]}")
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    # why not this?
    """ if i  == len(arr1):
        sorted_arr.extend(arr2[j:])
    elif j == len(arr2):
        sorted_arr.extend(arr1[i:])
    else:
        return sorted_arr """
        
    return sorted_arr

def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sort(l1, l2)


### Select Sort ###

def sel_sort(arr):
    counter = 0
    while counter < len(arr):
        for num in range(counter, len(arr)):
            if arr[num] < arr[counter]:
                arr[counter], arr[num] = arr[num], arr[counter]
        counter += 1
    

def run_funcs(func, arr):
    tic = time.time()
    func(arr)
    toc = time.time()
    seconds = toc - tic
    print (f"{func.__name__.capitalize()}\t-> Elapsed Time: {seconds:.5f}\n")

while True:
    size = int(input('What size list would you like to create? ' ))
    range_max = int(input('What is the max value of the range? '))
    num_of_runs = int(input('How many times should it run? '))
    l = [rd.randint(1, range_max) for x in range(size)]

    # passing in func obj NOT calling it

    
    for num in range(num_of_runs):
        '''run each function with l 
            measure the time it takes to run each
            print the times'''
        print(f'\nRun {num+1}')
        print('-'*40)
        run_funcs(quicksort, l)
        run_funcs(mergesort, l)
        run_funcs(bubble_sort, l.copy()) # sorts in place AKA changes the original arr. HAVE to use .copy() when using funcs that run in place
        run_funcs(sel_sort, l.copy())
    break
      
 
