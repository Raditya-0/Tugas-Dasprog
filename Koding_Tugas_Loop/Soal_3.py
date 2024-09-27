while True:
    try:
        susunan = input("Masukkan Susunan batunya: ").strip()
        if not susunan.isalpha():
            print("Input harus berupa string yang terdiri dari huruf.")
        else:
            break
    except ValueError:
        print("Input harus berupa string yang terdiri dari huruf.")
        continue

stack = []
kerugian = 0

for batu in susunan:
    if stack and stack[-1] == batu:
        stack.pop() 
        kerugian += ord(batu) * 1000 * 2  
    else:
        stack.append(batu)

if kerugian > 0:
    print(f"Di gudang tersisa {len(stack)} batu")
    print(f"Total Kerugian: {kerugian} Dolar Imbu")
else:
    print(f"Di gudang tersisa {len(stack)} batu")
    print("Wah, Jotaro Joemama tidak jadi dipecat")

