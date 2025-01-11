#with open("ex",'r') as f:
with open("case_database.txt.enc.txt", 'r') as f:
    mas = f.readline()
    print(mas)
    mas_new = ["" for i in range(len(mas))]
    step_true=32 # 27
    #step_true = 3
    rows = 27  # 32
    n = [0 for i in range(rows)]
    step_rows = int(rows/4)
    n[step_rows*2]=step_true*(step_rows-1)+(step_true)*(step_rows*2-1
    #n[step_rows]=56+8*16
    #n[step_rows*3]=step_rows*3
    for i in range(0, rows):
        if i>0 and i < step_rows:
            n[i] = n[i-1]+step_rows
        if i>step_rows and i < step_rows*2:
            n[i] = n[i-1]-step_rows
        if i>=step_rows*2 and i < step_rows*3:
            n[i] = n[i-1]-step_rows
        if (i >= (step_rows*3)):
            n[i] = i * step_rows
    n_new = n
    print(n_new)
    n = [0 for i in range(len(mas))]

    for j in range(0,len(mas)):
        if j<rows:
            n[j] = n_new[j % rows]
            continue
        #print(j,j%rows,j//rows)
        if(n[j-rows]+1 in n):
            print("!!!",n[j-rows]+1)
            continue
        n[j] = n[j-rows]+1
        #n[j] = j
        #n[i*step_true+j] = i*step_true+j
        #print((i*step_true+j))

    #n = [0, 1, 2, 8, 7, 6, 5, 4, 3, 9, 10, 11]
    print(n)
    i = 0
    for colum in range(0, step_true):
        for row in range(0, rows):
            #print(len(mas_new),len(n),i,n[i])
            mas_new[n[i]] = mas[i]
            i=i+1

print(mas_new)
for i in range(len(mas)):
    print(mas_new[i], end="")
print()
print(len(mas_new))
