import random


def hypotenuseMeter(x, y):
    # noktalar arası uzaklığı ölçer
    X_axis = x[0] - y[0]
    Y_axis = x[1] - y[1]
    return (X_axis ** 2 + Y_axis ** 2) ** 0.5


def pointMaker(width, height, n):
    # verilen boyut sınırları içinde n tane nokta üretir.
    nx2 = list()
    for _ in range(n):
        nx2.append([width * random.random(), height * random.random()])
    return nx2


def distanceMatrix(nx2):
    # noktalar listesindeki tüm noktaların birbirine olan uzaklığını ölçer ve döndürür.
    nxn = list()
    for i in nx2:
        row = list()
        for j in nx2:
            # tüm noktaları döngüye sokar.
            row.append(hypotenuseMeter(i, j))
        nxn.append(row)
    return nxn


def writeThePoints(nx2):
    # noktaları tablolaştırır.
    print("-" * 37)
    print("|  Nokta  |  X Ekseni  |  Y Ekseni  |")
    print("-" * 37)
    counter = 1
    for i in nx2:
        # noktaları döngüye sokar.
        print("|{:^9}|{:^12.1f}|{:^12.1f}|".format(counter, i[0], i[1]))
        print("-" * 37)
        counter += 1


def writeTheDM(nxn):
    # noktaların birbirine uzaklığını tablolaştırır.
    length = len(nxn)
    print("-" * ((length + 1) * 7 + 1))
    string1 = "|{:^" + str((length + 1) * 7) + "}|"
    # döngünün boyutuna uygun gerekli string üretilir.
    print(string1.format("Distance Matrix"))
    print("-" * ((length + 1) * 7 + 1))
    string2, string3 = "|", "|      |"
    # döngünün boyutuna uygun gerekli string üretilir.
    for _ in nxn:
        string2 += "{:^6.1f}|"
        # döngünün boyutuna uygun gerekli string üretilir.
        string3 += "{:^6}|"
        # döngünün boyutuna uygun gerekli string üretilir.
    print(string3.format(*range(length)))
    print("-" * ((length + 1) * 7 + 1))
    counter = 0
    for i in nxn:
        # matrixi döngüye sokar.
        print("|{:^6}".format(counter), end="")
        print(string2.format(*i))
        print("-" * ((length + 1) * 7 + 1))
        counter += 1


if __name__ == "__main__":
    # modülün başlangıç yeri belirtilir.
    points1 = pointMaker(100, 100, 10)
    # 10 adet nokta oluşturulur.
    writeThePoints(points1)
    # oluşturulan noktalar yazdırılır.
    points2 = pointMaker(100, 100, 100)
    # 100 adet noktalar oluşturulur.
    writeThePoints(points2)
    # oluşturulan nokta yazdırılır.
    points3 = pointMaker(100, 100, 10)
    # 100 adet nokta oluşturulur.
    DM = distanceMatrix(points3)
    # oluşturulan noktalar arası uzaklık ölçülür.
    writeTheDM(DM)
    # sonuç tablolaştırılmak için writeTheDM fonk.'una parametre olarak gönderilir.
