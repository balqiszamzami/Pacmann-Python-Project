from script import Transaction

test = Transaction()

while True:
    print("Main Menu :")
    print("1. Tambahkan item")
    print("2. Ubah nama item")
    print("3. Hapus item")
    print("4. Tampilkan transaksi")
    print("5. Hitung total transaksi")
    print("6. Reset transaksi")
    print("7. Cek order")
    print("0. Keluar")
    choice = input("Masukkan pilihan: ")

    if choice == '1':
        name = input("Nama item: ")
        qty = int(input("Jumlah item: "))
        price = int(input("Harga item: "))
        test.add_item([name, qty, price])

    elif choice == '2':
        old_name = input("Nama item yang akan diubah: ")
        new_name = input("Nama baru: ")
        test.update_item_name(old_name, new_name)

    elif choice == '3':
        name = input("Nama item yang akan dihapus: ")
        test.delete_item(name)

    elif choice == '4':
        test.show_order()

    elif choice == '5':
        test.total_price()

    elif choice == '6':
        test.reset_transaction()
        print("Semua item berhasil di delete!")

    elif choice == '7':
        test.check_order()

    elif choice == '0':
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak tersedia. Silakan pilih kembali.")
