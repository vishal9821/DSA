# def subarray_sum(arr,target):
#     hashtable = {0:-1}
#     current_sum = 0
#     for i , num in enumerate(arr):
#         current_sum+=num
#         if current_sum-target in hashtable:
#             starting_index = hashtable[current_sum-target]+1
#             return [starting_index,i]
#         hashtable[current_sum] = i
#         print(current_sum)
#         print(hashtable)
#         print(current_sum-target)
#     return []
    


    
        
# print(subarray_sum([-1,2,3,-4, 5], 0))
