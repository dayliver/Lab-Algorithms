# sort.py
#
# May 11th, 2017
# dayliver
#
# Try various sort algorithms and compare them.

import random, time, os, math, random

#methods = ['Bubble', 'Cocktail', 'Insertion', 'Selection', 'Bidirectional']
methods = ['Bubble', 'Cocktail', 'Cocktail_improved', 'Cocktail_wikibooks', 'Selection', 'Selection_bidirectional', 'Insertion', 'Heap', 'Quick', 'Python']

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
	
def Cocktail_improved(list):
	data = list[:]
	i = 0
	j = len(data)-1
	while i < j:
		for k in range(i, j+1):
			if data[k] < data[i]:
				data[i], data[k] = data[k], data[i]
			elif data[k] > data[j]:
				data[j], data[k] = data[k], data[j]
		i += 1
		j -= 1
	return data
	
def Cocktail_wikibooks(list): # https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Cocktail_sort
	data = list[:]
	for k in range(len(data)-1, 0, -1):
		swdatapped = False
		for i in range(k, 0, -1):
			if data[i]<data[i-1]:
				data[i], data[i-1] = data[i-1], data[i]
				swdatapped = True
		for i in range(k):
			if data[i] > data[i+1]:
				data[i], data[i+1] = data[i+1], data[i]
				swdatapped = True
		if not swdatapped:
			return data

def Selection(list):
	data = list[:]
	for i in range(len(data)):
		min_index = i
		for j in range(i+1, len(data)):
			if data[min_index] > data[j]:
				min_index = j
		data[i], data[min_index] = data[min_index], data[i]
	return data

def Selection_bidirectional(list):
	data = list[:]
	i = 0
	j = len(data)-1
	while i < j:
		if data[i] > data[j]:
			data[i], data[j] = data[j], data[i]
		min_index = i
		max_index = j
		for k in range(i+1, j):
			if data[k] < data[min_index]:
				min_index = k
			if data[k] > data[max_index]:
				max_index = k
		data[i], data[min_index] = data[min_index], data[i]
		data[j], data[max_index] = data[max_index], data[j]
		i += 1
		j -= 1
	return data
	
def Insertion(list):
	data = list[:]
	for i in range(1, len(data)):
		k = i
		for j in range(i, -1, -1):
			if data[k] < data[j]:
				data[k], data[j] = data[j], data[k]
				k = j
	return data

def Quick(list):
    data = [list[:]]
    length = len(list)
    while len(data) < length:
        for i in range(len(data)):
            pivot = data[i][len(data[i]) // 2]
            parts = [[],[],[]]
            for element in data[i]:
                if element < pivot:
                    parts[0].append(element)
                elif element == pivot:
                    parts[1].append(element)
                else:
                    parts[2].append(element)
            for j in range(2,-1,-1):
                if len(parts[j]) == 0:
                    del parts[j]
            data[i:i+1] = parts
    for i in range(length):
        data[i] = data[i][0]
    return data

def Python(list):
    data = list[:]
    data.sort()
    return data

def swap(idx1, idx2):
    temp = nodes[idx1].value
    nodes[idx1].value = nodes[idx2].value
    nodes[idx2].value = temp
    
def minChild(idx1, idx2):
    if len(nodes) <= idx2 or nodes[idx2].value == None or nodes[idx1].value <= nodes[idx2].value:
        return idx1
    else:
        return idx2
    
def countChildren(idx):
    noc = 0
    for c in nodes[idx].children:
        try:
            if nodes[c].value != None:
                noc += 1
        except:
            pass
    #print idx, nodes[idx].value, noc
    return noc

def Heap(list):
    for i in range(len(list)):
        nodes.append(node(list[i]))
        nodes[i].compUp()
    data = []
    for n in nodes:
        if nodes[0].value == None:
            break
        data.append(nodes[0].value)
        nodes[0].value = None
        nodes[0].fill()
    return data

class node:
    def __init__(self, value):
        self.value = value
        parts = []
        self.idx = len(nodes)
        if self.idx == 0:
            self.parent = -1
            self.children = [1, 2]
        else:
            idx = self.idx
            lv = int(math.log(idx+1,2))
            for i in range(lv, 1, -1):
                if idx >= 2**i + 2**(i-1) - 1:
                    parts.insert(0,2)
                    idx -= 2**i
                else:
                    parts.insert(0,1)
                    idx -= 2**(i-1)
            parts.insert(0,idx)
            p = 0
            c = 0
            m = 0
            for i in parts:
                c += 2 ** (m+1) * i
                if m > 0:
                    p += 2 ** (m-1) * i
                m += 1
            self.parent = p
            self.children = [c+1, c+2]
        
    def compUp(self):
        idx = self.idx
        while nodes[idx].parent > -1:
            if nodes[idx].value < nodes[nodes[idx].parent].value:
                swap(idx, nodes[idx].parent)
            idx = nodes[idx].parent
        
    def fill(self):
        idx = self.idx
        done = False
        while done == False:
            if nodes[idx].value == None:
                noc = countChildren(idx)
                if noc > 0:
                    mc = minChild(nodes[idx].children[0], nodes[idx].children[1])
                    swap(idx, mc)
                    idx = mc
                else:
                    nodes[idx].value = None
                    done = True
        
def testAllMethods():
	times = []
	results = []
    
	# Sort in each method
	for i in range(len(methods)):
		start = time.time()		
		exec('output = ' + methods[i] + '(list)')
		times.append(time.time()-start)
		# Check if sorted
		sorted = True
		for j in range(len(output)-1):
		    if output[j] > output[j+1]:
		        sorted = False
		        print("In the result of %s method, %d is larger than %d" % (methods[i], output[j], output[j+1]))
		        #break
		if sorted == True:
		    result = 'Succeeded!'
		else:
		    result = 'FAILED!!!!'
		results.append(result)
		print("\n" + methods[i] + " (" + results[i] + ")")
		print("%f seconds (Speed: %f)" % (times[i], times[0]/times[i]*100))

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

raw = generateList(number)
list = raw[0]
nodes = []
print("\nIt takes %f seconds to generate the list of %d items." % (raw[1], raw[2]))

for i in range(1):
    testAllMethods()

raw_input("\nPress enter to quit!")