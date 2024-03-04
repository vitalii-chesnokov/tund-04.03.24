from module import*


kasutajanimed=[]
while True:
    print("1-registeerimine\n2-autoriseerimine?n3-nime või parooli muutmine?n4-unustanud parooli taastamine?n5-lõpetamine")
    vastus=input("Sisestage arv")
    if vastus == 1:
        print("Registeerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus == 2:
        print("Autoriseerimine")
        autoriseerimine(kasutajad,salasõna)
    elif vastus == 3 :
        print("Nimi  või parooli muutmine")
    elif vastus == 4:
        print("Unustanud porooli taastamine")
    elif vastus == 5:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")

