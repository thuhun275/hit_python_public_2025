def songaytrongthang(thang, nam):
    def la_nam_nhuan(nam):
        return nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0)
    
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return "Tháng không hợp lệ"


print(songaytrongthang(10, 2020))
print(songaytrongthang(2, 2024))
print(songaytrongthang(2, 2025))
print(songaytrongthang(11, 1921))
