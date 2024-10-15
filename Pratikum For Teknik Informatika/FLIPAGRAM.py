n = int(input())
inputs = []
for _ in range(n):
    inputs.append(input().split())
        
for cmd, strA, strB in inputs:
    if cmd == "FLIP":
        if strA == strB[::-1]:
            print(f"Flip {strA} to get {strB}")
        else:
            print("This cannot lah bro")
    elif cmd == "ANAGRAM":
        if sorted(strA) == sorted(strB):
            print(f"Hhm {strA} can be arranged into {strB}")
        else:
            print("This cannot lah bro")
