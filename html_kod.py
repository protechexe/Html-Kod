from bs4 import BeautifulSoup
from tabulate import tabulate
from art import *
import platform
import codecs
import requests
import time
import os

def ClearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def PrintBanner():
    banner = text2art("HTML TR", font="big", chr_ignore=True)
    print(banner)
    print("Web Site Kod Paneline Hoş Geldiniz!")
    print("Programı yazan: Yunus Emre")
    print("İnstagram: @yuns.eemrree")
    print("-"*65,"\n")

def PrintMenu():
    table = [
        ["[INFO] Programa web site linkini girin"],
        ["[INFO] Program web sitesinden HTML,CSS,JAVASCRİPT kodlarını çeker."],
        ["[INFO] Sonrasında bunu 'main.txt' dosyasına yazar ve ilgili klasöre kaydeder."],
        ["[INFO] Program sadece statü kodu 200 olan web siteden veri çekebilir."],
    ]
    headers = ["Program Bilgisi"]
    print(tabulate(table, headers, tablefmt="grid"))

def ProgramSuresi():
    while True:
        islem = GetInput("Devam etmek için entera, programı sonlandırmak için 5 e basın: ")
        if islem == "5":
            exit()
        else:
            break

def GetInput(prompt):
    return input("[?]" + prompt)

def GetDownloadPath():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Darwin":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Linux":
        if "ANDROİD_DATA" is os.environ:
            return "/data/data/com.termux/files/home/downloads"
        else:
            return os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Android" or "linux":
        return "/storage/emulated/0/Download"
    else:
        raise Exception("Desteklenmeyen Platform")
    
def VeriYazdir():
    try:
        url = GetInput("Lütfen sitenin linkini girin: ")
        url = requests.get(url)

        if url.status_code == 200:
            soup = BeautifulSoup(url.content, "html.parser")

            formatted_html = soup.prettify()

            download_path = GetDownloadPath()
            file_path = os.path.join(download_path, "main.txt")

            file_path = file_path.replace("\\","/")

            if not os.path.exists(download_path):
                os.makedirs(download_path)

            with codecs.open(file_path, "w", encoding="utf-8") as dosya:
                dosya.write(formatted_html)

            
            print("[INFO] Site kodları dosyaya yazılıp kaydediliyor..")
            time.sleep(3)
            print(f"[INFO] Site kodları yazdırılıp {file_path} yoluna kaydedildi.")
        else:
            print(f"[INFO] Siteden veri çekilemedi. Statü kodu: {url.status_code}")
            print(f"[INFO] Statü kodu {url.status_code} olduğundan veri çekilemez.")

    except Exception as e:
        print("Bir hata oluştu.",e)

    finally:
        ProgramSuresi()

while True:
    ClearScreen()
    PrintBanner()
    PrintMenu()
    VeriYazdir()
