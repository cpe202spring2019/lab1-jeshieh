def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == []:
        return None

    elif int_list == None:
        raise ValueError

    else:
        max_num = int_list[0]
        for item in int_list:
            if item > max_num:
                max_num = item

            return max_num


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

    if int_list == None:
        raise ValueError

    if len(int_list) != 1:
        return_list = reverse_rec(int_list[1:])
        return_list.append(int_list[0])
        return return_list
    elif len(int_list) == 1:
        return int_list





def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """

    if int_list == None:
        raise ValueError

    index = int((low + high) // 2)

    if int_list[index] == target:
        return index

    if target < int_list[low] or target > int_list[high]:
        return None


    if int_list[index] > target:
        return bin_search(target, low, index - 1, int_list)

    else:
        return bin_search(target, index + 1, high, int_list)


