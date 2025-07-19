
tien = 28
gia_mot_chai = 28


so_chai_da_uong = tien // gia_mot_chai  
so_vo = so_chai_da_uong                

while so_vo >= 3:
    doi_duoc = so_vo // 3        
    so_chai_da_uong += doi_duoc  
    so_vo = so_vo % 3 + doi_duoc 


print(f"Số chai bia có thể mua được là: {so_chai_da_uong}")
