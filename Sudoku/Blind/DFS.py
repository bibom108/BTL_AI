import tracemalloc
import time

counter = 0

# Hàm in mảng
def print_grid(arr):
    global counter 
    counter = counter + 1
    # print('Step', counter)
    # for i in range(9):
    #     for j in range(9):
    #         if(j == 0):
    #             print('|', arr[i][j], '| ', end='')
    #         else: print(arr[i][j], '| ', end='')
    #     print('\n')

    with open('outputDFS.txt', 'a') as f:
        f.write('Step '+str(counter)+'\n')
        for i in range(9):
            if(i%3 == 0 and i):
                for j in range(8):
                    f.write('=====')
                f.write('\n')
            for j in range(9):
                if(j == 0):
                    f.write('| ')
                elif(j%3 == 0):
                    f.write('| ')
                else:
                    f.write(' ')
                f.write(str(arr[i][j]))
                f.write(' |')
            f.write('\n')


        
# Hàm tìm vị trí còn trống trong mảng, nếu có vị trí trống thì vị trí đó được gán lần lượt chỉ mục row, col cho mảng l, nếu không còn 
# vị trí nào trống thì return false
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]== '?'):
                l[0]= row
                l[1]= col
                return True
    return False

# Hàm check number đã được dùng trong hàng chưa
def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

# Hàm check number đã được dùng trong cột chưa
def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

# Hàm check number đã được dùng trong box 3x3 chưa
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False

# Hàm check number có dùng được ở vị trí đó không, nó trả về boolean, check number phải không trùng trong hàng, không trùng trong cột, không trùng trong box 3x3
def check_location_is_safe(arr, row, col, num):
    violationInRow = used_in_row(arr, row, num)
    violationInCol = used_in_col(arr, col, num)
    violationInBox = used_in_box(arr, row - row % 3, col - col % 3, num)
    if(violationInRow):
        with open('outputDFS.txt', 'a', encoding='utf-8') as f:
            f.write(str(num))
            f.write(' vi phạm luật trùng trên cùng 1 hàng\n')
    elif(violationInCol):
        with open('outputDFS.txt', 'a', encoding='utf-8') as f:
            f.write(str(num))
            f.write(' vi phạm luật trùng trên cùng 1 cột\n')
    elif(violationInBox):
        with open('outputDFS.txt', 'a', encoding='utf-8') as f:
            f.write(str(num))
            f.write(' vi phạm luật trùng trong 1 box 3x3\n')
    else:
        with open('outputDFS.txt', 'a', encoding='utf-8') as f:
            f.write('Không vi phạm luật nên chọn ')
            f.write(str(num))
            f.write('\n')
    return not violationInRow and not violationInCol and not violationInBox



def solve_sudoku(arr):
    
    # mảng l chứa chỉ mục hàng, cột vị trí trống
    l =[0, 0]
    
    # Nếu không có hàng, cột nào trống thì tất nhiên là ta đã hoàn thành bài toán, return true, nếu không thì chạy tiếp tục
    if(not find_empty_location(arr, l)):
        return True
    
    # Gán value đã ghi được ở mảng l vào cho 2 biến row, col
    row = l[0]
    col = l[1]

    # in ra từng bước
    print_grid(arr)   
    
    # xem xét điền số từ 1 tới 9
    for num in range(1, 10):
        
        # nếu mà number (từ 1 -> 9) phù hợp với vị trí này
        if(check_location_is_safe(arr,
                        row, col, num)):
            
            # điền số vào vị trí
            arr[row][col]= num

            # lặp đệ quy, nếu thành công, return true
            if(solve_sudoku(arr)):
                return True

            # nếu mà không thành công, trả lại ? cho vị trí đó, và thử số khác
            
            arr[row][col] = '?'  
    #return false nếu thoát vòng lặp for mà không thành công, kích hoạt quay lui	
    return False


# Hàm main
def main():
    
    # tạo mảng 2 chiều
    grid =[[0 for x in range(9)]for y in range(9)]
    
    # gán giá trị cho mảng
    grid =[['?',4, 9,1, '?', 6, '?', 3, 7],
        [3, '?',5 , '?', 9, '?', '?', 6, '?'],
        ['?',1,7, 4, '?', 3, 2,'?', '?'],
        ['?', 3, 2, 7, '?', '?', '?', 8, '?'],
        [5, '?', 6, '?', 3, '?', 1, '?', 4],
        ['?', 9, '?', 5, '?', 2, '?', 7, '?'],
        ['?', '?', 4, 6, 1,'?', '?', 9,'?'],
        ['?', '?', 3, '?', 7, '?', 6, '?', 2],
        [9, '?', 1,3, '?','?', '?', '?', '?']]

    #đo thời gian
    start = time.time()
    tracemalloc.start()
    if(solve_sudoku(grid)):
        print_grid(grid)
    else:
        print("No solution exists")

    end = time.time()
    mem = tracemalloc.get_traced_memory()[1]

    print('Memory used {} bytes'.format(mem))
    tracemalloc.stop()
    print('Solved in {:.04f} seconds'.format(end - start))
main()