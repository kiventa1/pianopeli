
import random

# koskettimet
def koskettimet():
    print("_________________________________________________________")
    print("|  |X| |X|  |  |X| |X| |X|  |  |X| |X|  |  |X| |X| |X|  |")
    print("|  |X| |X|  |  |X| |X| |X|  |  |X| |X|  |  |X| |X| |X|  |")
    print("|  |X| |X|  |  |X| |X| |X|  |  |X| |X|  |  |X| |X| |X|  |")
    print("|  |X| |X|  |  |X| |X| |X|  |  |X| |X|  |  |X| |X| |X|  |")
    print("|   |   |   |   |   |   |   |   |   |   |   |   |   |   |")
    print("|   |   |   |   |   |   |   |   |   |   |   |   |   |   |")    
    print("|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("")
    print("")
    print("")

# pelin sävelikkö
kaikki_sävelet = ["C", "D", "E", "F", "G", "A", "H", "C1", "D1", "E1", "F1", "G1", "A1", "H1"]

# pelin sävelikkö f avain
kaikki_sävelet_f = ["E", "F", "G", "A", "H", "C1", "D1", "E1", "F1", "G1", "A1", "H1", "C2", "D2"]

# pelin asetukset
pisteet = 0
oikeatvastaukset = 0
vaaditut_oikeat = 2  # Peräkkäiset oikeat vastaukset, jotta pelaaja saa pisteen.

# Funktio, joka soittaa fanfaarin (tulostaa fanfaarin)
def soita_fanfaari():
    print("\n🎉🎶 FANFAARI! 🎶🎉")
    print("")
    print(f"Hienoa, sait yhteensä {vaaditut_oikeat} oikein.")
    print("")

def tulosta_piano(savel):

    s = []
    i = 0

    # Kootaan lista, joka tulostetaan pianon koskettimille
    # Asetetaan listaan vain annettu sävel ja muut alkiot jätetään tyhjäksi
    # Asetetaan annetun sävelen kummallekin puolelle kysymysmerkki
    for item in kaikki_sävelet:
        if item == savel:
            s[i-1] = "?" # tulostetaan edelliseen koskettimeen ?
            s.append(item.rstrip("1234567890")) # poistetaan sävelnumerot tulostettavasta listasta
            s.append("?") # tulostetaan seuraavaan koskettimeen ?
        else: 
            s.append(" ") # tulostetaan tyhjä kaikkiin muihin koskettimiin

        i += 1

    print("_________________________________________________________")
    print("|  |X| |X|  |  |X| |X| |X|  |  |X| |X|  |  |X| |X| |X|  |")
    print("|  |X| |X|  |  |X| |X| |X|  |  |X| |X|  |  |X| |X| |X|  |")
    print("|  |X| |X|  |  |X| |X| |X|  |  |X| |X|  |  |X| |X| |X|  |")
    print("|  |X| |X|  |  |X| |X| |X|  |  |X| |X|  |  |X| |X| |X|  |")
    print("|   |   |   |   |   |   |   |   |   |   |   |   |   |   |")
    print(f"| {s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]} | {s[5]} | {s[6]} | {s[7]} | {s[8]} | {s[9]} | {s[10]} | {s[11]} | {s[12]} | {s[13]} |")
    print("|___|___|___|___|___|___|___|___|___|___|___|___|___|___|")
    print("")


def tulosta_gavain(savel):  #g-avaimella sävelet

    s2 = [] #lista sävelistä
    i = 0 #sävelpaikka

    for item in kaikki_sävelet:
        if item == savel:
            s2[i-1] = "?" # tulostetaan edelliseen koskettimeen ?
            s2.append(item.rstrip("1234567890")) # poistetaan sävelnumerot tulostettavasta listasta
            s2.append("?") # tulostetaan seuraavaan koskettimeen ?
        else: 
            s2.append("") # tulostetaan tyhjä kaikkiin muihin koskettimiin

        i += 1

   #G-AVAIN
    print("")
    print(f"                        {s2[13]} ")
    print(f"                     {s2[12]} ")
    print(f"                  {s2[11]} ")
    print(f"–––––––––––––––{s2[10]}–––––––––––––––––––––––––––––––––––––––")
    print(f"                  {s2[9]}                                    ")
    print(f"–––––––––––––––––––––{s2[8]}–––––––––––––––––––––––––––––––––")
    print(f"                       {s2[7]}                               ")
    print(f"––––––––––––––––––––––––––{s2[6]}––––––––––––––––––––––––––––")
    print(f"                       {s2[5]}                               ")
    print(f"–––––––––––––––––––––{s2[4]}–––––––––––––––––––––––––––––––––")
    print(f"                  {s2[3]}                                    ")
    print(f"––––––––––––––––{s2[2]}––––––––––––––––––––––––––––––––––––––")                                                                                            
    print(f"             {s2[1]}                                         ")
    print(f"          {s2[0]} ")
    print("")
    print("")
     

def tulosta_favain(savel): #f-avaimella sävelet
    s2 = [] #sävellista
    i = 0 #sävelpaikka

    for item in kaikki_sävelet_f:
        if item == savel:
            s2[i-1] = "?" # tulostetaan edelliseen koskettimeen ?
            s2.append(item.rstrip("1234567890")) # poistetaan sävelnumerot tulostettavasta listasta
            s2.append("?") # tulostetaan seuraavaan koskettimeen ?
        else: 
            s2.append("") # tulostetaan tyhjä kaikkiin muihin koskettimiin

        i += 1

    #F-AVAIN
    print("")
    print(f"")                                                                                 
    print(f"                              {s2[13]}")
    print(f"                           {s2[12]} ")
    print(f"                       {s2[11]} ")
    print(f"––––––––––––––––––––{s2[10]}––––––––––––––––––––––––––––––––––")   
    print(f"                  {s2[9]} ")
    print(f"–––––––––––––––{s2[8]}–––––––––––––––––––––––––––––––––––––––")
    print(f"                  {s2[7]}                                     ")
    print(f"–––––––––––––––––––––{s2[6]}–––––––––––––––––––––––––––––––––")
    print(f"                       {s2[5]}                               ")
    print(f"––––––––––––––––––––––––––{s2[4]}––––––––––––––––––––––––––––")
    print(f"                       {s2[3]}                               ")
    print(f"––––––––––––––––––––{s2[2]}––––––––––––––––––––––––––––––––––")
    print(f"                {s2[1]}                                      ")  
    print(f"             {s2[0]}                                         ")  
    print("")

# HAE_PISTEET        
def hae_pisteet():
    return 5

# ALOITUSTEKSTI
pelaaja = ""
def tulosta_aloitus():
    print("")
    print("")
    print("")
    koskettimet()
    print("")
    print("Tervetuloa Koskettimien taikaa -seikkailuun!") 
    print("")
    print("Tätä peliä pelaamalla opit musiikin aakkoset. \nOpit sävelten järjestyksen koskettimilla ja viivastolla, mikä nopeuttaa nuotinluvun oppimista.")
    print("")
    print(f"Pelissä keräät pisteitä ja saatuasi riittävästi pisteitä pääset seuraavalle tasolle. Sinun tulee saada oikeita vastauksia {vaaditut_oikeat}.\nTehtäväsi on selvittää tiesi neljän tason kautta pelin loppuun. Aivan lopuksi saat ratkaistavan arvoituksen.")
    print("")
    print("")
    print("Oletko valmis seikkailuun ja selvittämään koskettimien salaisuudet?")
    print("")
    pelaaja = input("Anna nimesi: ")
    print(f"Hei {pelaaja}!")

# NAAPURIT - KOSKETINSUUNTA
def hae_naapurit(sävel, sävel_list):
    index = sävel_list.index(sävel)
    naapurit = []

    # VARMISTETAAN, ETTEI YLITETÄ LISTAA
    naapurit.append(sävel_list[index - 1])  # ALIN
    naapurit.append(sävel_list[index + 1])  # YLIN
    return naapurit

# NAAPURIKYSYMYS
def kysy_kysymys(taso: int):
    #Kysyy satunnaisen sävelen ja sen naapurit.
    global oikeatvastaukset

    sävel_list = kaikki_sävelet

    if taso == 3:
        sävel_list = kaikki_sävelet_f

    #g-avaimen sävelten lista 
    kysyttävät_sävelet = sävel_list.copy()
    kysyttävät_sävelet.pop(0) # poistetaan ensimmäinen
    kysyttävät_sävelet.pop() # poistetaan viimeinen

    if taso == 1:
        #ARVOTAAN KYSYMYS
        arvottu_sävel = random.choice(kysyttävät_sävelet)  #arvotaan sävel, jota kysytään
        naapurit = hae_naapurit(arvottu_sävel, sävel_list)  #etsi naapurit

        tulosta_piano(arvottu_sävel) # kutsutaan tulosta_piano-funktiota

    if taso == 2:
        #ARVOTAAN KYSYMYS
        arvottu_sävel = random.choice(kysyttävät_sävelet)  #arvotaan sävel, jota kysytään
        naapurit = hae_naapurit(arvottu_sävel, sävel_list)  #etsi naapurit

        tulosta_gavain(arvottu_sävel) #kutsutaan tulosta_gavain-funktiota

    if taso == 3:
        #ARVOTAAN KYSYMYS
        arvottu_sävel = random.choice(kysyttävät_sävelet)  #arvotaan sävel, jota kysytään
        naapurit = hae_naapurit(arvottu_sävel, sävel_list)  #etsi naapurit

        tulosta_favain(arvottu_sävel) #kutsutaan tulosta_favain-funktiota

    # POISTETAAN SÄVELLISTAN NUMEROINNIT: ei haluta oktaavialoja, ei olennaista sävelten järjestysten oppimisen kannalta
    kysymys_sävel = arvottu_sävel.rstrip("1234567890")

    print(f"(Pisteesi: {oikeatvastaukset} / {vaaditut_oikeat}) \nMitkä ovat sävelen {kysymys_sävel.upper()} naapurit? Anna alempi ensin.") #kysymys

    # PELAAJAN VASTAUS
    pelaajan_vastaus = input(f"Naapurit: ").strip()

    # HUOMIOIDAAN ERILAISET VASTAUKSET; poistetaan kaikki ylimääräiset välilyönnit ja muutetaan kaikki isoiksi kirjaimiksi
    pelaajan_vastaus = pelaajan_vastaus.upper().replace(" ", "").replace("JA", "").replace(",", "")

#VASTAUKSEN TARKASTUS
    # Muutetaan oikea vastaus listasta merkkijonoksi, verrataan sitä pelaajan antamaan vastaukseen
    oikea_vastaus = ""
    for i in naapurit:
        item = i.rstrip("1234567890")
        oikea_vastaus += item
    
    # Onko vastaus oikein
    if pelaajan_vastaus == oikea_vastaus:
        oikeatvastaukset += 1
        print("")
        print("Oikein! Hienosti osattu.")
        print("")
    else:
        oikeatvastaukset -= 1  # Väärä vastaus vähentää yhden pisteen
        print("")
        print(f"Oi voi, nyt ei mennyt aivan oikein; sinulta vähennetään yksi piste. \nOikea vastaus on: {oikea_vastaus[0]} ja {oikea_vastaus[1]}.")
        print("")

    if oikeatvastaukset == vaaditut_oikeat:
        return True
    return False




# ------------------------------PÄÄOHJELMA--------------------------------------
# GLOBAALIT PARAMETRIT, ALOITUS
def pelaa_peli():
    global pisteet, oikeatvastaukset
    tulosta_aloitus()

    print("\nAloitetaan!\n")
    print("")
    
    # Taso 1
    print("Olet tasolla 1.")
    print("")
    
    while True:
        if kysy_kysymys(1):
            pisteet += 1
            if oikeatvastaukset == vaaditut_oikeat:
                soita_fanfaari()
                print("Pääset seuraavalle tasolle!")
                oikeatvastaukset = 0  #nollataan pisteet seuraavaa tasoa varten
                print("")
                break  # Siirrytään seuraavalle tasolle

    # Taso 2
    print("")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("")
    print("Olet tasolla 2. Harjoitellaan nyt säveliä viivastolla G-avaimen sävelpaikoilla.")
    
    while True:
        if kysy_kysymys(2):
            pisteet += 1
            if oikeatvastaukset == vaaditut_oikeat:
                soita_fanfaari()
                print("Pääset seuraavalle tasolle 3!")
                oikeatvastaukset = 0 #nollataan pisteet seuraavaa tasoa varten
                print("")
                break  # Siirrytään tasolle 3

    # Taso 3
    print("")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("")
    print("Olet tasolla 3. Harjoitellaan nyt säveliä viivastolla F-avaimen sävelpaikoilla!")
    while True:
        if kysy_kysymys(3):
            pisteet += 1
            print("")
            if oikeatvastaukset == vaaditut_oikeat:
                soita_fanfaari()
                print("Pääset seuraavalle tasolle 4!")
                oikeatvastaukset = 0 #nollataan pisteet seuraavaa tasoa varten
                print("")
                break 

    # Taso 4
    print("")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("")
    print("Olet tasolla 4. Loppukiri - nyt saat erilaisia tehtäviä peräkkäin!")
    while True:
        if kysy_kysymys(random.choice([1,2,3])):
            pisteet += 1
            print("")
            if oikeatvastaukset == vaaditut_oikeat:
                soita_fanfaari()
                print("Mahtavaa! Olet läpäissyt kaikki tasot. Nyt saat arvoituksen.")
                break  # Pelin loppu

    # Arvoitus
    print("")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("")
    print("SANA-ARVOITUS - KIRJAIMET SEKAISIN")
    print("Olet jo melkein selvittänyt Koskettimien taikaa -pelin. Nyt sinun pitää ratkaista vielä sana-arvoitus!")
    print("")
    
    arvoitus = ["Flyygeli", "Pianonsoitto", "Koskettimet", "Sorminumerot", "Nuottiviivasto", "Ylöspäin", "Joulupukki", "Soittotunti"]
    vastaus = random.choice(arvoitus)
    kirjaimet_sekoitettu = ''.join(random.sample(vastaus, len(vastaus))) # Muutetaan sana listaksi kirjaimista ja sekoitetaan ne
    print(f"Tässä on sana-arvoitus, jossa on kirjaimet sekaisin. \nMikä sana näistä muodostuu? {kirjaimet_sekoitettu}")
    print("")

    while True:
        arvaus = input(f"Vastaus: ")
        if arvaus.lower() == vastaus.lower():
            print("")
            soita_fanfaari()
            print(f"Onneksi olkoon, {arvaus} on oikein. Olet ratkaissut arvoituksen ja selvittänyt kaikki pelin tasot.")
            print("")
            print("Koskettimien taikaa -peli on päättynyt. Voit aloittaa uudelleen pelin.")
            print("")
            koskettimet()
            print("")
            break
        else: 
            print("")
            print("Yritä arvata uudelleen! \nVihje: Sana alkaa kirjaimella, joka on iso kirjain. \nVoit myös kokeilla kirjoittaa kirjaimia eri järjestykseen paperille.")
            print("")

# Käynnistä peli
if __name__ == "__main__":
    pelaa_peli()

