for i in range(1,10):
    for j in range(1,10):
        re = i*j
        if j > i:
            break
        print(str(j) + "x" + str(i) + "=" + str(re),end=" ")
    print()

