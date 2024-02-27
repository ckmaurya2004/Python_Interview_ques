def rectangle(n_sticks,lengths):
    arr = []
    for skt in lengths:
        if lengths.count(skt)>=2 and skt not in arr:
            arr.append(skt)
    max_area = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i]*arr[j])>max_area:
                max_area =(arr[i]*arr[j])

    return max_area


print(rectangle(8,[1,5,6,5,1,6,8,8]))