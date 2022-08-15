import csv
import gspread
import time


def gettingData(file, transactions):
    with open(file, mode='r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)  # skip header
        for row in csv_reader:
            date = row[0]
            name = row[2]
            sender = row[3]
            title = row[6]
            amount = float(row[7].replace(",", "."))
            method = row[10]

            sites = ["ECARD S.A.", "PAYU", "PAYPRO S.A.", "BLUE MEDIA S.A.", "DOTPAY S.A.", "PWPW 4"]
            for site in sites:
                if site in name:
                    name = sender
            if name == "J. PILSUDSKIEGO 9      MALBORK":
                name = method

            category = checkCategory(name)
            transaction = (date, name, amount, category, method)
            print(transaction)
            transactions.append(transaction)
        return transactions


def checkCategory(name):
    categories = {
        "EATING OUT": ["MCDONALDS", "KFC", "PIZZAHUTDOSTAWA", "PYSZNE", "ALFA", "AUTOMATY", "KAWIARNIA",
                       "WWW.ADYEN.COM", "FRIDAY", "SHELL", "YGREK", "METROPOLIA", "BERLIN DONER KEBAP", "DELIKATESY"],
        "SHOPPING": ["BIEDRONKA", "LEROY", "LIDL", "CARREFOUR", "ZABKA", "EUROSPAR", "SIN-SAY", "KIK", "TEDI", "AUCHAN",
                     "DEALZ", "PIOTR I PAWEL ", "WWW.MEDIAMARKT.", "ELECLERC",
                     "TIGER", "ME M06 03              GDANSK", "FORUM", "KAUFLAND", "MEDIAMARKT", "TESCO", "OPEN ER",
                     "OLX", "HM                     GDANSK"],
        "ONLINE SHOPPING": ["ALLEGRO", "AMAZON", "WWW.OLX.PL", "GESSLERMAGDA", "WWW.VIDEOPORADY", "HTTPS://WWW.VIN",
                            "PIXEL-SHOP", "GARETH DAVID STUD", "EPLAKATY.PL", "MI-HOME", "CRAZYSHOP.PL",
                            "FURGONETKA.PL", "BEWOOD.PL", "MOTOS.PL", "FUNNYCASE", "ADYEN N.V.", "BANK POCZTOWY"],
        "CLOTHES": ["H&M", "WWW.SINSAY.COM", "WEARMEDICINE.CO", "CROPP", "HOUSE", "RESERVED", "WWW.HM.COM", "LPP",
                    "ENVOYSERVIC", "VINTED"],
        "BEAUTY": ["ZIAJA.COM", "FRYZJERSKIE", "ROSSMANN", "TRINY.PL"],
        "TRANSPORT": ["JAKDOJADE", "KOLEO.PL ul. Kanclerska 15,Poznan", "KOLEO.PL", "MPSA",
                      "WOJEWÓDZKI OŚRODEK RUCHU DROGOWEGO", "INFO-CAR.PL", "STAROSTWO"],
        "CINEMA": ["WWW.HELIOS.PL Grunwaldzka 186,Poznan", "HELIOS"],
        "FUNDRAISERS": ["SIEPOMAGA", "RATUJEMYZW", "REDCROSS", "ZRZUTKA.PL"],
        "SUBSCRIPTIONS": ["SPOTIFY", "MICROSOFT", "DISNEY", "TVN", "NETFLIX", "HBO", "ODRABIAMY.PL", "GOOGLE PAYMENT",
                          "MOVIESTARPLANET.PL", "CANAL"],
        "VIDEO GAMES": ["STEAMGAMES", "KONSOLEIGRY", "ULTIMA", "FANATICAL", "KINGUIN", "INSTANT GAMING", "PLAYSTATION",
                        "HIPAY.COM", "WWW.SMART2PAY.C", "WWW.ENEBA.COM", "G2A", "INDIEGOGO*", "ORIGIN", "UBISOFT",
                        "GAMIVO", "HUMBLEBUNDLE", "GOG", "ROCKSTAR", "ENEBA"],
        "CULTURE": ["WWW.KUPBILECIK", "UNIWERSYTET", "EVENTIM", "BIBLIOTECZKA", "SWIATKSIAZK", "CASHBILL",
                    "KULTURALNYSKLEP", "DUA LIPA", "EMPIK", "EBILET", "WWW.EBILET.Pl", "ALTENBERG", "ALTERART.PL",
                    "WWW.EBILET.PL Grunwaldzka 186,Poznan", "POCZTAKSIAZKOWA"]
    }

    for category in categories:
        #  print(category)
        tablica = categories.get(category)
        for element in tablica:
            #  print(name, "-", element)
            if element in name:
                return category

    return "OTHER"


def uploadData(rows, wks):
    wks.insert_row(["DATE", "NAME", "AMOUNT", "CATEGORY", "PAYMENT"], 1)
    for row in rows:
        wks.insert_row([row[0], row[1], row[2], row[3], row[4]], 2)
        time.sleep(2)


def main(y, m):
    year = y
    month = m
    file = f"Data/Lista_operacji_{year}_{month}.csv"

    transactions = []

    sa = gspread.service_account()
    sh = sa.open("Personal Finance")
    # wks = sh.worksheet(f"{year}/{month}")
    wks = sh.add_worksheet(title=f"{year}/{month}", rows="150", cols="20")
    rows = gettingData(file, transactions)

    uploadData(rows, wks)


main("2020", "01")
main("2020", "02")
main("2020", "03")
main("2020", "04")
main("2020", "05")
main("2020", "06")
main("2020", "07")
main("2020", "08")
main("2020", "09")
main("2020", "10")
main("2020", "11")
main("2020", "12")
main("2021", "01")
main("2021", "02")
main("2021", "03")
main("2021", "04")
main("2021", "05")
main("2021", "06")
main("2021", "07")
main("2021", "08")
main("2021", "09")
main("2021", "10")
main("2021", "11")
main("2021", "12")
main("2022", "01")
main("2022", "02")
main("2022", "03")
main("2022", "04")
main("2022", "05")
main("2022", "06")
main("2022", "07")
