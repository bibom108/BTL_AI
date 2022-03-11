
# Trắng: '0'
# Đen : '1'
# Trống : 'N'
import time

class Object:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

class BinairoBFS:
    def __init__(self, filename):
        arr = []
        f = open(filename, "r")
        for row in f:
            tmp = [(ele) for ele in row if ele != '\n']
            arr.append(tmp)
        self.arr = arr
        self.N = len(self.arr)
        self.queue = []

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
            for col in range(1, self.N - 1):
                if self.arr[row][col] == 'N':
                    continue
                if self.arr[row][col - 1] == self.arr[row][col] == self.arr[row][col + 1]:
                    return False

        for col in range(self.N):
            for row in range(1, self.N - 1):
                if self.arr[row][col] == 'N':
                    continue
                if self.arr[row - 1][col] == self.arr[row][col] == self.arr[row + 1][col]:
                    return False
        # Check number of black and white
        for i in range(self.N):
            if self.get_row(i).count("0") > self.N / 2 or self.get_row(i).count("1") > self.N / 2:
                return False
            if self.get_col(i).count("0") > self.N / 2 or self.get_col(i).count("1") > self.N / 2:
                return False
        # Check unique
        for i in range(self.N):
            for j in range(i):
                if self.get_row(i).count("N") == 0 and self.get_row(j).count("N") == 0 and self.get_row(
                        i) == self.get_row(j):
                    return False
                if self.get_col(i).count("N") == 0 and self.get_col(j).count("N") == 0 and self.get_col(
                        i) == self.get_col(j):
                    return False
        return True

    def display(self):
        print("")
        for row in range(self.N):
            print(self.get_row(row))
        print("")

    def findEmpty(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.arr[i][j] == 'N':
                    return i, j
        return None

    # Tạo node phù hơp thêm vào mảng
    def addQueue(self, arr, value):
        newTemp = []
        for i in range(len(arr)):
            newTemp.append(arr[i])
        newTemp.append(value)
        return newTemp

    def solver(self):
        findOut = self.findEmpty()
        row, col = findOut
        self.arr[row][col] = '0'
        if self.is_valid():
            self.queue.append([Object('0', row, col)])

        self.arr[row][col] = '1'
        if self.is_valid():
            self.queue.append([Object('1', row, col)])

        self.arr[row][col] = 'N'

        while (len(self.queue) != 0):
            temp = self.queue.pop(0)
            for i in range(len(temp)):
                self.arr[temp[i].row][temp[i].col] = temp[i].value

            findOut = self.findEmpty()
            if not findOut:
                return True

            row, col = findOut
            self.arr[row][col] = '0'
            if self.is_valid():
                self.queue.append(self.addQueue(temp, Object('0', row, col)))
            self.arr[row][col] = '1'
            if self.is_valid():
                self.queue.append(self.addQueue(temp, Object('1', row, col)))

            self.arr[row][col] = 'N'
            for i in range(len(temp)):
                self.arr[temp[i].row][temp[i].col] = 'N'
        return None


class BinairoDFS:
    def __init__(self, filename):
        arr = []
        f = open(filename, "r")
        for row in f:
            tmp = [(ele) for ele in row if ele != '\n']
            arr.append(tmp)
        self.arr = arr
        self.N = len(self.arr)

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
            for col in range(1, self.N - 1):
                if self.arr[row][col] == 'N':
                    continue
                if self.arr[row][col - 1] == self.arr[row][col] == self.arr[row][col + 1]:
                    return False

        for col in range(self.N):
            for row in range(1, self.N - 1):
                if self.arr[row][col] == 'N':
                    continue
                if self.arr[row - 1][col] == self.arr[row][col] == self.arr[row + 1][col]:
                    return False
        # Check number of black and white
        for i in range(self.N):
            if self.get_row(i).count("0") > self.N / 2 or self.get_row(i).count("1") > self.N / 2:
                return False
            if self.get_col(i).count("0") > self.N / 2 or self.get_col(i).count("1") > self.N / 2:
                return False
        # Check unique
        for i in range(self.N):
            for j in range(i):
                if self.get_row(i).count("N") == 0 and self.get_row(j).count("N") == 0 and self.get_row(
                        i) == self.get_row(j):
                    return False
                if self.get_col(i).count("N") == 0 and self.get_col(j).count("N") == 0 and self.get_col(
                        i) == self.get_col(j):
                    return False
        return True

    def findNextPlace(self):
        for row in range(self.N):
            for col in range(self.N):
                if self.arr[row][col] == 'N':
                    return True, row, col
        return False, -1, -1

    def display(self):
        print("")
        for row in range(self.N):
            print(self.get_row(row))
        print("")

    def solver(self):
        ret, row, col = self.findNextPlace()
        if ret == False:
            return True

        for num in range(0, 2):
            self.arr[row][col] = str(num)
            if self.is_valid():
                if self.solver():
                    return True
            self.arr[row][col] = 'N'

        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    binairobfs = BinairoBFS("input.txt")
    start = time.time()
    binairobfs.solver()
    end = time.time()
    binairobfs.display()
    print('Solved in {:.04f} seconds'.format(end - start))

    binairodfs = BinairoDFS("input.txt")
    start = time.time()
    binairodfs.solver()
    end = time.time()
    binairodfs.display()
    print('Solved in {:.04f} seconds'.format(end - start))