def find_all_path(dict,start_vertex, end_vertex, path=[]):
    extended_path = None
    paths = []
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return [path]
    if start_vertex not in dict:
        return []
    for node in dict[start_vertex]:
        if node not in path:
            extended_path = find_all_path(dict,node, end_vertex, path)
            for p in extended_path:
                paths.append(p)
    return paths

if __name__ == "__main__":
    print("Enter no of testcases: ")
    t = int(input())
    if t>=1 and t<=100:
        for y in range(0,t):
            matrix = []
            print("\n")
            print("Enter n and m: ")
            row,column = input().split()
            row = int(row)
            column = int(column)
            if row <= 20 and row >= 1 and column <= 20 and column >= 1:
                print("next %s X %s space seprated values, where value is either 0 or 1" %(row,column))
                val = input().split()
                for i in range(row):
                    arr = []
                    for j in range(column):
                        arr.append(int(val[0]))
                        del val[0]
                    matrix.append(arr)
                #print(matrix)
                print("Enter destination index")
                n, m = input().split()
                n = int(n)
                m = int(m)
                destination = (n,m)
                dict = {}
                for k in range(row):
                    for l in range(column):
                        dict[(k, l)] = []
                        if (l - 1) >= 0:
                            if matrix[k][(l - 1)] == 1:
                                dict[(k, l)].append((k, l - 1))
                        if (l + 1) <= (column - 1):
                            if matrix[k][(l + 1)] == 1:
                                dict[(k, l)].append((k, l + 1))
                        if (k - 1) >= 0:
                            if matrix[(k - 1)][l] == 1:
                                dict[(k, l)].append((k - 1, l))
                        if (k + 1) <= (row - 1):
                            if matrix[(k + 1)][l] == 1:
                                dict[(k, l)].append((k + 1, l))
                #print(dict)
                paths = find_all_path(dict,(0,0),destination)
                paths = sorted(paths,key=len)
                res_path = []
                if len(paths)>=1:
                    res_path = paths[0]
                if res_path == [] or destination not in res_path:
                    print("-1")
                else:
                    print(len(res_path)-1)
            else:
                print("value of n and m is not in range- 1<=n,m<=20")

