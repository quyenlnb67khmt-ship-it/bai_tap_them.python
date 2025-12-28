#viết chương trình in ra tất cả các số nguyên nhỏ hơn 100
for i in range(2,100):
    so_nguyen_to = True
    for j in range(2,i):
        if i%j==0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(i)