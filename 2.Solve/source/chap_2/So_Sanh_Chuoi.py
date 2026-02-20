# Định nghĩa một hàm có đầu vào là 2 chuỗi và 
# in chuỗi có độ dài lớn hơn trong giao diện điều khiển. 
# Nếu 2 chuỗi có chiều dài như nhau thì 
# in tất cả các chuỗi theo dòng. 

def ex_24(st1, st2):
    len1 = len(st1)
    len2 = len(st2)
    
    if len1 > len2:
        print(st1)
    elif len1 < len2:
        print(st2)
    else:
        print(st1) 
        print(st2)