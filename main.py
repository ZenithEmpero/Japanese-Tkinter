
#Kung mag run ka ani dapat ang UI folder, a.ico, etc. kay naa sa same directory as this file
#If mo error sa first time nimo mag open try daw check sa internet connection

import tkinter as tk, pickle, os, sys
from tkinter.constants import RIDGE
from PIL import ImageTk, Image
from gtts import gTTS
from playsound import playsound

#   Create/use saved data
z = os.path.isfile('./data')
if z == True:
    with open('data', 'rb') as f:
        ui_mode = pickle.load(f)
else:
    data = open('data', 'w+')
    with open('data', 'wb') as f:
        pickle.dump('light', f)
    with open('data', 'rb') as f:
        ui_mode = pickle.load(f)
        

#   Variables   #
Hiragana = [
    'あ',     'い',     'う',     'え',     'お',

    'か',     'き',     'く',     'け',     'こ',

    'さ',     'し',     'す',     'せ',     'そ',

    'た',     'ち',     'つ',     'て',     'と',

    'な',     'に',     'ぬ',     'ね',     'の',

    'は',     'ひ',     'ふ',     'へ',     'ほ',

    'ま',     'み',     'む',     'め',     'も',

    'や',               'ゆ',               'よ',     

    'ら',     'り',     'る',     'れ',     'ろ',

    'わ',                                   'を'
]

Katakana = [
    'ア',     'イ',     'ウ',     'エ',     'オ',

    'カ',     'キ', 	'ク',  	  'ケ',     'コ',

    'サ',     'シ',     'ス',     'セ',     'ソ',

    'タ',     'チ',     'ツ',     'テ',     'ト',

    'ナ',     'ニ',     'ヌ',     'ネ',     'ノ',

    'ハ',     'ヒ',     'フ',     'ヘ',     'ホ',

    'マ',     'ミ',     'ム',     'メ',     'モ',

    'ヤ',               'ユ', 	            'ヨ',

    'ラ',     'リ',     'ル',     'レ',     'ロ',

    'ワ',    	                            'ヲ'
]

if ui_mode == 'light':
    main_color = 'white'
    secondary_color = '#0d1017'
elif ui_mode == 'dark':
    main_color = '#0d1017'
    secondary_color = 'white'

#   Download mp3    #

z = os.path.exists('./mp3')
if z != True:
    os.makedirs('./mp3')
    for i in range(45):
        a = gTTS(Hiragana[i], lang='ja')
        a.save('./mp3/' + str(i) + '.mp3')

#   Window Details    #
w = tk.Tk()
w.config(background=main_color)
w.title('Japanese Characters')
w.wm_iconbitmap("a.ico")
w.geometry('455x650')
w.resizable(width=False,height=True)

#   Window Contents    #

#----- Images -----
if ui_mode == 'light':
    hir_img = ImageTk.PhotoImage(Image.open('./UI/Hiragana_Select_w.png'))
    kat_img = ImageTk.PhotoImage(Image.open('./UI/Katakana_Select_w.png'))
else:
    hir_img = ImageTk.PhotoImage(Image.open('./UI/Hiragana_Select_d.png'))
    kat_img = ImageTk.PhotoImage(Image.open('./UI/Katakana_Select_d.png'))
set_img = ImageTk.PhotoImage(Image.open('./UI/settings.png'))


#   Event Functions   #
def ChangeToKatakana(Event):
    panel.config(image=kat_img)
    Center_Label.config(text='Katakana')
    hir_can.place(x = -100)
    kat_can.place(x = -5)
def ChangeToHiragana(Event):
    panel.config(image=hir_img)
    Center_Label.config(text='Hiragana')
    hir_can.place(x = -5)
    kat_can.place(x = 500)
    
def Settings(Event):
    global set_switch
    if set_switch:
        set_can.place(anchor='center', x=230, y=-300)
        set_switch = False
    else:
        set_can.place(anchor='center', x=230, y=150)
        set_switch = True

def CharacterClick(i):
    playsound('./mp3/' + str(i) + '.mp3', block=False)

panel= tk.Label(image=hir_img, bg=main_color)
panel.pack()
panel.place(x=-5, y=50)

#----- Buttons -----
#----- Settings Button -----
Settings_Label = tk.Label(image=set_img, bg=main_color)
Settings_Label.pack()
Settings_Label.place(anchor='center', x = 435, y = 20)
Settings_Label.bind('<Button-1>', Settings)

#----- Hiragana Button -----
hiragana_btn = tk.Label(text='Hiragana', font=('MV Boli', 13), bg=main_color, fg=secondary_color)
hiragana_btn.pack()
hiragana_btn.place(x=81, y = 59)
hiragana_btn.bind('<Button-1>', ChangeToHiragana)

#----- Katakana Button -----
katakana_btn = tk.Label(text='Katakana', font=('MV Boli', 13), bg=main_color, fg=secondary_color)
katakana_btn.pack()
katakana_btn.place(x= 230, y= 59)
katakana_btn.bind('<Button-1>', ChangeToKatakana)

#----- Center Label -----
Center_Label = tk.Label(text='Hiragana', font=('Arial', 30), bg=main_color, foreground=secondary_color)
Center_Label.pack()
Center_Label.place(anchor='center', x=230, y=150)

#----- Hiragana Canvas -----
hir_can = tk.Canvas(relief=tk.RIDGE, highlightthickness=0, bg=main_color, width=460, height=800)
hir_can.pack()
hir_can.place(x=-5, y=200)

#----- Katakana Canvas -----
kat_can = tk.Canvas(relief=RIDGE, highlightthickness=0, bg=main_color, width=460, height=800)
kat_can.pack()
kat_can.place(x=500, y=200)

#----- Settings Canvas -----
set_switch = False
set_can = tk.Canvas(bg=main_color, width=370)
set_can.pack()
set_can.place(anchor='center', x=230, y=-300)

#----- Create A Grid -----
#Hiragana Buttons
h_x = 44
h_y = 30
k_x = 44
k_y = 30 #215
btn = []
for i in range(45):
    #Hiragana
    if h_x < 400:
        e = i
        tk.Button(master=hir_can, text=Hiragana[i], bg = main_color, fg = secondary_color, font=("MV Boli", 13), relief=tk.GROOVE, command=lambda i=i: CharacterClick(i)).place(anchor="center", x= h_x, y= h_y)
        h_x += 92
    else:
        tk.Button(master=hir_can, text=Hiragana[i], bg = main_color, fg = secondary_color, font=("MV Boli", 13), relief=tk.GROOVE, command=lambda i=i: CharacterClick(i)).place(anchor="center", x= h_x, y= h_y)
        h_x = 44
        h_y += 80 
    #Katakana
    if k_x < 400:
        tk.Button(master=kat_can, text=Katakana[i], bg = main_color, fg = secondary_color, font=("MV Boli", 13), relief=tk.GROOVE, command=lambda i=i: CharacterClick(i)).place(anchor="center", x= k_x, y= k_y)
        k_x += 92
    else:
        tk.Button(master=kat_can, text=Katakana[i], bg = main_color, fg = secondary_color, font=("MV Boli", 13), relief=tk.GROOVE, command=lambda i=i: CharacterClick(i)).place(anchor="center", x= k_x, y= k_y)
        k_x = 44
        k_y += 80
#----- Change UI Mode -----
bg_config = [w, panel, Settings_Label, hiragana_btn, katakana_btn, Center_Label,  set_can]
fg_config = [hiragana_btn, katakana_btn, Center_Label]
def ChangeUI():
    global z
    if ui_mode == 'light':
        with open('data', 'wb') as f:
            pickle.dump('dark', f)
    else:
        with open('data', 'wb') as f:
            pickle.dump('light', f)
    z = os.path.isfile('./japanese.exe')
    if z == True:
        os.startfile('japanese.exe')
    
    sys.exit()

ui_btn = tk.Button(master=set_can, text='Change Theme', bg=main_color, fg=secondary_color, font=('Arial', 30), command=ChangeUI)
ui_btn.place(anchor='center', x=185, y=100)



w.mainloop()
