import requests,os,time
from rich import print as prints
from rich.panel import Panel

os.system("clear")
print(" [!]  Subscribe Youtube Ery Devs")
time.sleep(4)
os.system("xdg-open https://youtube.com/channel/UCTpvwoW8MDOut6wln7pRZZQ")
os.system("clear")
prints(Panel(f"[deep_pink3] @Creator: Ery Israndi \n Youtube : Ery Devs \n Github  : eryWibu.com"))

prints(Panel(f"[deep_pink3] [1]. Install Packages \n [2]. Link Termux  \n [3]. Exit"))

wa = input("[?] Pilih : ")

if wa =="1":
   prints(Panel(f"[deep_pink3]   [!] Proses Penginstalan"))
   os.system("pkg update && pkg upgrade")
   os.system("pkg install git")
   os.system("pkg install python3")
   os.system("pkg install python2")
   os.system("pip3 install requests bs4 colorama")
   os.system("pip2 install requests bs4 colorama")
   prints(Panel(f"[deep_pink3] [!] Install Selesai"))
   time.sleep(5)
   os.system("python install.py")
if wa =="2":
   os.system("xdg-open https://www.mediafire.com/file/k4tya4lmxbxi7rb/com.termux_118.apk/file")
   os.system("python install.py")
if wa =="3":
   os.system("exit")
