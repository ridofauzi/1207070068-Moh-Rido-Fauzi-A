#Memanggil Library
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Mengambil gambar menggunakan cv2.imread
img = cv2.imread("mario.jpg")

# Mendapatkan tinggi, lebar, jumlah channel, dan tipe data gambar
img_height = img.shape[0]
img_width = img.shape[1]
img_channels = img.shape[2]
img_type = img.dtype

# Membuat array kosong dengan ukuran dan tipe data yang sama dengan gambar asli
img_brightness = np.zeros(img.shape, dtype=np.uint8)

# Fungsi Q untuk menyesuaikan kecerahan dengan nilai yang diberikan
def Q(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Mendapatkan nilai warna merah, hijau, dan biru pada pixel
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            
            # Menghitung nilai keabuan sebagai rata-rata dari merah, hijau, dan biru
            gray = (int(red) + int(green) + int(blue)) / 3
            
            # Menambahkan nilai yang diberikan ke nilai keabuan
            gray += nilai
            
            # Membatasi nilai keabuan dalam rentang [0, 255]
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            
            # Mengatur nilai piksel pada gambar baru
            img_brightness[y][x] = (gray, gray, gray)

# Menyesuaikan kecerahan dengan nilai -100 dan menampilkan gambar
Q(-100)
plt.imshow(img_brightness)
plt.title("Kecerahan -100")
plt.show()

# Menyesuaikan kecerahan dengan nilai 20 dan menampilkan gambar
Q(20)
plt.imshow(img_brightness)
plt.title("Kecerahan 20")
plt.show()

# Membuat array baru yang kosong dengan channel RGB
img_Q = np.zeros(img.shape, dtype=np.uint8)

# Mendefinisikan kembali fungsi Q untuk menyesuaikan masing-masing channel RGB secara terpisah
def Q(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Menyesuaikan masing-masing channel RGB dengan nilai yang diberikan
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            
            # Mengatur nilai piksel pada gambar baru
            img_Q[y][x] = (red, green, blue)

# Menyesuaikan kecerahan dengan nilai -100 dan menampilkan gambar
Q(-100)
plt.imshow(img_Q)
plt.title("Kecerahan -100")
plt.show()

# Menyesuaikan kecerahan dengan nilai 100 dan menampilkan gambar
Q(100)
plt.imshow(img_Q)
plt.title("Brightness 100")
plt.show()
