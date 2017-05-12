# sort.py
#
# May 11th, 2017
# dayliver
#
# Try various sort algorithms and compare them.

import random, time, os

#methods = ['Bubble', 'Cocktail', 'Insertion', 'Selection', 'Bidirectional']
methods = ['Cocktail']

def Bubble(list):
    data = list[:]
    for i in range(len(data)):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def Cocktail(list):
    data = list[:]
    i = -1
    j = len(data)-1
    while i < j:
        i+=1
        for k in range(i,j):
            if data[k] > data[k+1]:
                data[k], data[k+1] = data[k+1], data[k]
        j-=1
        for k in range(j,i,-1):
            if data[k-1] > data[k]:
                data[k-1], data[k] = data[k], data[k-1]
    return data

def testAllMethods():
    times = []
    for method in methods:
        start = time.time()
        eval(method + '(list)')
        times.append(time.time()-start)
    for i in range(len(methods)):
        print("\n" + methods[i])
        print("%f seconds (%f)" % (times[i], times[i]/times[0]*100))
        

def generateList(number):
    start = time.time()
    list = range(number)
    for count in range(number):
        # previous code: i = random.randrange(number)
        # but it causes 0 and the final number to be unsorted.
        i = count
        j = random.randrange(number)
        list[i], list[j] = list[j], list[i]
    end = time.time() - start
    return list, end, number

os.system("cls")

number = int(raw_input("How many items do you want to generate? "))

if number < 1000:
    number = 1000

result = generateList(number)
list = result[0]
print("\nIt takes %f seconds to generate the list of %d items." % (result[1], result[2]))

testAllMethods()


raw_input()