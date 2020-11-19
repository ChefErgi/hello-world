# 1. Bilgisayyar 1 - 100 arasında bir sayı tutar
# 2. Kullanıcı bu sayıyı tahmin eder
# 3. Eğer girilen sayı tutulan sayıdan BÜYÜKSE ekrana Aşağı yazar
# 4. Eğer girilen sayı tutulan sayıdan  KÜÇÜKSE ekrana YUKARI yazar
# 5. Eğer girilen sayı tutulan sayıya eşit ise ekrana BİLDİN yazar
import random

try:
    rasgtele_sayi = random.randint(1, 100)
    count = 0
    sayı_bilindi_mi = False
    while sayı_bilindi_mi == False:
        tahmin = int( input("1-100 arasındai sayıyı tahmin ediniz: "))
        count += 1
        if tahmin < rasgtele_sayi:
            print("Yukarı, tekrar deneyiniz.")
        elif tahmin > rasgtele_sayi:
            print("Aşağı, tekrar deneyiniz.")
        else:
            print("Vallahi doğru bildiniz.")
            print("Sayıyı {} denemede bildiniz".format(count))
            sayı_bilindi_mi = True

except ValueError:
    print("Lütfen tamsayı yazınız.")

#döngü: belirli bir koşul gerçekleşinceye dek tekrar işlem
