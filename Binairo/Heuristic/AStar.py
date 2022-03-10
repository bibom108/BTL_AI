from copy import deepcopy
from queue import PriorityQueue
import time

class Prioritize:
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item

    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

class State:
    def __init__(self, filename):
        self.filename = filename
        arr = []
        f = open(filename, "r")
        for row in f:
            tmp = [(ele) for ele in row if ele != '\n']
            arr.append(tmp)
        self.arr = arr
        self.N = len(self.arr)

    def deepcp(self):
        res = State(self.filename)
        res.arr = deepcopy(self.arr)
        res.N = deepcopy(self.N)
        return res

    def get_row(self, row):
        res = ''
        for col in range(self.N):
            res += self.arr[row][col]
        return res

    def get_col(self, col):
        res = ''
        for row in range(self.N):
            res += self.arr[row][col]
        return res
    
    def is_valid(self):
        # Check continuos character
        for row in range(self.N):
            for col in range(1,self.N-1):
                if self.arr[row][col] == 'N':
                    continue
                if self.arr[row][col-1] == self.arr[row][col] == self.arr[row][col+1]:
                    return False

        for col in range(self.N):
            for row in range(1,self.N-1):
                if self.arr[row][col] == 'N':
                    continue
                if self.arr[row-1][col] == self.arr[row][col] == self.arr[row+1][col]:
                    return False
        # Check number of black and white
        for i in range(self.N):
            if self.get_row(i).count("0") > self.N/2 or self.get_row(i).count("1") > self.N/2:
                return False
            if self.get_col(i).count("0") > self.N/2 or self.get_col(i).count("1") > self.N/2:
                return False
        # Check unique
        for i in range (self.N):
            for j in range (i):
                if self.get_row(i).count("N") == 0 and self.get_row(j).count("N") == 0 and self.get_row(i) == self.get_row(j):
                    return False
                if self.get_col(i).count("N") == 0 and self.get_col(j).count("N") == 0 and self.get_col(i) == self.get_col(j):
                    return False
        return True  

    def findNextPlace(self):
        for row in range(self.N):
            for col in range(self.N):
                if self.arr[row][col] == 'N':
                    return True,row,col
        return False,-1,-1

    def count_empty(self):
        res = 0
        for row in range(self.N):
            res += self.get_row(row).count("N")
        return res

    def display(self):
        print("")
        for row in range(self.N):
            print(self.get_row(row))
        print("")

    def produce(self):
        result = []
        res = self.deepcp()
        cur_empty_cell = res.count_empty()
        res_empty_cell = cur_empty_cell
        for row in range(self.N):
            for col in range(self.N):
                if self.arr[row][col] == 'N':
                    if col-2 >= 0 and self.arr[row][col-1] == self.arr[row][col-2] != 'N':
                        res_empty_cell -= 1
                        if self.arr[row][col-1] == '0':
                            res.arr[row][col] = '1'
                        else:
                            res.arr[row][col] = '0'
                    elif col+2 < self.N and self.arr[row][col+1] == self.arr[row][col+2] != 'N':
                        res_empty_cell -= 1
                        if self.arr[row][col+1] == '0':
                            res.arr[row][col] = '1'
                        else:
                            res.arr[row][col] = '0'
                    elif row-2 >= 0 and self.arr[row-1][col] == self.arr[row-2][col] != 'N':
                        res_empty_cell -= 1
                        if self.arr[row-1][col] == '0':
                            res.arr[row][col] = '1'
                        else:
                            res.arr[row][col] = '0'
                    elif row+2 < self.N and self.arr[row+1][col] == self.arr[row+2][col] != 'N':
                        res_empty_cell -= 1
                        if self.arr[row+1][col] == '0':
                            res.arr[row][col] = '1'
                        else:
                            res.arr[row][col] = '0'
        if res_empty_cell != cur_empty_cell and res.is_valid():
            result.append([res_empty_cell, res])
        else:
            ret,row,col = self.findNextPlace()
            if ret == True:
                tmp1 = self.deepcp()
                tmp2 = self.deepcp()
                tmp1.arr[row][col] = '0'
                tmp2.arr[row][col] = '1'
                if tmp1.is_valid():
                    result.append([cur_empty_cell-1, tmp1])
                if tmp2.is_valid():
                    result.append([cur_empty_cell-1, tmp2])
        return result

class Solver():
    def __init__(self, state):
        self.initial = state
        self.q = PriorityQueue()
        self.visited = set()
        
    def solver(self):
        cur = self.initial
        self.q.put(Prioritize(cur.count_empty(), cur))
        
        while cur.count_empty() != 0 and self.q.qsize():
            tmp = self.q.get()
            prior = tmp.priority
            cur = tmp.item
            self.visited.add(str(cur))

            for x in cur.produce():
                if str(x) not in self.visited:
                    self.q.put(Prioritize(x[0], x[1]))

        return cur

state = State("input.txt")
solver = Solver(state)
start = time.time()
res = solver.solver()
end = time.time()
res.display()
print('Solved in {:.04f} seconds'.format(end - start))
