from asyncio.windows_events import NULL
from copy import deepcopy
from queue import PriorityQueue
import time
import tracemalloc
# import guppy
# from guppy import hpy

counter = 0
matrix = 9

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
    
    # Hàm check number đã được dùng trong hàng chưa
    def used_in_row(self, row, num):
        for i in range(matrix):
            if(self.arr[row][i] == num):
                return True
        return False

    # Hàm check number đã được dùng trong cột chưa
    def used_in_col(self, col, num):
        for i in range(matrix):
            if(self.arr[i][col] == num):
                return True
        return False

    # Hàm check number đã được dùng trong box 3x3 chưa
    def used_in_box(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if(self.arr[i + row][j + col] == num):
                    return True
        return False

    # Hàm check number có dùng được ở vị trí đó không, nó trả về boolean, check number phải không trùng trong hàng, không trùng trong cột, không trùng trong box 3x3
    # Phạm luật return False, ngược lại return True
    def check_location_is_safe(self, row, col, num):
        violationInRow = self.used_in_row(row, num)
        violationInCol = self.used_in_col(col, num)
        violationInBox = self.used_in_box(row - row % 3, col - col % 3, num)
        return not violationInRow and not violationInCol and not violationInBox
    # Hàm in mảng
    def print_grid(self):
        global counter 
        counter = counter + 1
        with open('outputAStar.txt', 'a') as f:
            f.write('Step '+ str(counter) + '\n')
            for i in range(matrix):
                if(i%3 == 0 and i):
                    for j in range(matrix-1):
                        f.write('=====')
                    f.write('\n')
                for j in range(matrix):
                    if(j == 0):
                        f.write('| ')
                    elif(j%3 == 0):
                        f.write('| ')
                    else:
                        f.write(' ')
                    f.write(str(self.arr[i][j]))
                    f.write(' |')
                f.write('\n')
    
    def findNextPlace(self):
        for row in range(self.N):
            for col in range(self.N):
                if self.arr[row][col] == '?':
                    return True,row,col
        return False,-1,-1

    def countEmpty(self):
        # Tính số vị trí còn trống
        emptyNum = 0
        for row in range(matrix):
            for col in range(matrix):
                if(self.arr[row][col] == '?'): 
                    emptyNum += 1
        return emptyNum
    def countPossibleWays(self, row, col):
        # Tính số cách có thể không bị vi phạm
        caseNum = 0
        for i in range(1, 10):
            if self.check_location_is_safe(row, col, str(i)):
                caseNum += 1
        return caseNum

    def produce(self):
        result = []
        for row in range(self.N):
            for col in range(self.N):
                if(self.arr[row][col] == '?'):
                    # Tính độ ưu tiên dựa trên số ô còn trống + số khả năng có thể của ô trống đó.
                    priority = self.countEmpty() + self.countPossibleWays(row, col)
                    for i in range(1,10):
                        if self.check_location_is_safe(row, col, str(i)):
                            # print(row, col, i)
                            child = self.deepcp()
                            child.arr[row][col] = str(i)
                            result.append([priority, child])
        return result






class Solver():
    def __init__(self, state):
        self.initial = state
        self.q = PriorityQueue()
        self.visited = set()
        
    def solver(self):
        cur = self.initial
        self.q.put(Prioritize(cur.countEmpty(), cur))

        while cur.countEmpty() != 0 and not self.q.empty():
            tmp = self.q.get()
            
            cur = tmp.item

            cur.print_grid()

            self.visited.add(str(cur))

            for x in cur.produce():
                if str(x[1]) not in self.visited:
                    self.q.put(Prioritize(x[0],x[1]))
        if(cur.countEmpty() != 0):
            return NULL
        return cur

# Hàm main
def main():
    
    tracemalloc.start()
    # TODO
    state = State("input.txt")
    solver = Solver(state)
    #đo thời gian
    start = time.time()
    res = solver.solver()
    if(res == NULL):
        print("Không có lời giải!")
    else:
        print("Tìm thấy lời giải, xem trong file OutputAStar.txt")
    end = time.time()
    
    # đo bộ nhớ
    mem = tracemalloc.get_traced_memory()[1]
    print('Memory used {} bytes'.format(mem))
    tracemalloc.stop()
    print('Solved in {:.04f} seconds'.format(end - start))


main()
