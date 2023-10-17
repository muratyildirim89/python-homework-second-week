letterList = ["A", "B", "C", "D", "E"]
seatList = [[
    [["X", "A1"], [" ", ""], [" ", ""], [" ", ""], [" ", ""]],
    [["X", "B1"], ["X", "B2"], [" ", ""], [" ", ""], [" ", ""]],
    [["X", "C1"], ["X", "C2"], ["X", "C3"], [" ", ""], [" ", ""]],
    [["X", "D1"], ["X", "D2"], ["X", "D3"], ["X", "D4"], [" ", ""]],
    [["X", "E1"], ["X", "E2"], ["X", "E3"], ["X", "E4"], ["X", "E5"]],
],
            [
                [[" ", ""], [" ", ""], [" ", ""], [" ", ""], ["X", "A5"]],
                [[" ", ""], [" ", ""], [" ", ""], ["X", "B4"], ["X", "B5"]],
                [[" ", ""], [" ", ""], ["X", "C3"], ["X", "C4"], ["X", "C5"]],
                [[" ", ""], ["X", "D2"], ["X", "D3"], ["X", "D4"], ["X",
                                                                    "D5"]],
                [["X", "E1"], ["X", "E2"], ["X", "E3"], ["X", "E4"],
                 ["X", "E5"]],
            ]]
reserveSeat = []
moviegoer = ""
isCompare = False


def seatView(list):
  x = 23

  for i in range(x):
    print("*", end='')
  print("< P E R D E >", end='')

  for i in range(x):
    print("*", end='')
  print("\n")

  for i in range(0, 5):

    print("|  ", letterList[i], ">>|   ", list[i][0][0], "   |   ",
          list[i][1][0], "   |   ", list[i][2][0], "   |   ", list[i][3][0],
          "   |   ", list[i][4][0], "   |\n")

  for i in range(2 * x + 13):
    print("_", end='')
  print("\n")
  print("|       |^^^ 1 ^^^|^^^ 2 ^^^|^^^ 3 ^^^|^^^ 4 ^^^|^^^ 5 ^^^|\n")

  for i in range(2 * x + 13):
    print("*", end='')
  print("\n")


def buyTickets(saloon):
  seatCode = input("Lütfen Satın Almak İstediğiniz Koltuk Kodunu Giriniz: ")
  seatCode = seatCode.upper()
  reserveSeat.clear()
  reserveSeat.append([letterList.index(seatCode[0]), int(seatCode[1])])
  if seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][0] == "X":
    isNull = False
  else:
    isNull = True

  if not isNull:
    print("Koltuk Boş Değil. Lütfen Boş Bir Koltuk Seçiniz...")
    buyTickets(saloon)
  else:
    moviegoer = input("İzleyici Adını Giriniz:")
    moviegoer = moviegoer.upper()
    seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][1] = moviegoer
    print(seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][1],
          " İzleyicisine Bilet Başarılı Bir Şekilde Satıldı.")
    seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][0] = "X"
    seatView(seatList[saloon])


def cancelTickets(saloon):
  seatCode = input("Lütfen İade Almak İstediğiniz Koltuk Kodunu Giriniz: ")
  seatCode = seatCode.upper()
  moviegoer = input("İzleyici Adını Giriniz: ")
  moviegoer = moviegoer.upper()
  reserveSeat.clear()
  reserveSeat.append([letterList.index(seatCode[0]), int(seatCode[1])])

  if (seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][0] == " "):
    print("Koltuk Boş. Lütfen Dolu Bir Koltuk Seçiniz...")
    isCompare = False
    cancelTickets(saloon)
  elif (seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][0] == "X"
        and seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][1]
        == moviegoer.upper()):
    isCompare = True
  else:
    isCompare = False
    print("Bilet Bilgileri Eşleşmemektedir...")

  print("Koltuk Nu:", seatCode, " İzleyici Adı: ", moviegoer)

  if isCompare:
    seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][0] = " "
    seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][1] = ""
    print("İzleyici Bileti İade Edildi.")
    seatView(seatList[saloon])
  else:
    pass


def checkTickets(saloon):
  seatCode = input("Lütfen Kontol Etmek İstediğiniz Koltuk Kodunu Giriniz: ")
  seatCode = seatCode.upper()
  moviegoer = input("İzleyici Adını Giriniz: ")
  moviegoer = moviegoer.upper()
  reserveSeat.clear()
  reserveSeat.append([letterList.index(seatCode[0]), int(seatCode[1])])

  if (seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][0] == " "):
    print("Koltuk Boş. Lütfen Dolu Bir Koltuk Seçiniz...")
    isCompare = False
    checkTickets(saloon)
  elif (seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][0] == "X"
        and seatList[saloon][reserveSeat[0][0]][reserveSeat[0][1] - 1][1]
        == moviegoer):
    isCompare = True
  else:
    isCompare = False
    print("Bilet Bilgileri Eşleşmemektedir...")

  if isCompare:
    print("Koltuk Nu:", seatCode, " İzleyici Adı: ", moviegoer)
    print("Bilet Bilgileri Eşleşmektedir...")
  else:
    pass


def Menu(num):

  menuItem = int(
      input(
          "\t\t [1] Koltuk Görüntüle\n\t\t [2] Bilet Satın Al\n\t\t [3] Bilet İade\n\t\t [4] Bilet Kontrol\n"
      ))

  if menuItem > 0 and menuItem < 5:
    if menuItem == 1:
      seatView(seatList[num])
    if menuItem == 2:
      buyTickets(num)
    if menuItem == 3:
      cancelTickets(num)
    if menuItem == 4:
      checkTickets(num)
  else:
    print("Hatalı Seçim Yapıldı.")


def FilmSelect():
  filmEnum = int(
      input(
          "Lütfen Film Seçiniz\n [1] Cars (Arabalar)\n [2] Ice Age (Buz Devri)\n"
      ))

  if filmEnum == 1 or filmEnum == 2:
    Menu(filmEnum - 1)
  else:
    print("Hatalı seçim yapıldı...")


while True:
  FilmSelect()
