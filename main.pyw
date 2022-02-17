from os import system
import easygui
from infi.systray import SysTrayIcon

def one_hour(systray):
    system("shutdown /s /t 3600")

def two_hours(systray):
    system("shutdown /s /t 7200")

def four_hours(systray):
    system("shutdown /s /t 14400")

def custom_timer(systray):
    myvar = easygui.enterbox("Tempo em minutos:")
    if myvar != None:
        system(f"shutdown /s /t {int(myvar) * 60}")

menu = []

menu.append( ("1 Hora", None, one_hour) )
menu.append( ("2 Horas", None, two_hours) )
menu.append( ("4 Horas", None, four_hours) )
menu.append( ("Custom Timer", None, custom_timer) )

systray = SysTrayIcon("icon.ico", "Timer de Desligamento", tuple(menu))
systray.start()