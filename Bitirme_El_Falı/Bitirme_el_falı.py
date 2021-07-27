from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

dizix1 = []
dizix2 = []
diziy1 = []
diziy2 = []
fark = []
fark2 = []
fark3 = []
fal1=0
fal2=0
fal3=0
fal4=0
fal5=0

img = Image.open("images/sondeneme (2).png")
width, height = img.size
area_avuçiçi = (0,int(height)/2,int(width),int(height/1.25))
area_1parmak = (0,0,(1.15*int(width))/5,int(height/2))
area_2parmak = ((int(width))/5,0,(2.35*int(width))/5,int(height/2))
area_3parmak = ((2.35 * int(width))/5,0,(3.50 * int(width))/5,int(height/2))
area_4parmak = ((3.50 * int(width))/5,0,int(width),int(height/2))



img_avucici = img.crop(area_avuçiçi)
img1 = img.crop(area_1parmak)
img2 = img.crop(area_2parmak)
img3 = img.crop(area_3parmak)
img4 = img.crop(area_4parmak)


img_avucici.save("images/sero1.png")
img1.save("images/sero2.png")
img2.save("images/sero3.png")
img3.save("images/sero4.png")
img4.save("images/sero5.png")

iimg_avucici = r'images/sero1.png'
iimg1 = r'images/sero2.png'
iimg2 = r'images/sero3.png'
iimg3 = r'images/sero4.png'
iimg4 = r'images/sero5.png'

plt.subplot(2,4,1), plt.imshow(img)
plt.subplot(2,4,4), plt.imshow(img_avucici)
plt.subplot(2,4,5), plt.imshow(img1)
plt.subplot(2,4,6), plt.imshow(img2)
plt.subplot(2,4,7), plt.imshow(img3)
plt.subplot(2,4,8), plt.imshow(img4)
plt.show()

#İLK PARMAK İÇİN YAPILACAK İŞLEMLER
img1_1 = cv.imread(iimg1)
gray_img1_5 = cv.cvtColor(img1_1, cv.COLOR_BGR2GRAY)
(thresh1, output1) = cv.threshold(gray_img1_5, 79, 255, cv.THRESH_BINARY)
output1 = cv.GaussianBlur(gray_img1_5, (5, 5), 3)
output1 = cv.Canny(output1, 0, 95)
plt.imshow(output1)
plt.show()

img1_1_height = img1_1.shape[0]
img1_1_width = img1_1.shape[1]
#resmin sağ tarafına maskelem işlemi yapar
contours = np.array([[0, 0], [0,img1_1_height], [(6*img1_1_width)/8, img1_1_height], [(6*img1_1_width)/8,0]])
mask = np.zeros_like(output1)
cv.fillPoly(mask, np.array([contours], dtype=np.int32), 255)
masked_img1_1 = cv.bitwise_and(output1, mask)

#resmin sol tarafına maskeleme işlemi yapar
contours2 = np.array([[(2*img1_1_width)/8, 0], [(2*img1_1_width)/8,img1_1_height], [(img1_1_width), img1_1_height], [(img1_1_width),0]])
mask2 = np.zeros_like(masked_img1_1)
cv.fillPoly(mask2, np.array([contours2], dtype=np.int32), 255)
masked_img1_1_2 = cv.bitwise_and(masked_img1_1, mask2)

plt.imshow(masked_img1_1_2)
plt.show()
lines = cv.HoughLinesP(masked_img1_1_2, 5, np.pi / 280, 30)
for line in lines:
	x1, y1, x2, y2 = line[0]
	dizix1.append(x1)
	dizix2.append(x2)
	diziy1.append(y1)
	diziy2.append(y2)
	cv.line(img1_1, (x1, y1), (x2, y2), (0, 255, 0), 2)

for a in dizix1:
	for b in dizix2:
		fark.append(abs(a-b))

for c in diziy1:
	for d in diziy2:
		fark2.append(abs(c-d))

for i in range(len(diziy1)):
		fark3.append(int((fark2[i] ** 2) + (fark[i] ** 2)) ** 0.5)
fark3.sort()
fark3.reverse()
fal1 = fark3[0]

dizix1.clear()
dizix2.clear()
diziy1.clear()
diziy2.clear()
fark.clear()
fark2.clear()
fark3.clear()

plt.imshow(img1_1)
plt.show()


#İKİNCİ PARMAK İÇİN YAPILACAKLAR
img1_2 = cv.imread(iimg2)
gray_img1_2 = cv.cvtColor(img1_2, cv.COLOR_BGR2GRAY)
(thresh2, output2) = cv.threshold(gray_img1_2, 95, 255, cv.THRESH_BINARY)
output2 = cv.GaussianBlur(gray_img1_2, (5, 5), 3)
output2 = cv.Canny(output2, 0, 75)
plt.imshow(output2)
plt.show()

img1_2_height = img1_2.shape[0]
img1_2_width = img1_2.shape[1]
#resmin sağ tarafına maskelem işlemi yapar
contours3 = np.array([[0, 0], [0,img1_2_height], [(6*img1_2_width)/8, img1_2_height], [(6*img1_2_width)/8,0]])
mask3 = np.zeros_like(output2)
cv.fillPoly(mask3, np.array([contours3], dtype=np.int32), 255)
masked_img1_2 = cv.bitwise_and(output2, mask3)

#resmin sol tarafına maskeleme işlemi yapar
contours4 = np.array([[(2*img1_2_width)/8, 0], [(2*img1_2_width)/8,img1_2_height], [(img1_2_width), img1_2_height], [(img1_2_width),0]])
mask4 = np.zeros_like(masked_img1_2)
cv.fillPoly(mask4, np.array([contours4], dtype=np.int32), 255)
masked_img1_2_2 = cv.bitwise_and(masked_img1_2, mask4)

plt.imshow(masked_img1_2_2)
plt.show()
lines = cv.HoughLinesP(masked_img1_2_2, 5, np.pi / 280, 30)
for line in lines:
	x1, y1, x2, y2 = line[0]
	dizix1.append(x1)
	dizix2.append(x2)
	diziy1.append(y1)
	diziy2.append(y2)
	cv.line(img1_2, (x1, y1), (x2, y2), (0, 255, 0), 2)

for a in dizix1:
	for b in dizix2:
		fark.append(abs(a-b))

for c in diziy1:
	for d in diziy2:
		fark2.append(abs(c-d))

for i in range(len(diziy1)):
		fark3.append(int((fark2[i] ** 2) + (fark[i] ** 2)) ** 0.5)
fark3.sort()
fark3.reverse()
fal2 = fark3[0]

dizix1.clear()
dizix2.clear()
diziy1.clear()
diziy2.clear()
fark.clear()
fark2.clear()
fark3.clear()

plt.imshow(img1_2)
plt.show()


#ÜÇÜNCÜ PARMAK İÇİN YAPILACAKLAR
img1_3 = cv.imread(iimg3)
gray_img1_3 = cv.cvtColor(img1_3, cv.COLOR_BGR2GRAY)
(thresh3, output3) = cv.threshold(gray_img1_5, 95, 255, cv.THRESH_BINARY)
output3 = cv.GaussianBlur(gray_img1_3, (5, 5), 3)
output3 = cv.Canny(output3, 0, 75)
plt.imshow(output3)
plt.show()

img1_3_height = img1_3.shape[0]
img1_3_width = img1_3.shape[1]
#resmin sağ tarafına maskelem işlemi yapar
contours5 = np.array([[0, 0], [0,img1_3_height], [(6*img1_3_width)/8, img1_3_height], [(6*img1_3_width)/8,0]])
mask5 = np.zeros_like(output3)
cv.fillPoly(mask5, np.array([contours5], dtype=np.int32), 255)
masked_img1_3 = cv.bitwise_and(output3, mask5)

#resmin sol tarafına maskeleme işlemi yapar
contours6 = np.array([[(2*img1_3_width)/8, 0], [(2*img1_3_width)/8,img1_3_height], [(img1_3_width), img1_3_height], [(img1_3_width),0]])
mask6 = np.zeros_like(masked_img1_3)
cv.fillPoly(mask6, np.array([contours6], dtype=np.int32), 255)
masked_img1_3_2 = cv.bitwise_and(masked_img1_3, mask6)

plt.imshow(masked_img1_3_2)
plt.show()
lines = cv.HoughLinesP(masked_img1_3_2, 5, np.pi / 280, 30)
for line in lines:
	x1, y1, x2, y2 = line[0]
	dizix1.append(x1)
	dizix2.append(x2)
	diziy1.append(y1)
	diziy2.append(y2)
	cv.line(img1_3, (x1, y1), (x2, y2), (0, 255, 0), 2)

for a in dizix1:
	for b in dizix2:
		fark.append(abs(a-b))

for c in diziy1:
	for d in diziy2:
		fark2.append(abs(c-d))

for i in range(len(diziy1)):
		fark3.append(int((fark2[i] ** 2) + (fark[i] ** 2)) ** 0.5)
fark3.sort()
fark3.reverse()
fal3 = fark3[0]

dizix1.clear()
dizix2.clear()
diziy1.clear()
diziy2.clear()
fark.clear()
fark2.clear()
fark3.clear()

plt.imshow(img1_3)
plt.show()


#DÖRDÜNCÜ PARMAK İÇİN YAPILACAKLAR
img1_4 = cv.imread(iimg4)
gray_img1_4 = cv.cvtColor(img1_4, cv.COLOR_BGR2GRAY)
(thresh4, output4) = cv.threshold(gray_img1_4, 95, 255, cv.THRESH_BINARY)
output4 = cv.GaussianBlur(gray_img1_4, (5, 5), 3)
output4 = cv.Canny(output4, 0, 75)
plt.imshow(output4)
plt.show()

img1_4_height = img1_4.shape[0]
img1_4_width = img1_4.shape[1]
#resmin sağ tarafına maskelem işlemi yapar
contours7 = np.array([[0, 0], [0,img1_4_height], [(6*img1_4_width)/8, img1_4_height], [(6*img1_4_width)/8,0]])
mask7 = np.zeros_like(output4)
cv.fillPoly(mask7, np.array([contours7], dtype=np.int32), 255)
masked_img1_4 = cv.bitwise_and(output4, mask7)

#resmin sol tarafına maskeleme işlemi yapar
contours8 = np.array([[(2*img1_4_width)/8, 0], [(2*img1_4_width)/8,img1_4_height], [(img1_4_width), img1_4_height], [(img1_4_width),0]])
mask8 = np.zeros_like(masked_img1_4)
cv.fillPoly(mask8, np.array([contours8], dtype=np.int32), 255)
masked_img1_4_2 = cv.bitwise_and(masked_img1_4, mask8)

plt.imshow(masked_img1_4_2)
plt.show()
lines = cv.HoughLinesP(masked_img1_4_2, 5, np.pi / 280, 30)
for line in lines:
	x1, y1, x2, y2 = line[0]
	dizix1.append(x1)
	dizix2.append(x2)
	diziy1.append(y1)
	diziy2.append(y2)
	cv.line(img1_4, (x1, y1), (x2, y2), (0, 255, 0), 2)

for a in dizix1:
	for b in dizix2:
		fark.append(abs(a-b))

for c in diziy1:
	for d in diziy2:
		fark2.append(abs(c-d))

for i in range(len(diziy1)):
		fark3.append(int((fark2[i] ** 2) + (fark[i] ** 2)) ** 0.5)
fark3.sort()
fark3.reverse()
fal4 = fark3[0]

dizix1.clear()
dizix2.clear()
diziy1.clear()
diziy2.clear()
fark.clear()
fark2.clear()
fark3.clear()

plt.imshow(img1_4)
plt.show()


#AVUÇİÇİ İÇİN YAPILACAKLAR
img1_5 = cv.imread(iimg_avucici)
gray_img1_5 = cv.cvtColor(img1_5, cv.COLOR_BGR2GRAY)
(thresh5, output5) = cv.threshold(gray_img1_5, 95, 255, cv.THRESH_BINARY)
output5 = cv.GaussianBlur(gray_img1_5, (5, 5), 3)
output5 = cv.Canny(output5, 0, 75)
plt.imshow(output5)
plt.show()

img1_5_height = img1_5.shape[0]
img1_5_width = img1_5.shape[1]
#resmin sağ tarafına maskelem işlemi yapar
contours9 = np.array([[0, 0], [0,img1_5_height], [(6*img1_5_width)/8, img1_5_height], [(6*img1_5_width)/8,0]])
mask9 = np.zeros_like(output5)
cv.fillPoly(mask9, np.array([contours9], dtype=np.int32), 255)
masked_img1_5 = cv.bitwise_and(output5, mask9)
lines = cv.HoughLinesP(masked_img1_5, 5, np.pi / 280, 30)
for line in lines:
	x1, y1, x2, y2 = line[0]
	dizix1.append(x1)
	dizix2.append(x2)
	diziy1.append(y1)
	diziy2.append(y2)
	cv.line(img1_5, (x1, y1), (x2, y2), (0, 255, 0), 2)

for a in dizix1:
	for b in dizix2:
		fark.append(abs(a-b))

for c in diziy1:
	for d in diziy2:
		fark2.append(abs(c-d))

for i in range(len(diziy1)):
		fark3.append(int((fark2[i] ** 2) + (fark[i] ** 2)) ** 0.5)
fark3.sort()
fark3.reverse()
fal5 = fark3[0]

dizix1.clear()
dizix2.clear()
diziy1.clear()
diziy2.clear()
fark.clear()
fark2.clear()
fark3.clear()

plt.imshow(img1_5)
plt.show()

if(fal1<fal3):
	print("Böyle insanlar genelde çekici, etkileyici, girişken ve konuşkan bir yapıya sahiptirler. Kararlı, cesaretli ve sorunlarla başa çıkma hususunda başka insanlara oranla daha iyidirler. İnsanlara karşı çok cana yakındırlar ve etraflarındakiler bu içtenliklerini hissedebilirler. Kişilikleri gereği mühendislik ve bilim insanı olmaya daha çok yatkındırlar. Aynı zamanda bulmaca çözme konusunda çok başarılıdırlar.")

if(fal1>fal3):
	print("İşaret parmağı, yüzük parmağından büyük insanlar genellikle kendilerine güvenen insanlardır. Arkadaş ortamlarında eğlenmeyi bilen ve gereksiz konular için zamanlarını boşa harcamaktan kaçınan bir yapıya sahipsiniz. Yeni bir iş girişimi konusunda ya da kişisel ilişkilerinizde, genellikle ilk adımı atmamayı tercih edersiniz. İncelikli düşünen bir yapıya sahip olup, pek çok konuda oldukça dikkatlisiniz.")

if(fal1==fal3):
	print("Eğer işaret ve yüzük parmağınız eşit ise; oldukça sakin, iyi huylu ve fikir ayrılıklarından hoşlanmayan bir yapıya sahipsiniz. Organize olma ve herkesle iyi anlaşma konusunda oldukça iyisiniz. Ailenize ve arkadaşlarınıza çok sadıksınız ve kendinizi onlara adarsınız. Kolay sinirlenen bir yapıya sahipsiniz. Küçük bir anlaşmazlık, büyük bir kavgaya dönüşebilir. Size karşı çıkılmasından daha çok sizin tarafınızda olunmasından hoşlanırsınız.")

if(fal2==fal5):
	print("Katı kuralları olan ve enerjik, bazen inatçısınız.Ayni zamanda pratik ve sorumlu, bazen maddiyatçı,Yaratıcı, anlayışlı ve sempatik, Karamsar, duygusal ve çekingen olabilirsiniz.Ayni zamanda İçe kapanık , İşleri sessizce ve öngörülü bir şekilde yapıyorsunuz , maddi varlık konusunda rahatsınız.")

if(fal2>fal5):
	print("Sosyal, konuşkan ve esprili veya Sığ, kinci ve soğuk olabilirsiniz.Zihinsel ve manevi açıdan rahatsınız .İşleri farklı ve radikal yollardan yapıyorsunuz")

if(fal2<fal5):
	print("Doğal, hevesli ve iyimsersiniz.Bazen egoist, fevri ve duygusuz olabiliyorsunuz. Dışa dönüksünüz. İşleri cesurca ve düşünmeden yapan bir kişiliğe sahipsiniz.")

if(fal4>fal3*1.5):
	print("Utangaç bir yapıya sahipsiniz. Sosyalleşme konusunda   bir takım sıkıntılar yaşıyorsunuz.  Fakat bu sizin soğukluğunuzdan değil,  aslında insanlarla iletişim kurmak istiyorsunuz fakat utangaç yapınız buna izin vermiyor.")

if(fal4<fal3*1.5):
	print("Çok konuşkan bir insansınız.  Her ortamda göze çarpan biri olmayı başarıyorsunuz.  Odak noktası olmayı seviyorsunuz. Etrafiniza neşe saçıyorsunuz.")

if(fal4==fal3*1.5):
	print("Bu kişilerin, kendilerine özgü bir havaları vardır. Onlar genelde farklı ve yaratıcı olurlar. Orijinal fikirlere sahiptirler.")

if(fal1>fal2):
	print(" iyi huylu, iyi görünümlü ve narin olmanızin yanı sıra endişe göstergesi de olabilir. ")

if(fal1<fal2):
	print("Sabırsız  ve yaratıcı kişilerde bulunur. Oldukça yaratıcı bir kişiliğe sahipsiniz. Durum kurtarma konusunda oldukça ustasınız.")

if(fal1==fal2):
	print(" Oyunculuk kabiliyetiniz oldukca yüksek. Aynı zamanda güzel yalan söyleme beceriniz de aynı oranda yüksek.  Etrafınızdaki insanları kolaylıkla kandirabilen, ikna etme özelliği oldukça yüksek bir insansınız.")


