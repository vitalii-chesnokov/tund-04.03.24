from string import*

def autoriseerimine(kasutajad:list, paroolid:list):
    """Funktsioon kuva ekraanile "Tere tulemast kui kasutaja on olemas nimekirajs 
    Nimi on järjendis kasutajad
    Salasõna on paroolide järjendis
    Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad:...
    :param list paroolid:...
    """
p=0
while True:
    nimi=input("Sisesta kasutajanimi: ")
    parool=input("Sisesta salasõna: ")
    p+=1
    if nimi in kasutajad and parool i paroolid:
        if kasutajad.index(nimi)==paroolid.index(parool):
            print(f"Tere tulemast! {nimi} ")
            break
        else:
            print("Vale nimi või salasõna!")
            if p==5:
                print("Proovi uuesti 10 sek pärast")
                for i in range(10):
                    sleep(1)
                    print(f"On jäänud {10-i} sek ")
     else:
         print("Kasutajad pole")
    


def registeerimine(kasutajad:list, paroolid:list)->any:
    """kikjeldus
    :param list kasutajad: Kirjeldus
    :param list paroolid: Kirjeldus
    :rtype: list,list

    """
    while True:
        nimi=input("Mis on sinu nimi? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool?  ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                             flag_p=True
                        elif p in ascii_lowercase:
                            flag_l=True
                        elif p in ascii_lowercase:
                             flag_u=True
                        elif p in ascii_lowercase:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.uppend(nimi)
                        paroolid.uppend(parool)
                    break
                else:
                  print("Nõrk salasõna!")
            else:
                print("Selline kasutaja on juba olemas!")


    return kasutajad, paroolid
 