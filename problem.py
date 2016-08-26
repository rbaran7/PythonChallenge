#author: Roman Baran
#Python Challenge submission

m=int(raw_input())
n=int(raw_input())
matrix = [ ]
max = 0
count = 0

for i in xrange(m):
        matrix.append([int(x) for x in raw_input().split()])
#print(matrix)

matry = [[0 for x in xrange(n)] for y in xrange(m)]
#print(matry)

def find_connected(matrix, matry, i, j):        # 1 next 1
        global count
        if i < 0 or i >=m or j < 0 or j >= n:
                return
        if matry[i][j] == 1 or matrix[i][j] == 0:
                return
        count +=1
        matry[i][j] = 1
        #print(matry)
        for x in xrange(-1, 2):
                for y in xrange(-1,2):
                        if not(x==0 and y==0):
                                find_connected(matrix, matry, i+x, j+y)

for i in xrange(m):
        for j in xrange(n):
                find_connected(matrix, matry, i, j)
                if count > max:                         
                        max = count
                count = 0
print(max)
