if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        cmd = input().strip().split()
        action = cmd[0]

        if action == "insert":
            arr.insert(int(cmd[1]), int(cmd[2]))
        elif action == "print":
            print(arr)
        elif action == "remove":
            arr.remove(int(cmd[1]))
        elif action == "append":
            arr.append(int(cmd[1]))
        elif action == "sort":
            arr.sort()
        elif action == "pop":
            arr.pop()
        elif action == "reverse":
            arr.reverse()