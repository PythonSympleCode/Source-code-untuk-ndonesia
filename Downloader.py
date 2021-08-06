
pilihan = 'y'
while(pilihan == 'y'):
    
    from tqdm import tqdm
    from time import sleep
    import os

    print("==================================================================")
    print("")
    print("Selamat datang di File downloader")
    print("Silahkan pilih jenis file yang ingin di download")
    print("")
    print("")
    print("1. Txt File")
    print("2. File PY")
    print("3. File JSON")
    print("4. Jenis file lain")
    print("")
    option = input("Option: ")

    if option == '1':
        print("===============================================================")
        print("")
        nama_txt_file=input("Masukkan nama untuk file txt anda: ")
        text_didalam_txt_file=input("Masukkan text yang ingin anda masukkan ke Txt file anda: ")

        f = open(f"C:/Users/Gadget House/Documents/{nama_txt_file}.txt","a")

        f.write(text_didalam_txt_file)

        f.close()
        print("")
        print("File anda telah terdownload di Document")

    elif option =='2':
        print("================================================")
        print()
        nama_py_file=input("Masukkan nama untuk File PY anda: ")

        f2 = open(f"C:/Users/Gadget House/Documents/{nama_py_file}.py","a")

        print("")
        print("File anda telah terdownload di Document")

    elif option=='3':
        nama_json_file=input("Masukkan nama untuk File JSON anda: ")

        f3 = open(f"C:/Users/Gadget House/Documents/{nama_json_file}.json","a")

        f3.close()

    elif option =='4':
        print("===============================================")
        print()
        nama_file_lain=input("Masukkan nama file: ")
        jenis_file=input("Masukkan jenis file: ")

        f4 = open(f"C:/Users/Gadget House/Documents/{nama_file_lain}.{jenis_file}","a")

        f4.close()

        print("")
        print("File anda telah terdownload di Document")

    else:
        print("")
        print("Nonimal tidak di ketahui")

    print("================================================")
    pilihan = input("Apakah anda ingin mendownload file lagi (y/n)?")
    print("================================================")

    if pilihan == 'n':
        break