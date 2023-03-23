#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對了，印出"你答對了"
#猜錯了，要告訴他比答案大還是小

import random
start = int(input('請使用者輸入開始值:'))
end = int(input('請使用者輸入結束值:'))
r = random.randint(start, end)
count = 0
while True:
    count = count + 1
    num = input('請輸入數字:')
    num = int(num)
    if num == r:
        print('你答對了')
        break

    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
        print('這是你猜的第幾次', count,'次')