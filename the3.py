import sys 
import copy

def neighbors(lst,row,column):
    dneighbor = 0
    fneighbor = 0
    if row != 0:
        if lst[row-1][column] == '-':
            dneighbor += 1
        else:
            fneighbor += 1
        if column != 0:
            if lst[row-1][column-1] == '-':
                dneighbor += 1
            else: 
                fneighbor += 1
        if column != len(lst[0])-1:
            if lst[row-1][column+1] == '-':
                dneighbor += 1
            else:
                fneighbor += 1
    if column != 0:
        if lst[row][column-1] == '-':
            dneighbor += 1
        else:
            fneighbor += 1
        if row != len(lst)-1:
            if lst[row+1][column-1] == '-':
                dneighbor += 1
            else:
                fneighbor += 1
    if row != len(lst)-1:
        if lst[row+1][column] == '-':
            dneighbor += 1
        else:
            fneighbor += 1
        if column != len(lst[0])-1:
            if lst [row+1][column+1] == '-':
                dneighbor += 1
            else:
                fneighbor += 1
    if column != len(lst[0])-1:
        if lst[row][column+1] == '-':
            dneighbor += 1
        else:
            fneighbor += 1
    return ['*',fneighbor,'-',dneighbor]

f = open(sys.argv[1], "r")
f1 = f.readlines()
lst = []
for line in f1:
    row = [] 
    for i in range(len(line)):
        if line[i] == '\n':
            continue
        row.append(line[i])
    lst.append(row) 
new_lst = copy.deepcopy(lst)
f.close()
for i in range(int(sys.argv[3])):
    num_row = 0
    for x in lst:
        num_column = 0
        for y in x:
            f = open(sys.argv[2],"r")
            f1 = f.readlines()
            check = neighbors(lst, num_row, num_column)
            for line in f1:
                first = line[0]
                condition = line[1]
                num = int(line[2])
                second = line[3]
                if first == second:
                    continue
                if y == first:
                    if condition == '=':
                        if check[1] == num:
                            new_lst[num_row][num_column] = second
                    if condition == '>':
                        if check[1] > num:
                            new_lst[num_row][num_column] = second
                    if condition == '<':
                        if check[1] < num:
                            new_lst[num_row][num_column] = second
            f.close()
            num_column += 1
        num_row += 1
    lst = copy.deepcopy(new_lst)
for x in new_lst:
    print "".join(x)
