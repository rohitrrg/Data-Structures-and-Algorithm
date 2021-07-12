def findMean(arr, queries, n, q): 
        # Complete the function
        b = []
        for i in range(0,q,2):
            print(queries[i], queries[i+1])
            for j in range(queries[i], queries[i+1]+1):
                print(j)

arr = [1,2,3,4,5]
queries = [0,2,1,3,0,4]

findMean(arr, queries=queries, n=5, q=6)