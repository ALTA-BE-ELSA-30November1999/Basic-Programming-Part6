def find_max_sum_sub_array(k, arr):
    start = 0
    sum = 0
    maxsum = 0
    for i in range(len(arr)) :
        sum += arr[i]
        if i >= k-1 :
            maxsum = max(maxsum, sum)
            sum -= arr[start]
            start+=1
    return maxsum

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8