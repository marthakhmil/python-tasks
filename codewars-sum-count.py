#count_positives_sum_negatives([1,2,3,4,5,6,-9,-6,-5])
def count_positives_sum_negatives(arr):
    my_list_pos=[]
    my_list_total=[]
    total=0
    for i in arr:
        if i > 0:
            my_list_pos.append(i)
            a=len(my_list_pos)
    my_list_total.append(a)
            
    for i in arr:
         if i < 0 :
            total+=i
    my_list_total.append(total)
    print (my_list_total)
    for i in arr:
         if i = 0 :
    print ([0,0])
