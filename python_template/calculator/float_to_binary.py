# coding: utf-8
def float_to_binary(num, places=10):
    whole_part = int(num)  # 整数部分
    frac_part = num - whole_part  # 小数部分

    whole_binary = bin(whole_part).replace("0b", "")  # 整数部分を2進数に
    frac_binary = ""
    
    while places:  # 指定された桁数まで計算
        frac_part *= 2
        bit = int(frac_part)
        if bit == 1:
            frac_part -= bit
            frac_binary += "1"
        else:
            frac_binary += "0"
        places -= 1
    
    return whole_binary + "." + frac_binary
    
