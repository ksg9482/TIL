def strnum_add(strnum:str):
    splited = list(strnum)
    total = int(strnum)
    for i in splited:
        total += int(i)
    return total

def self_num():
    num_arr = list(map(int, range(1,10000+1)))
    copy_arr = num_arr[0:]
    for i in num_arr:
        num_str = str(i)
        if len(num_str) < 2:
            num_str = '0' + str(i)
        self_number = strnum_add(num_str)
        try:
            copy_arr.remove(self_number)
        except:
            pass
    for i in copy_arr:
        print(i)
self_num()
