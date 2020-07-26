
def get_max(value):
    max = 0
    if len(value) ==1:
        return 0
    for i in range(0,len(value)):
        if max < value[i]:
            max = value[i]
            index = i
    return index

def compare_weight(value,weight,val_arr,weight_arr,w):
    for i in range(0,len(value)):
        if len(value) == 0:
            return val_arr,weight_arr
        else:
            i = get_max(value)
            if weight[i]<=int(w):
                if (sum(weight_arr) + weight[i])<=int(w):
                    weight_arr.append(weight[i])
                    val_arr.append(value[i])
                    del value[i]
                    del weight[i]
                else:
                    del value[i]
                    del weight[i]
            else:
                del value[i]
                del weight[i]
            compare_weight(value, weight, val_arr, weight_arr,w)

def sub_lists(sublist,list1,index,subarr):
    # store all the sublists
    # sublist = [[]]
    if index == len(list1):
        if len(subarr) != 0:
            sublist.append([subarr])
            print(subarr)

    else:
        sub_lists(sublist, list1, index + 1, subarr)
        sub_lists(sublist, list1, index + 1, subarr + [list1[index]])

    return sublist

if __name__ == "__main__":
    print("Enter no of testcases: ")
    t = int(input())
    if t>=1 and t<=20:
        for y in range(0,t):
            arr = []
            print("Enter capacity and no of values: ")
            w,n = input().split()
            w = int(w)
            n = int(n)
            print("next %s lines, where each line contains 2 numbers weight and value" % n)
            for i in range(int(n)):
                v1, v2 = input().split()
                tup1 = (int(v1),int(v2))
                arr.append(tup1)
            print("values are %s" %arr)
            #value = [200, 100, 120, 60,0,1]
            #weight = [10, 20, 30, 40,0,1]
            #w = 70
            sub_arr = sub_lists([[]],arr,0,[])
            value = []
            for val in sub_arr:
                value1 = []
                weight1 = []
                for val1 in val:
                    value1.append(val1[1])
                    weight1.append(val1[0])
                tup2 = (value1,weight1)
                value.append((tup2))
            for var in value:
                if var[1] > w:
                    value.remove(var)
            value2 = []
            for var in value:
                value2.appen(var[0])
            print(value2.sort()[-1])



