from colorama import Fore, Back, Style, init
init(autoreset=True)
import webbrowser
import time
while True:
    print(Fore.GREEN + """
    
M""MMMMMMMM oo          dP       MM"""""""`YM dP       oo          dP                         
M  MMMMMMMM o8          88       MM  mmmmm  M 88       o8          88                         
M  MMMMMMMM dP 88d888b. 88  .dP  M'        .M 88d888b. dP .d8888b. 88d888b. .d8888b. 88d888b. 
M  MMMMMMMM 88 88'  `88 88888"   MM  MMMMMMMM 88'  `88 88 Y8ooooo. 88'  `88 88ooood8 88'  `88 
M  MMMMMMMM 88 88    88 88  `8b. MM  MMMMMMMM 88    88 88       88 88    88 88.  ... 88       
M         M dP dP    dP dP   `YP MM  MMMMMMMM dP    dP dP `88888P' dP    dP `88888P' dP       
MMMMMMMMMMM                      MMMMMMMMMMMM                                                 
                                                                                              

    
""")
    print(Style.RESET_ALL)
    fake = str(input(Fore.BLUE + "Yanıltıcı (Sahte) Linki Girin : "))
    print(Style.RESET_ALL)
    print(Back.GREEN + "Sahte Link :" + fake + "")
    print(Style.RESET_ALL)
    real = str(input(Fore.BLUE + "Real (Yönlendirilecek Linki Girin : "))
    print(Style.RESET_ALL)
    print(Back.GREEN + "Yönlendirilecek Link :" + real + "")
    print(Style.RESET_ALL)
    print(Fore.GREEN + "-------------------------------------------------")
    print(Style.RESET_ALL)
    time.sleep(2)
    print(Fore.RED + ""+fake+"@"+real+"")
    soru = str(input("Linki Şimdi Açmak İstiyor Musun ? Y&n: "))
    if soru == 'Y':
        webbrowser.open(""+fake+"@"+real+"")
    elif soru == 'n':
        print("Vazgeçildi.")
    
