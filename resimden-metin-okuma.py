import cv2
#OpenCV (Open Source Computer Vision) açık kaynak kodlu görüntü işleme kütüphanesidir.
import numpy as np
#NumPy (Numerical Python) bilimsel hesaplamaları hızlı bir şekilde yapmamızı sağlayan bir matematik kütüphanesidir.
from PIL import Image
#Python Image Library, Python Resim Kütüphanesi, Pythonda image işlemlerini kolayca yapabilmek için geliştirilmiş kütüphanedir.
import pytesseract
# kütüphaneleri ekledik

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
# burada tesseract yazıları için adres tanımladık bu sayede tesseract'a ulaştık

kaynak_yolu="C:\\Users\\acabo\\Desktop\\yapayresim"
# kaynak yolu bize renkli resim var ise onu temizleyip kaydetme işlemi için de geçerli olan bölüme ekleme yapmak için

def metin_oku(img_yolu):
    img=cv2.imread(img_yolu)
    #resme erişim sağlar

    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #resmi gri tonuna çevirir


    kernel=np.ones((1,1),np.uint8)
    #(1,1) dizinin şekli
    #dizi için istenilen veri tipi
    img=cv2.erode(img,kernel,iterations=1)
    #Bir görüntünün özelliklerini azaltmak için kullanılır. erozyon

    img = cv2.dilate(img, kernel, iterations=1)
    # resmi gürültüsünü azaltma için kullanıyor. dilatasyon
    # Görüntüdeki beyaz bölgeyi arttırır veya ön plandaki nesnenin büyüklüğü artar

    img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2)
    # resimlerdeki renkli resimleri siyah hale getiriyor

    cv2.imwrite(kaynak_yolu+'gurultusuz.png',img)
    # gürültüsüz resmi kaynak yoluna belirlediğimiz adrese gürültüsüz.png olarak yazdırır

    sonuc=pytesseract.image_to_string(Image.open(kaynak_yolu+'gurultusuz.png'),lang='tur')
    #tesseract ile yazıyı okuyor ve sonuc değişkenine atama yapıyor

    return sonuc
    # buradan da fonksiyondan değeri döndürme işlemi yapılır
print("---------------------------------")
print("metin okuma")
# bilgilendirme veriliyor yapılan işlem için
print("---------------------------------")
# okunacak metini karıştırmamak için
print(metin_oku('el_yazisi_resim\\a01-000u-s00-00.png'))
# okunacak resmin dosya yolunu girerek ulaşabilir.
print("---------------------------------")
print("tamamlandı")
