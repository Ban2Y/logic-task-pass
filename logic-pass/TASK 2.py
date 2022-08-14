#TASK 2:

def chk_Prime(No):
    if No > 1:
        for i in range(2 ,int(No/2)+1):
            if No % i == 0:
                print(No, 'Not Prime')
                break
        else:
            print(No, 'This Prime')
chk_Prime(3)
chk_Prime(33)