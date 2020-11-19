#sokağa çıkabileceğimi ya da çıkamayacaımı söyleyen bir kod

try:

    yaş = int(input("Merhabalar, lütfen yaşınızı giriniz: "))
    haftasonu = input("Bugün haftasonu mu ?(E/H) :").upper()
    saat = float(input("Lütfen saati giriniz: "))
    çalışan = input("Çalışıyor musunuz ?(E/H) :").upper()

    while haftasonu == "E":
        if 10 < saat < 20:
            print("Dışarı çıkabilirsiniz efendim. Corona'ya dikkat edelim :)")
        else:
            print("Üzgünüm, evde kalmanız herkes için en iyisi olacak :(")
        break

    while haftasonu == "H" and 20 < yaş < 65:
        print("Dışarı çıkabilirsiniz efendim. Corona'ya dikkat edelim :)")
        break

    while haftasonu == "H" and yaş < 20:
        if çalışan == "E":
            print("Dışarı çıkabilirsiniz efendim. İyi çalışmalar :)")
        elif çalışan == "H" and 13 < saat < 16:
            print("Dışarı çıkabilirsiniz efendim. Çok cozutma kardeş :)")
        else:
            print("Maalesef kardeşim, dışarı çıkamazsın şu an :(")
        break

    while haftasonu == "H" and 65 < yaş:
        if çalışan == "E":
            print("Dışarı çıkabilirsiniz efendim. İyi çalışmalar :)")
        elif çalışan == "H" and 10 < saat < 13:
            print("Dışarı çıkabilirsiniz efendim. Corona'ya dikkat ediniz lütfen :)")
        else:
            print("Maalesef efendim, şu an dışarı çıkamazsın :(")
        break

except ValueError:
    print("Lütfen tamsayı yazınız!")



