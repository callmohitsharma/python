def sub_lists(sublist,list1,index,subarr):
    # store all the sublists
    #sublist = [[]]
    if index == len(list1):
        if len(subarr)!= 0:
            sublist.append([subarr])
            print(subarr)

    else:
        sub_lists(sublist,list1,index+1,subarr)
        sub_lists(sublist,list1, index + 1, subarr+[list1[index]])


    return sublist
#This is wrong
def sub_lists2(list1):
    # store all the sublists
    sublist = [[]]
    res = [list1[i: j] for i in range(len(list1))
           for j in range(i + 1, len(list1) + 1)]

    sublist.append(res)

    return sublist


if __name__ == "__main__":
    l1 = [1, 2, 3]
    print(sub_lists([[]],l1,0,[]))
    #print(sub_lists2(l1))