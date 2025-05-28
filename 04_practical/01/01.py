def reverse_list(lst):
    return lst[::-1]

my_list = ['becky','joseph', 'lorpu', 'james']
reversed_list = reverse_list(my_list)
print(reversed_list)  

def rotate_list(lst, k):
    k = k % len(lst) 
    return lst[-k:] + lst[:-k]

my_list = [1, 2, 3, 4, 5]
print(rotate_list(my_list, 2)) 
