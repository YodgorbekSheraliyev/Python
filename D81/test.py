chars = "aewfew"

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
results= []
is_ascending = False


for row in grid: 
    results.append(sorted(list(row)))
    
for index in range(len(results[0])):
    current_row = results[index]
    for next_row in results[index+1::]:
        
        pass
    
print("a" < "b")
print(grid[1::])