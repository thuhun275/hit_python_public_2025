luong = 5000000


if luong > 15000000:
    thue = luong * 0.3
elif luong > 7000000:
    thue = luong * 0.2
else:
    thue = luong * 0.1

luong_rong = luong - thue

print(f"Thuế: {int(thue)}")
print(f"Thu nhập: {int(luong_rong)}")