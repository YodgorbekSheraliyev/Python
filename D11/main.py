enemies = 1

def increase():
    global enemies
    enemies +=1
    print(f"your enemies: {enemies}")
    
print(increase())