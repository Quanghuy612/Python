# 1. Tính tổng các số từ 1 đến 100
def tong_1_den_100():
    return sum(range(1, 101))

# 2. In bảng cửu chương của n
def bang_cuu_chuong(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# 3. Tính giai thừa của một số
def tinh_giai_thua(n):
    giaithua = 1
    for i in range(1, n + 1):
        giaithua *= i
    return giaithua

# 4. Tính Fibonacci n-th
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# 5. In các số nguyên tố nhỏ hơn N
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to_nho_hon_N(N):
    return [n for n in range(2, N) if la_so_nguyen_to(n)]

# 6. In hình tam giác sao
def in_tam_giac_sao(h):
    for i in range(1, h + 1):
        print("*" * i)

# 7. Kiểm tra số Armstrong
def la_so_armstrong(n):
    chu_so = list(map(int, str(n)))
    return sum(x ** len(chu_so) for x in chu_so) == n

# 8. Đảo ngược một số
def dao_nguoc_so(n):
    return int(str(n)[::-1])

# 9. Tính tổng các chữ số của một số
def tong_chu_so(n):
    return sum(map(int, str(n)))

# 10. Tính số lần xuất hiện của từ trong câu
def dem_tu_xuat_hien(s, word):
    return s.split().count(word)

# Kiểm tra với một số giá trị
print("Tổng từ 1 đến 100:", tong_1_den_100())  # 5050
bang_cuu_chuong(5)
print("5! =", tinh_giai_thua(5))  # 120
print("Fibonacci thứ 10:", fibonacci(10))  # 55
print("Số nguyên tố nhỏ hơn 20:", in_so_nguyen_to_nho_hon_N(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
in_tam_giac_sao(5)
print("153 có phải số Armstrong không?", la_so_armstrong(153))  # True
print("Số 1234 sau khi đảo ngược:", dao_nguoc_so(1234))  # 4321
print("Tổng các chữ số của 987:", tong_chu_so(987))  # 24
print("Số lần từ 'hello' xuất hiện:", dem_tu_xuat_hien("hello world hello", "hello"))  # 2
