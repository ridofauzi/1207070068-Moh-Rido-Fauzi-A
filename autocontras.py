import numpy as np #import library numpy dan di-assign sebagai "np"
import cv2 #import library opencv dan di-assign sebagai "cv2"
import matplotlib.pyplot as plt #import library matplotlib dan di-assign sebagai "plt"

img = cv2.imread ("mario.jpg") #membaca gambar dengan menggunakan opencv dan meng-assign ke variabel "img"
img_hight= img.shape[0] #mengambil tinggi gambar dan di-assign ke variabel "img_hight"
img_width= img.shape[1] #mengambil lebar gambar dan di-assign ke variabel "img_width"
img_chanel= img.shape[2] #mengambil channel gambar dan di-assign ke variabel "img_chanel"
img_type= img.dtype #mengambil tipe data gambar dan di-assign ke variabel "img_type"

#kontras
img_contras = np.zeros(img.shape, dtype= np.uint8) #membuat matriks nol dengan dimensi yang sama dengan gambar dan di-assign ke variabel "img_contras"
def contrass(nilai): #membuat fungsi dengan parameter "nilai"
    for y in range(0, img_hight): #membuat perulangan for loop dari 0 hingga tinggi gambar
        for x in range(0, img_width): #membuat perulangan for loop dari 0 hingga lebar gambar
            red = img[y][x][0] #mengambil nilai piksel merah pada posisi (y,x) dan di-assign ke variabel "red"
            green = img[y][x][1] #mengambil nilai piksel hijau pada posisi (y,x) dan di-assign ke variabel "green"
            blue = img[y][x][2] #mengambil nilai piksel biru pada posisi (y,x) dan di-assign ke variabel "blue"
            gray = (int(red)+int(green)+int(blue))/3 #menghitung nilai keabuan dengan rata-rata dari tiga channel warna
            gray *= nilai #menambahkan nilai kontras
            if gray > 255: #jika nilai keabuan lebih dari 255, maka
                gray = 255 #nilai keabuan di-assign sebagai 255
                img_contras[y][x] = (gray, gray, gray) #nilai piksel pada posisi (y,x) di-assign dengan nilai keabuan yang telah dihitung

#menampilkan
contrass(20) #memanggil fungsi "contrass" dengan nilai parameter 20
plt.imshow(img_contras) #menampilkan gambar menggunakan matplotlib
plt.title("contrass 20") #mengatur judul plot
plt.show() #menampilkan plot

contrass(100) #memanggil fungsi "contrass" dengan nilai parameter 100
plt.imshow(img_contras) #menampilkan gambar menggunakan matplotlib
plt.title("contrass 100") #mengatur judul plot
plt.show() #menampilkan plot       

img_contrast_rgb = np.zeros(img.shape, dtype=np.uint8)  # Membuat array kosong dengan ukuran yang sama dengan gambar untuk menyimpan hasil kontras RGB

def rgb_contrast(nilai):
    for y in range(0, img_hight):
        for x in range(0, img_width):
            red = img[y][x][0]  # Mendapatkan nilai komponen merah pada piksel (y, x)
            red += nilai  # Menambahkan nilai kontras ke komponen merah
            if red > 255:
                red = 255  # Memastikan nilai komponen merah tidak melebihi 255 (batas maksimum)
            green = img[y][x][1]  # Mendapatkan nilai komponen hijau pada piksel (y, x)
            green += nilai  # Menambahkan nilai kontras ke komponen hijau
            if green > 255:
                green = 255  # Memastikan nilai komponen hijau tidak melebihi 255 (batas maksimum)
            blue = img[y][x][2]  # Mendapatkan nilai komponen biru pada piksel (y, x)
            blue += nilai  # Menambahkan nilai kontras ke komponen biru
            if blue > 255:
                blue = 255  # Memastikan nilai komponen biru tidak melebihi 255 (batas maksimum)
            img_contrast_rgb[y][x] = (red, green, blue)  # Menyimpan nilai kontras RGB pada array hasil

rgb_contrast(20)  # Menerapkan kontras 20 pada gambar
plt.imshow(img_contrast_rgb)  # Menampilkan gambar dengan kontras 20
plt.title("kontras 20")  # Memberikan judul pada plot
plt.show()

rgb_contrast(100)  # Menerapkan kontras 100 pada gambar
plt.imshow(img_contrast_rgb)  # Menampilkan gambar dengan kontras 100
plt.title("kontras 100")  # Memberikan judul pada plot
plt.show()

img_auto_contrast = np.zeros(img.shape, dtype=np.uint8)  # Membuat array kosong dengan ukuran yang sama dengan gambar untuk menyimpan hasil kontras otomatis

def auto_contrast():
    xmax = 200  # Inisialisasi nilai maksimum awal
    xmin = 0  # Inisialisasi nilai minimum awal
    d = 0  # Inisialisasi rentang kontras awal
    # Menghitung nilai maksimum dan minimum dari nilai keabuan
    for y in range(0, img_hight):
        for x in range(0, img_width):
            red = img[y][x][0]  # Mendapatkan nilai komponen merah pada piksel (y, x)
            green = img[y][x][1]  # Mendapatkan nilai komponen hijau pada piksel (y, x)
            blue = img[y][x][2]  # Mendapatkan nilai komponen biru pada piksel (y, x)
            gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung nilai keabuan dengan rata-rata komponen RGB
            if gray < xmax:
                xmax = gray  # Mengupdate nilai maksimum jika nilai keabuan lebih kecil dari xmax
            if gray > xmin:
                xmin = gray  # Mengupdate nilai minimum jika nilai keabuan lebih besar dari xmin

    d = xmin - xmax  # Menghitung rentang kontras

    # Mengaplikasikan kontras otomatis pada gambar
    for y in range(0, img_hight):
        for x in range(0, img_width):
            red = img[y][x][0]  # Mendapatkan nilai komponen merah pada piksel (y, x)
            green = img[y][x][1]  # Mendapatkan nilai komponen hijau pada piksel (y, x)
            blue = img[y][x][2]  # Mendapatkan nilai komponen biru pada piksel (y, x)
            gray = (int(red) + int(green) + int(blue)) / 3  # Menghitung nilai keabuan dengan rata-rata komponen RGB
            gray = int(float(255 / d) * (gray - xmax))  # Menghitung nilai keabuan baru dengan kontras otomatis
            img_auto_contrast[y][x] = (gray, gray, gray)  # Menyimpan nilai keabuan baru pada array hasil

auto_contrast()  # Menerapkan kontras otomatis pada gambar
plt.imshow(img_auto_contrast)  # Menampilkan gambar dengan kontras otomatis
plt.title("Kontras Otomatis")  # Memberikan judul pada plot
plt.show()
