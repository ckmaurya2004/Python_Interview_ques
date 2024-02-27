# Iterate on  list without using loop from start to end

#[2,4,6,4,90]


lst = eval(input(" enter a list" ))
start_index = eval(input(" enter a last index "))
end_indx = eval(input(" enter a end  index "))



def iterate(lst,start,end):
    if start<0 or start>=end:
        return
    print(lst[start])
    iterate(lst,start+1,end)


iterate(lst,start_index,end_indx)
