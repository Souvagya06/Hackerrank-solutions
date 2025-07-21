if __name__ == '__main__':
    n = int(input())          #Total no. of elements
    arr = list(map(int, input().split()))         #taking the elements from the user
    m = list(set(arr))          #list(set(arr)) to remove duplicate elements
    m.sort()                    #sorting the list with no duplicate elements
    print (m[-2])               #printfing the runner-up score
