#Bài tập về kiểu dữ liệu
#Sắp xếp mảng tăng/giảm dần bằng python

#Nhập dữ liệu
def enter_num():
    global num
    while True:
        x = input('Dữ liệu nhập vào mảng: ').upper()
        if x == 'DONE':
            print('Kết thúc nhập dữ liệu cho mảng')
            break
        num.append(float(x))

#Sắp xếp mảng
def sort_array(num):
    print('Chọn (1) hoặc (2):\n (1)Tăng dần\n (2)Giảm dần')
    choice = int(input('Lựa chọn của bạn: '))
    if choice == 1:
        for i in range (0,len(num) -1):
            for j in range (i+1, len(num)):
                if num[i] > num[j]:
                    tmp = num[i]
                    num[i] = num[j]
                    num[j] = tmp
        return num
    if choice == 2:
        for i in range (0,len(num) -1):
            for j in range (i+1, len(num)):
                if num[i] < num[j]:
                    tmp = num[i]
                    num[i] = num[j]
                    num[j] = tmp
        return num

#Chạy chương trình
print('CHƯƠNG TRÌNH SẮP XẾP MẢNG')
print('Nhập xong nhập (Done) để kết thúc')
num=[]
print('Nhập dữ liệu')
enter_num()
print('Mảng trước khi sắp xếp:\n',num)
print('Mảng sau khi sắp xếp:\n',sort_array(num))

