# 1. Kiểm tra số chẵn/lẻ
def kiem_tra_chan_le(n):
    return "Chẵn" if n % 2 == 0 else "Lẻ"

# 2. Kiểm tra năm nhuận
def kiem_tra_nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return "Năm nhuận"
    return "Không phải năm nhuận"

# 3. Kiểm tra số lớn hơn 100 hay không
def kiem_tra_lon_hon_100(n):
    return "Lớn hơn 100" if n > 100 else "Nhỏ hơn hoặc bằng 100"

# 4. Tính thuế thu nhập dựa trên mức lương
def tinh_thue(luong):
    if luong <= 5000000:
        thue = luong * 0.05
    elif luong <= 10000000:
        thue = luong * 0.1
    elif luong <= 20000000:
        thue = luong * 0.15
    else:
        thue = luong * 0.2
    return f"Thuế phải đóng: {thue}"

# 5. Xác định học lực
def xep_loai_hoc_luc(dtb):
    if dtb >= 8.5:
        return "Giỏi"
    elif dtb >= 6.5:
        return "Khá"
    elif dtb >= 5:
        return "Trung bình"
    else:
        return "Yếu"

# 6. Kiểm tra số chia hết cho 3 và 5
def chia_het_3_5(n):
    return "Chia hết cho cả 3 và 5" if n % 3 == 0 and n % 5 == 0 else "Không chia hết"

# 7. Xác định giai đoạn tuổi
def xac_dinh_tuoi(tuoi):
    if tuoi < 12:
        return "Trẻ em"
    elif tuoi < 18:
        return "Thanh niên"
    elif tuoi < 60:
        return "Người lớn"
    else:
        return "Người già"

# 8. Kiểm tra ba số có tạo thành tam giác không
def kiem_tra_tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "Là tam giác"
    return "Không phải tam giác"

# 9. Xác định nguyên âm hay phụ âm
def kiem_tra_nguyen_am_phu_am(ch):
    nguyen_am = "aeiouAEIOU"
    return "Nguyên âm" if ch in nguyen_am else "Phụ âm"

# 10. Kiểm tra tính hợp lệ của ngày trong tháng
def kiem_tra_ngay_hop_le(ngay, thang, nam):
    from calendar import isleap
    if thang < 1 or thang > 12:
        return "Không hợp lệ"

    ngay_trong_thang = [31, 29 if isleap(nam) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return "Hợp lệ" if 1 <= ngay <= ngay_trong_thang[thang - 1] else "Không hợp lệ"

# Kiểm tra với một số giá trị
print(kiem_tra_chan_le(7))               # Lẻ
print(kiem_tra_nam_nhuan(2024))          # Năm nhuận
print(kiem_tra_lon_hon_100(150))         # Lớn hơn 100
print(tinh_thue(12000000))               # Thuế phải đóng: 1800000.0
print(xep_loai_hoc_luc(7.2))             # Khá
print(chia_het_3_5(15))                  # Chia hết cho cả 3 và 5
print(xac_dinh_tuoi(25))                 # Người lớn
print(kiem_tra_tam_giac(3, 4, 5))        # Là tam giác
print(kiem_tra_nguyen_am_phu_am('e'))    # Nguyên âm
print(kiem_tra_ngay_hop_le(29, 2, 2023)) # Không hợp lệ
