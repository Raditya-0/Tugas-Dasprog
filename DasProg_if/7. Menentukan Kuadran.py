def tentukan_posisi(x, y):
    if x == 0 and y == 0:
        return "Titik berada di pusat koordinat"
    elif x == 0:
        return "Titik berada di sumbu y"
    elif y == 0:
        return "Titik berada di sumbu x"
    elif x > 0 and y > 0:
        return "Titik berada di kuadran I"
    elif x < 0 and y > 0:
        return "Titik berada di kuadran II"
    elif x < 0 and y < 0:
        return "Titik berada di kuadran III"
    elif x > 0 and y < 0:
        return "Titik berada di kuadran IV"

def main():
    while True:
       try:
           x,y = map(float, input("Masukkan koordinat x dan y (pisahkan dengan spasi) : ").split())
           posisi = tentukan_posisi(x, y)
           print(f"({x}, {y}) adalah {posisi}")
           break
       except ValueError:
           print("Input tidak valid. Masukkan angka yang benar.")

if __name__ == "__main__":
    main()
