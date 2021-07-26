def odd_evn(lst):
    evn_cnt,odd_cnt=0,0
    for item in lst:
            if item%2==0:
                evn_cnt=evn_cnt+1
            else:
                odd_cnt=odd_cnt+1

    return evn_cnt,odd_cnt

lst1=[1,2,3,4,5,5,6,6,7,8,9]
o,e=odd_evn(lst1)
print("Number of Even",e,"Number of Odd",o)

