"""
เขียนโปรแกรมอะไรก็ได้ที่อยาก present Python's skill set เจ๋ง ๆ ของตัวเอง
ข้อนี้ไม่ต้องทำก็ได้ ไม่มีผลลบกับการให้คะแนน แต่ถ้าทำมาเเล้วเจ๋งจริง ก็จะพิจารณาเป็นพิเศษ

"""

#assume arr sort  ascending

def binarySearch(arr,num):
    minIndex = 0
    maxIndex = len(arr)
    while minIndex<=maxIndex:

        midIndex = (minIndex + maxIndex)//2
        if arr[midIndex] == num:
            return midIndex
        elif arr[midIndex]>num:
            maxIndex = midIndex-1
        elif arr[midIndex]<num:
            minIndex = midIndex+1
        
    return -1

print(binarySearch([1,2,3,4,5,6,7], 2))