
n = int(input())
    arr = list(map(int, input().split()))
    max_value = max(arr)
    arr_list = [i for i in arr if i != max_value]
    second_max_value = max(arr_list)

    print(second_max_value)