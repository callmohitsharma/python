#1- Loop over value array and compare value of each element with previous element
#if value is more then previous value take this value and continue the operation
#Step1 will give the Max value and its location.
#2- start the weight of this value and compare it with W if less then keep it and replace val and wt value in both the array with 0
#and move to step1 again.
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

if __name__ == "__main__":
    value = []
    weight = []
    #print("Enter no of testcases: ")
    t = int(input())
    if t>=1 and t<=20:
        for y in range(0,t):
            #print("Enter capacity and no of values: ")
            w,n = input().split()
            #print("next %s lines, where each line contains 2 numbers weight and value" % n)
            for i in range(int(n)):
                v1, v2 = input().split()
                value.append(int(v2))
                weight.append(int(v1))

            #print("values are %s" %value)
            #value = [200, 100, 120, 60,0,1]
            #weight = [10, 20, 30, 40,0,1]
            #w = 70
            val_arr = []
            weight_arr = []
            if len(value) == len(weight):
                val_arr,weight_arr = compare_weight(value,weight,val_arr,weight_arr,w)
                #print(sum(val_arr))
                print("Sub array is %s and max value achieved is %s, weight arrar is %s and total weight is %s" %(val_arr,sum(val_arr),weight_arr, sum(weight_arr)))
            else:
                print("length of value list and weignt list is not same")


