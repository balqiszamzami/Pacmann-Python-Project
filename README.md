# Pacmann Python Project : *self-service cashier*

## Latar Belakang Problems
Dalam menjalankan bisnisnya, Andi mengalami masalah dalam proses pembayaran di toko offlinenya. Karena keterbatasan pegawai yang ada, antrian pembayaran seringkali cukup panjang, sehingga membuat pelanggan merasa tidak nyaman dan memakan waktu yang cukup lama. Selain itu, Andi juga ingin memberikan pilihan kepada pelanggan yang tidak bisa langsung berbelanja di toko offlinenya tetap dapat berbelanja, sehingga sistem self-service cashier menjadi alternatif yang tepat.

Solusi yang diberikan yaitu dengan membuat sistem self-service cashier yang mudah digunakan oleh pelanggan dan memudahkan proses pembayaran di toko offline. Pelanggan dapat memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli melalui aplikasi atau mesin kasir yang disediakan. Dengan adanya sistem self-service cashier, pelanggan dapat memproses pembayaran dengan cepat dan tidak perlu menunggu lama di antrian pembayaran. Selain itu, sistem kasir self-service juga mempermudah pelanggan yang tidak dapat berbelanja langsung di toko offline.

## Requirements or Objective
Pembuatan sistem self-service cashier yang dapat digunakan oleh pelanggan untuk melakukan pembelian barang secara mandiri di supermarket. Sistem ini harus dapat menerima input berupa nama item, jumlah item, dan harga item yang dibeli oleh pelanggan. Selain itu, sistem juga harus dapat menampilkan transaksi, menghitung total harga, dan memverifikasi apakah pemesanan sudah benar.
- Membuat proses `tambah item` barang yang ingin dibeli.
- Membuat proses `hapus item` barang barang yang ingin dibeli.
- Membuat proses `edit nama item` barang barang yang ingin dibeli.
- Membuat proses `edit jumlah item` barang barang yang ingin dibeli. 
- Membuat proses `edit harga item` barang barang yang ingin dibeli.
- Membuat proses `hitung total harga item` barang barang yang ingin dibeli.
- Membuat proses `hitung diskon item` barang barang yang ingin dibeli.
- Membuat proses `kosongkan barang` barang yang ingin dibeli.
- Mengecek barang yang ingin dibeli dengan `menampilkan seluruh barang`.

## Flowchart
![Flowchart](https://user-images.githubusercontent.com/115378082/231020885-5bd0c819-6d45-4570-abdd-3167bf348985.jpg)

## Penjelasan
### Penjelasan Code
1. Class Transaction :
    + Merupakan class untuk menyimpan dan mengelola item-item transaksi.
    + Memiliki method untuk menambah, mengubah, dan menghapus item, serta menampilkan dan menghitung total harga transaksi.
        
2. def init(self):
    + Method untuk menginisialisasi items sebagai sebuah list kosong.
        
3. def add_item(self, item):
    + Method untuk menambahkan item baru ke dalam list items.
    
4. def update_item_name(self, old_name, new_name):
    + Method untuk mengubah nama item yang sudah ada dalam list items.
        
5. def update_item_qty(self, name, new_qty):
    + Method untuk mengubah jumlah item yang sudah ada dalam list items.
   
6. def update_item_price(self, name, new_price):
    + Method untuk mengubah harga item yang sudah ada dalam list items.
    
7. def delete_item(self, name):
    + Method untuk menghapus item yang sudah ada dalam list items.
    
8. def reset_transaction(self):
    + Method untuk menghapus semua item dalam list items.
    
9. def check_order(self):
    + Method untuk memeriksa apakah pemesanan sudah benar atau terdapat kesalahan input data.
    
10. def show_order(self):
    + Method untuk menampilkan seluruh item yang ada dalam list items.
    
11. def total_price(self):
    + Method untuk menghitung total harga transaksi berdasarkan jumlah item dan harga setiap item.
 
### Penjelasan alur program
- Program memulai dengan membuat instance dari class Transaction.
- Program menampilkan menu utama dengan 8 pilihan, yaitu Tambahkan item, Ubah nama item, Hapus item, Tampilkan transaksi, Hitung total transaksi, Reset transaksi, Cek order, dan Keluar.
- Program meminta user untuk memilih salah satu dari 8 pilihan tersebut.
- Jika user memilih "Tambahkan item", program akan meminta user untuk memasukkan nama item, jumlah item, dan harga item. Kemudian program akan memanggil method `add_item` dari instance Transaction dan menambahkan item ke dalam daftar items.
- Jika user memilih "Ubah nama item", program akan meminta user untuk memasukkan nama item lama dan nama item baru. Kemudian program akan memanggil method `update_item_name` dari instance Transaction dan mengubah nama item yang lama menjadi nama item yang baru.
- Jika user memilih "Hapus item", program akan meminta user untuk memasukkan nama item yang ingin dihapus. Kemudian program akan memanggil method `delete_item` dari instance Transaction dan menghapus item yang memiliki nama yang sama dengan nama item yang dimasukkan oleh user.
- Jika user memilih "Tampilkan transaksi", program akan memanggil method `show_order` dari instance Transaction dan menampilkan daftar semua item yang telah dimasukkan oleh user beserta jumlah item, harga item, dan total harga.
- Jika user memilih "Hitung total transaksi", program akan memanggil method `total_price` dari instance Transaction dan menampilkan total harga dari semua item yang telah dimasukkan oleh user beserta diskon yang didapat jika total harga melebihi batas tertentu.
- Jika user memilih "Reset transaksi", program akan menghapus semua item dengan method `reset_transaction`
- Jika user memilih "Cek order", program akan memanggil method `check_order` dari instance Transaction dan mengecek apakah semua item yang telah dimasukkan oleh user memiliki nilai yang valid (tidak ada nilai yang kosong atau negatif). Jika semua item valid, program akan memanggil method `show_order` untuk menampilkan daftar semua item. Jika terdapat item yang tidak valid, program akan menampilkan pesan kesalahan.
- Jika user memilih "Keluar", program akan menampilkan pesan terima kasih dan keluar dari program.
  
## Test Case
1. Test 1 : `add_item()` <br>
Pelanggan ingin menambahkan dua item baru menggunakan method `add_item()`. Item yang ditambahkan adalah sebagai berikut :
    - Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
    - Nama Item: Pasta Gigi, Qty: 3, Harga: 15000 
![Test 1](https://user-images.githubusercontent.com/115378082/231023022-9f1bf4d9-d89c-4405-9545-2f06c08d5f0d.jpg)

2. Test 2 : `delete_item()` <br>
Ternyata pelanggan salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka pelanggan menggukan method `delete_item()` untuk menghapus item. Item yang ingin dihapus adalah **Pasta Gigi**.
![Test 2](https://user-images.githubusercontent.com/115378082/231023028-732b4d64-114e-4e74-b264-91c1108fb580.jpg)

3. Test 3 : `reset_transaction()` <br>
Ternyata setelah dipikir-pikir, pelanggan salah memasukkan item yang ingin dibeli! Daripada menghapusnya satu - satu, maka pelanggan cukup menggunakan method `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.
![Test 3](https://user-images.githubusercontent.com/115378082/231023031-db186969-6dd4-4c94-8c03-e2a6434f4e17.jpg)

4. Test 4 : `total_price()` <br>
Setelah pelanggan selesai berbelanja, program akan menghitung total belanja yang harus dibayarkan menggunakan method `total_price()`. <br>
![Test 4](https://user-images.githubusercontent.com/115378082/231023035-817829b6-6ef8-43bb-9d96-3caf82bb34d4.jpg)

5. Test 5 : `check_order()` <br>
Pelanggan ingin memastikan barang yang ingin dibeli dengan menggunakan method `check_order` pelanggan dapat mengetahui apakah pemesanannya sudah benar atau belum.
![Test 5](https://user-images.githubusercontent.com/115378082/231023037-fae1884c-4dd6-431e-90d9-da3a37e9b3da.jpg)

6. Test 6 : `update_item_name()` & `show_order()` <br>
Pelanggan ingin mengubah nama item barang yang ingin dibeli, program akan mengubah nama barang yang sudah ditambahkan dengan menggunakan method `update_item_name()` sekaligus ingin melihat apakah nama item barang yang ingin dibeli sudah berubah atau belum dengan method `show_order()`. <br>
![Test 6](https://user-images.githubusercontent.com/115378082/231023042-14665259-ff60-43e2-ab35-9fe259f814a7.jpg)

7. Test 7 : `Keluar` <br>
Pelanggan telah selesai belanja, maka pilihan `keluar` akan mengakhiri program self-service cashier.
![Test 7](https://user-images.githubusercontent.com/115378082/231023044-4a8800d2-ea82-4c48-969a-4b9f3d93d033.jpg)

## Conclusion & Future Work
Pada setiap pilihan, program menggunakan metode yang telah didefinisikan sebelumnya di kelas Transaction. Dalam kelas Transaction, metode ini melakukan operasi yang diperlukan seperti menambahkan item, mengubah nama item, menghapus item, menampilkan transaksi, menghitung total harga transaksi, mereset transaksi, dan memeriksa pesanan. Secara keseluruhan, program ini cukup sederhana namun dapat berguna dalam manajemen transaksi kecil. Program dapat ditingkatkan dengan menambahkan fitur-fitur baru lainnya.

Future Work :
  + Penanganan Kesalahan Input yang Lebih Baik. Program saat ini belum cukup kuat untuk menangani kesalahan input. Sebagai contoh, jika pengguna mencoba memasukkan harga atau jumlah item dalam bentuk string, program akan gagal. Menambahkan penanganan kesalahan input yang lebih baik akan memungkinkan program lebih mudah digunakan dan lebih andal.
  + Implementasi fitur diskon khusus untuk produk tertentu. Saat ini, diskon yang diberikan berdasarkan total belanja. Namun, dapat dikembangkan fitur diskon yang diberikan khusus untuk produk tertentu. Misalnya, memberikan diskon untuk pembelian produk dengan kuantitas tertentu.
  + Penambahan fitur pencarian item. Jika daftar item sudah cukup panjang, pencarian item akan sangat membantu pengguna dalam mencari dan mengedit item tertentu.
  + Penyimpanan data transaksi. Saat ini program hanya dapat digunakan untuk satu kali transaksi. Agar lebih berguna dan memudahkan pengguna, bisa ditambahkan fitur penyimpanan data transaksi. Pengguna dapat melihat riwayat transaksi sebelumnya dan melacak pengeluaran mereka dari waktu ke waktu.
  + Implementasi fitur checkout. Fitur ini dapat memberikan kemudahan bagi pengguna untuk membayar pesanan mereka secara online, tanpa harus keluar dari program. Hal ini dapat meningkatkan pengalaman pengguna dan kemungkinan keuntungan bagi bisnis yang menggunakan program ini.
  + Menambahkan GUI. Menambahkan antarmuka pengguna grafis (GUI) dapat membuat program lebih mudah digunakan dan lebih menarik secara visual. Ini dapat memungkinkan pengguna untuk melakukan operasi pada transaksi dengan lebih mudah dan intuitif.
