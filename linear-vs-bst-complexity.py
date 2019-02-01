import random
from timeit import Timer

def main():
#LINEAR
        #timing list 1k entries long with linear search
        list1 = [random.randrange(2, 1000001, 2) for _ in range(1000)]#create list using randrange(2, 1000001, 2) which makes creates a list of random even numbers between 2 and 1000001.
        S1 = [random.choice(list1), random.choice(list1), random.choice(list1), random.choice(list1), random.choice(list1), 101, 2001, 30001, 40001, 500001]#search list created by randomly selecting 5 numbers from the list to be sorted
        S12 = [None]*100 #search list of length 100 created by a for loop
        for x in range(0, 100):
                if x < 50:
                        S12[x] = random.choice(list1)#contains elements of list 1
                else:
                        S12[x] = random.randrange(1, 1000000+1, 2)
        S13 = [None]*1000#search list of length 1000 created by a for loop
        for x in range(0, 1000):
                if x < 500:
                        S13[x] = random.choice(list1)
                else:
                      S13[x] = random.choice(list1)+1
        sum = 0
        for x in range(0,10): #for loop to check every number in the S array if it's in the list array
                t = Timer(lambda: linearSearch(list1,S1[x]))#times linear search of xth element of S1
                sum += t.timeit(number=1) #adds time together
        print("Linear 1k time, 10 searches: ", end="")
        print(sum/10) #divide time by 10 to average
        sum = 0
        for x in range(0,100): #for loop to check every number in the S array if it's in the list array
                t = Timer(lambda: linearSearch(list1,S12[x]))#times linear search of xth element of S1
                sum += t.timeit(number=1) #adds time together
        print("Linear 1k time, 100 searches: ", end="")
        print(sum) 
        sum = 0
        for x in range(0,1000): #for loop to check every number in the S array if it's in the list array
                t = Timer(lambda: linearSearch(list1,S13[x]))#times linear search of xth element of S1
                sum += t.timeit(number=1) #adds time together
        print("Linear 1k time, 1000 searches: ", end="")
        print(sum) 
                                                                                                                                                            

        #timing list 2k entries long with linear search
        list2 = [random.randrange(2, 1000001, 2) for _ in range(2000)]
        S2 = [random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), random.choice(list2), 101, 2001, 30001, 40001, 500001]
        S22 = [None]*100
        for x in range(0, 100):
                if x < 50:
                        S22[x] = random.choice(list2)
                else:
                        S22[x] = random.choice(list1)+1
        S23 = [None]*1000
        for x in range(0, 1000):
                if x < 500:
                        S23[x] = random.choice(list2)
                else:
                        S23[x] = random.choice(list1)+1
                        
        sum = 0
        for x in range(0,10):
                t = Timer(lambda: linearSearch(list2,S2[x]))
                sum += t.timeit(number=1)
        print("Linear 2k time, 10 searches: ", end="")
        print(sum)

        sum = 0
        for x in range(0,100):
                t = Timer(lambda: linearSearch(list2,S22[x]))
                sum += t.timeit(number=1)
        print("Linear 2k time, 100 searches: ", end="")
        print(sum)

        sum = 0
        for x in range(0,1000):
                t = Timer(lambda: linearSearch(list2,S23[x]))
                sum += t.timeit(number=1)
        print("Linear 2k time, 1000 searches: ", end="")
        print(sum)

	#timing list 5k entries long with linear search
        list3 = [random.randrange(2, 1000001, 2) for _ in range(5000)]
        S3 = [random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), random.choice(list3), 101, 2001, 30001, 40001, 500001] 
        S32 = [None]*100
        for x in range(0, 100):
                if x < 50:
                        S32[x] = random.choice(list3)
                else:
                        S32[x] = random.choice(list1)+1
        S33 = [None]*1000
        for x in range(0, 1000):
                if x < 500:
                        S33[x] = random.choice(list3)
                else:
                        S33[x] = random.choice(list1)+1
        sum = 0
        for x in range(0,10):
                t = Timer(lambda: linearSearch(list3,S3[x]))
                sum += t.timeit(number=1)
        print("Linear 5k time, 10 searches: ", end="")
        print(sum)

        sum = 0
        for x in range(0,100):
                t = Timer(lambda: linearSearch(list3,S32[x]))
                sum += t.timeit(number=1)
        print("Linear 5k time, 100 searches: ", end="")
        print(sum)

        sum = 0
        for x in range(0,1000):
                t = Timer(lambda: linearSearch(list3,S33[x]))
                sum += t.timeit(number=1)
        print("Linear 5k time, 1000 searches: ", end="")
        print(sum)
        
	#timing list 10k entries long with linear search
        list4 = [random.randrange(2, 1000001, 2) for _ in range(10000)]
        S4 = [random.choice(list4), random.choice(list4), random.choice(list4), random.choice(list4), random.choice(list4), 101, 2001, 30001, 40001, 500001]
        S42 = [None]*100
        for x in range(0, 100):
                if x < 50:
                        S42[x] = random.choice(list4)
                else:
                        S42[x] = random.randrange(1, 1000000+1, 2)
        S43 = [None]*1000
        for x in range(0, 1000):
                if x < 500:
                        S43[x] = random.choice(list4)
                else:
                        S43[x] = random.randrange(1, 1000000+1, 2)
                        
        sum = 0
        for x in range(0,10):
                t = Timer(lambda: linearSearch(list4,S4[x]))
                sum += t.timeit(number=1)
        print("Linear 10k time, 10 searches: ", end="") 
        print(sum)

        sum = 0
        for x in range(0,100):
                t = Timer(lambda: linearSearch(list4,S42[x]))
                sum += t.timeit(number=1)
        print("Linear 10k time, 100 searches: ", end="")
        print(sum)

        sum = 0
        for x in range(0,1000):
                t = Timer(lambda: linearSearch(list4,S43[x]))
                sum += t.timeit(number=1)
        print("Linear 10k time, 1000 searches: ", end="")
        print(sum)

        
#BINARY
        #timing list 1k entries long with binary search 
        p = Timer(lambda: sort(list1))
        #must time how long it takes to sort the list
        sortTime = p.timeit(number=1)
        
        sum = 0
        for x in range(0,10):
                t = Timer(lambda: binarySearch(list1,S1[x]))
                sum += t.timeit(number=1)
        print("Binary 1k time, 10 searches: ", end="")
        print((sum)+sortTime)

        sum = 0
        for x in range(0,100):
                t = Timer(lambda: binarySearch(list1,S12[x]))
                sum += t.timeit(number=1)
        print("Binary 1k time, 100 searches: ", end="")
        print((sum)+sortTime)

        sum = 0
        for x in range(0,1000):
                t = Timer(lambda: binarySearch(list1,S13[x]))
                sum += t.timeit(number=1)
        print("Binary 1k time, 1000 searches: ", end="")
        print((sum)+sortTime)
        
        print("Sort Time: ", end="")
        print(sortTime)

	#timing list 2k entries long with binary search 
        p = Timer(lambda: sort(list2))
        sortTime = p.timeit(number=1)
        sum = 0
        for x in range(0,10):
                t = Timer(lambda: binarySearch(list2,S2[x]))
                sum += t.timeit(number=1)
        print("Binary 2k time, 10 searches: ", end="")
        print((sum)+sortTime)

        sum = 0
        for x in range(0,100):
                t = Timer(lambda: binarySearch(list2,S22[x]))
                sum += t.timeit(number=1)
        print("Binary 2k time, 100 searches: ", end="")
        print((sum)+sortTime)

        sum = 0
        for x in range(0,1000):
                t = Timer(lambda: binarySearch(list2,S23[x]))
                sum += t.timeit(number=1)
        print("Binary 2k time, 1000 searches: ", end="")
        print((sum)+sortTime)
        print("Sort Time: ", end="")
        print(sortTime)

	#timing list 5k entries long with binary search 
        p = Timer(lambda: sort(list3))
        sortTime = p.timeit(number=1)
        sum = 0
        for x in range(0,10):
                t = Timer(lambda: binarySearch(list3,S3[x]))
                sum += t.timeit(number=1)
        print("Binary 5k time, 10 searches: ", end="")
        print((sum)+sortTime)

        sum = 0
        for x in range(0,100):
                t = Timer(lambda: binarySearch(list3,S32[x]))
                sum += t.timeit(number=1)
        print("Binary 5k time, 100 searches: ", end="")
        print((sum)+sortTime)

        sum = 0
        for x in range(0,1000):
                t = Timer(lambda: binarySearch(list3,S33[x]))
                sum += t.timeit(number=1)
        print("Binary 5k time, 1000 searches: ", end="")
        print((sum)+sortTime)
        
        print("Sort Time: ", end="")
        print(sortTime)

	#timing list 10k entries long with binary search 
        p = Timer(lambda: sort(list4))
        sortTime = p.timeit(number=1)
        sum = 0
        for x in range(0,10):
                t = Timer(lambda: binarySearch(list4,S4[x]))
                sum += t.timeit(number=1)
        print("Binary 10k time, 10 searches: ", end="")
        print((sum)+sortTime)
        
        sum = 0
        for x in range(0,100):
                t = Timer(lambda: binarySearch(list4,S42[x]))
                sum += t.timeit(number=1)
        print("Binary 10k time, 100 searches: ", end="")
        print((sum)+sortTime)
        
        sum = 0
        for x in range(0,1000):
                t = Timer(lambda: binarySearch(list4,S43[x]))
                sum += t.timeit(number=1)
        print("Binary 10k time, 1000 searches: ", end="")
        print((sum)+sortTime)
        
        print("Sort Time: ", end="")
        print(sortTime)
	
	
	
def sort(list):
        #using python built in to sort
        list.sort()
        
# a function to perform binary search
def binarySearch(lst, target):   
        min = 0
        max = len(lst)-1
        avg = (min+max)//2
  # uncomment next line for traces
  # print lst, target, avg  
        while (min < max):
                if (lst[avg] == target):
                        return avg
                elif (lst[avg] < target):
                        return avg + 1 + binarySearch(lst[avg+1:], target)
                else:
                        return binarySearch(lst[:avg], target)
        return avg
# a function to perform linear search
def linearSearch(array, target):
        found = False
        position = 0
        while position < len(array):
                if array[position] == target:
                        found = True
                        break
                position = position + 1
        return found
	
if __name__=='__main__':
	main()
    
