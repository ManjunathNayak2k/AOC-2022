with open("input.txt", 'r', encoding="utf-8") as f:
    lines = f.read().split('\n')

matrix = []
rows = len(lines)
cols = len(list(lines[0]))
for i in lines:
    matrix.append(list(i))

n=5
total = 2*cols + 2*(rows-2)

# part 1
# print(total)
# for i in range(1,rows-1):

#     for j in range(1,cols-1):
#         flagl = flagr= flagu = flagd = True
        
        
#         for r in range(i):
#             if matrix[i][j] <= matrix[r][j]:
#                 flagd = False
            

#         for c in range(j):
#             if matrix[i][j] <= matrix[i][c]:
#                 flagl = False


#         for r in range(i+1, rows):
#             if matrix[i][j] <= matrix[r][j]:
#                 flagu = False


#         for c in range(j+1, cols):
#             if matrix[i][j] <= matrix[i][c]:
#                 flagr = False
        
#         if flagr or flagu or flagd or flagl: 
            
#             total= total + 1

# print(total)

# part 2
total = 0
for i in range(1,rows-1):

    for j in range(1,cols-1):
        countl = countr= countu = countd = 0
        
        
        for r in range(i-1, -1, -1):
            countu = countu+1
            if matrix[i][j] <= matrix[r][j]:
                break
            
        for c in range(j-1, -1, -1):
            countl = countl+1
            if matrix[i][j] <= matrix[i][c]:
                break

        for r in range(i+1, rows):
            countd = countd+1
            if matrix[i][j] <= matrix[r][j]:
                break       
                
        for c in range(j+1, cols):
            countr = countr+1
            if matrix[i][j] <= matrix[i][c]:                
                break
   
        score = countl*countr*countd*countu

        if score > total:
            total = score

print(total)
