n = 54

so_chu_so = len(str(n))

tong = sum(int(chu_so)for chu_so in str(n)) 

print(f"Số lượng chữ số:  {so_chu_so}")
print(f"Tổng các chữ số: {tong}")