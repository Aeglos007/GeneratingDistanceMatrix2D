from functools import reduce


class Money:
    # input edilen bilgilere sahip obje oluşturur.
    def __init__(self, variance, distortion, flatness, entropy, realType=int(), estimatedType=int()):  # Constructor.
        self.variance = variance
        # varyans değeri
        self.distortion = distortion
        # çarpıklık değeri
        self.flatness = flatness
        # basıklık değeri
        self.entropy = entropy
        # entropi değeri
        self.realType = int(realType)
        # gerçek tür
        self.estimatedType = int(estimatedType)
        # tahmini tür

    def nearness(self, money):
        # Paraların öklid algoritmasına göre yakınlığı ölçülür.
        firstComperation = (self.variance - money.variance) ** 2
        secondComperation = (self.distortion - money.distortion) ** 2
        thirdComperation = (self.flatness - money.flatness) ** 2
        lastComperation = (self.entropy - money.entropy) ** 2
        return (firstComperation + secondComperation + thirdComperation + lastComperation) ** 0.5


def kNN(theMoneyOfKNN, allMoneysOfKNN, kOfKNN):
    # fonksiyon, nearness metodu yardımıyla söz konusu paranın türünü tahmin eder
    ResultsOfKNN = map(lambda i: [theMoneyOfKNN.nearness(i), i], allMoneysOfKNN)
    # bellekteki tüm paraların söz konusu parayla yakınlığı kendisiyle beraber listelenir.
    theResult = sorted(ResultsOfKNN, key=lambda x: x[0])[:kOfKNN]
    # liste 0. sütuna göre sıralanır ve ilk kOfKNN kadarı saklanır.
    elimination = reduce(lambda x, y: x - y if y == 0 else x + y, map(lambda x: x[1].realType, theResult))
    # listenin 1. sütunu alınır, oluşan listedeki objelerin tür değerlerinin çoğunluğu  ölçülür.
    if elimination > 0:
        theMoneyOfKNN.estimatedType = 1
    # değişkenin 0'dan büyük olması "1" türünün çoğunlukta olduğunu gösterir.
    elif elimination == 0:
        theMoneyOfKNN.estimatedType = theResult[0][1].realType
    # farklı türe ait paraların eşit olduğu koşuldur. en yakın komşunun türü hesaba katılır.
    elif elimination < 0:
        theMoneyOfKNN.estimatedType = 0
    # değişkenin 0'dan küçük olması "0" türünün çoğunlukta olduğunu gösterir.
    return theResult  # en yakın k komşu yakınlık ölçüleriyle braber döndürülür.


def readTheFile():
    # veriSeti.txt dosyası üzerinde işlemler yapar.
    allMoneysOfReadTheFile = list()
    with open("VeriSeti.txt", "r", encoding="utf-8") as file:
        # veriSeti.txt dosyasını açar ve tüm satırları file değişkenine listeler.
        for i in file:
            # listeyi döngüye sokar.
            liste = Money(*map(float, i.split(",")))
            # her satır para objesine dönüştürülür
            allMoneysOfReadTheFile.append(liste)
    return allMoneysOfReadTheFile  # tüm veri para objesi halinde döndürülür.


def successTesting(allMoneysOfSuccessTesting, kOfSuccessTesting):
    # kNN algoritmasının başarı oranını ölçer.
    fakes, originals = [x for x in allMoneysOfSuccessTesting if x.realType == 0], [y for y in allMoneysOfSuccessTesting
                                                                                   if y.realType == 1]
    # tüm paralar "list comprehension" yardımıyla gerçek ve sahte olanlar olarak ikiye ayrılır.
    testMoneys, restOfAll = fakes[-1:-101:-1] + originals[-1:-101:-1], fakes[:len(fakes) - 99:] + originals[
                                                                                                  :len(fakes) - 99:]
    # gerçek ve sahte paraların son yüz elemanı test edilmek için ayrılır, kalanlar bir değişkene atanır.
    verified = 0
    # gerçek ve tahmini türü uyuşan paralar sayar.
    for j in testMoneys:
        # test paralarını döngüye sokar.
        theResult = kNN(j, restOfAll, kOfSuccessTesting)
        # her değeri kNN fonk.'una gönderir, return verisini saklar.
        writeTheMoneys(j, theResult)
        # saklanan return verisini tablolamak için writeTheMoneys fonk.'una gönderir.
        print("Söz konusu banknotun gerçek türü: ", j.realType)
        # değerin gerçek değerini yazdırır.
        if j.realType == j.estimatedType: verified += 1
        # gerçek ve tahmini türü uyuşan paraları bulur.
    print("Başarı oranı: %{:.2f}".format(verified / len(testMoneys) * 100))
    # verified sayesinde başarı yüzdesi ölçülür ve yazdırılır.


def writeTheMoneys(testedMoney, neigborsList):
    # test edilmiş her paranın daha önce belirlenen en yakın komşuları tablolaştırılır.
    print("-" * 111)
    print(
        "| Örnek No | Varyans Değeri | Çarpıklık Değeri | Basıklık Değeri | Entropi Değeri | Tür |       uzaklık       |")
    print("-" * 111)
    for counter, i in enumerate(neigborsList):
        # komşular index değerleriyle ikili listeler oluşturur.hepsi bir liste içinde döngüye girer
        print("|{:^10}|{:^16}|{:^18}|{:^17}|{:^16}|{:^5}|{:^21}|".format(counter, i[1].variance, i[1].distortion,
                                                                         i[1].flatness, i[1].entropy, i[1].realType,
                                                                         i[0]))
        print("-" * 111)
    print("Söz konusu banknotun tahmini türü: ", testedMoney.estimatedType)


def writeTheDataBase(wholeMoneys):
    # veriSetinden alınmış tüm paralar tablolaştırılır.
    print("-" * 89)
    print("| Örnek No | Varyans Değeri | Çarpıklık Değeri | Basıklık Değeri | Entropi Değeri | Tür |")
    print("-" * 89)
    for counter, i in enumerate(wholeMoneys):
        # paralar index değerleriyle ikili listeler oluşturur.hepsi bir liste içinde döngüye girer
        print("|{:^10}|{:^16}|{:^18}|{:^17}|{:^16}|{:^5}|".format(counter, i.variance, i.distortion, i.flatness,
                                                                  i.entropy, i.realType))
        print("-" * 89)


if __name__ == "__main__":
    # modülümüzün başlangıç yeri belirtilir.
    allMoneys = readTheFile()  # veriSetindeki tüm paralar saklanır.
    while True:
        Variance = float(input("Varyans: "))  # varyans değerini alır ve saklar.
        Distortion = float(input("Çarpıklık: "))  # çarpıklık değerini alır ve saklar.
        Flatness = float(input("Basıklık: "))  # basıklık değerini alır ve saklar.
        Entropy = float(input("Entropi: "))  # entropi değerini alır ve saklar.
        K = int(input("K: "))  # k değerini alır ve saklar.
        theMoney = Money(Variance, Distortion, Flatness,
                         Entropy)  # input edilen verileri para objesine dönüştürür ve saklar.
        result = kNN(theMoney, allMoneys, K)
        # para objesi, bellekteki tüm para ve k değişkeni parametre olarak kNN fonk.'una gönderilir. return verisi saklanır.
        writeTheMoneys(theMoney, result)
        # return verisi tablolaştırılmak için writeTheMoneys fonk.'una parametre olarak gönderilir.
        theQuestion = input("tekrar input girişi yapmak ister misiniz?(e/h)")
        if theQuestion == "h": break
    k = int(input("K(test için): "))
    # tes için k değeri istenir ve saklanır.
    successTesting(allMoneys, k)
    # bellekteki tüm para, k değeri ile beraber parametre olarak succesTesting fonk.'una gönderilir.
    writeTheDataBase(allMoneys)
    # bellekteki tüm para tablolaştırılmak için writeTheDataBase fonk.'una parametre olarak gönderilir.
