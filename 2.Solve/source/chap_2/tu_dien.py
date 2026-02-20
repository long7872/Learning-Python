# Bài 25: Tạo tệp tu_dien.py để định nghĩa:
# - 01 hàm Tao_TD(Max) để tạo 1 từ điển, chứa các key là số từ 1 đến Max (số Max nhập vào từ bàn phím) và các giá trị là bình phương của key. 
# - 01 Hàm Print_Item(TD) để in các phần tử của từ điển.
# - 01 Hàm Print_Key(TD) để in các giá trị của các phần tử từ điển
# - 01 Hàm Print_Value(TD) để in giá trị của các phần tử từ điển 
# - Tạo tệp Test_TD.py để sử dụng các hàm này.

def Tao_TD(Max):
    dc = {}
    for i in range(1, Max+1):
        dc[i] = i**2
    return dc

def Print_Item(TD: dict):
    for tup in TD.items():
        print(tup, end=" ")
    print()

def Print_Key(TD: dict):
    for k in TD.keys():
        print(k, end=" ")
    print()

def Print_Value(TD: dict):
    for v in TD.values():
        print(v, end=" ")
    print()