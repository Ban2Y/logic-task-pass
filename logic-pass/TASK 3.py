#TASK 3:

def COUNT(String, G_chr):
    count = 0
    for i in String:
        if G_chr == i:
            count += 1
    print(G_chr, 'Repeated:', count, 'time')
COUNT('BanKhalid' , 'a')