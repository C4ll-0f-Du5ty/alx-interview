#!/usr/bin/python3



def minOperations(n):
    if(n < 1):
        return 0
    operationsList = []
    current = 2


    def a(current):
        operations = 2
        oldCurrent = current
        flag = False
        while current < n:
            if n % current == 0:
                current += oldCurrent
                operations += 1 if flag else 2
                flag = True
            else:
                flag = False
                current += 1
                oldCurrent = current
                operations += 1
        return [operations, current]
    

    
    while current != n:
        temp = a(current)
        list.append(temp[0])
        
        
    if current == n:
        return operations
    else:
        return 0
