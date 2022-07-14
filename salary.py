def sort(N,m = []):
    mas = m
    size = N
    done = True # flag - done
    while(done):
        done = False
        for i in range(size-1):
            if mas[i] >= mas[i+1]:
                mas[i], mas[i+1] = mas[i+1], mas[i]
                done = True
    return mas




def SynchronizingTables (N ,ids = [],salary = []):
    done = True # flag - done
    copy_ind = []
    for i in range(N):
        copy_ind.append(ids[i])
    
    sort_salary = sort(N,salary)
    sort_ind = sort(N,copy_ind)
    new_array = []
    for x in range(N):
        for y in range(N):
            if ids[x] == sort_ind[y]:
                new_array.append(salary[y])

    return new_array
