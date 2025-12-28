#Viết chương trình kiểm tra xem một số có phải là số nguyên tố hay không

so = int(input("Hãy nhập số mong muốn: "))
so_nguyen_to = True
for i in range(2,so):
    if so%i==0:
        so_nguyen_to = False
        break
if so_nguyen_to:
    print(f"Số {so} là số nguyên tố")
else:
    print(f"Số {so} không phải là số nguyên tố")