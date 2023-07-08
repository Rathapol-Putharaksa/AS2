
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def NumtoThai(num):
    thaiValueFront = ["","หนึ่ง","สอง","สาม","สี่","ห้า","หก","เจ็ด","แปด","เก้า"]
    thaiValueBack = ["","สิบ","ร้อย","พัน","หมื่น","แสน","ล้าน","สิบล้าน"]
    degree = len(str(num))
    ConvertNumToThai = ""
    for index in range(degree):
         
        digit = num//10**index %10
        
        if degree == 1 and digit==0:
            return "ศูนย์"
        elif digit == 1 and index == 0:
            ConvertNumToThai = "เอ็ด"+ConvertNumToThai
        elif digit == 2 and index == 1:
            ConvertNumToThai = "ยี่สิบ"+ConvertNumToThai
        elif digit == 1 and index == 1:
            ConvertNumToThai = "สิบ"+ConvertNumToThai
        else:
            ConvertNumToThai = thaiValueFront[digit]+thaiValueBack[index]+ConvertNumToThai
    return ConvertNumToThai

        
        


    