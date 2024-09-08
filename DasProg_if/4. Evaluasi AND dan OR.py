if __name__ == "__main__":
    # Pengujian &&
    print("Pengujian &&")
    while True:
        # Meminta input dari pengguna
        input_str = input("Masukkan 'T' untuk true atau 'F' untuk false: ").strip().upper()

        # Memeriksa input dan memberikan respons
        if input_str == 'T':
            result1 = 1
            break
        elif input_str == 'F':
            result1 = 0
            break
        else:
            print("Input tidak valid, masukkan 'T' untuk true atau 'F' untuk false.")
    
    if result1:
        print("fun2 performed")
        result1 = 1
    if result1:
        print("Test of && complete")

    # Pengujian ||
    print("Pengujian ||")
    while True:
        # Meminta input dari pengguna
        input_str = input("Masukkan 'T' untuk true atau 'F' untuk false: ").strip().upper()

        # Memeriksa input dan memberikan respons
        if input_str == 'T':
            result2 = 1
            break
        elif input_str == 'F':
            result2 = 0
            break
        else:
            print("Input tidak valid, masukkan 'T' untuk true atau 'F' untuk false.")
    
    if result2 == 0:
        print("fun2 performed")
        result2 = 1
    if result2:
        print("Test of || complete")
