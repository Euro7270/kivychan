# -*- coding: utf-8 -*-
import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.button import Label,Button
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from datetime import datetime
from kivy.core.window import Window

import geocoder
from bs4 import BeautifulSoup
import requests
import webbrowser
import urllib.parse


#ウィンドウを作成
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')

"""
canvas = tk.Canvas(root, width = 800, height = 600)#Canvasの作成
canvas.create_rectangle(0, 0, 800, 600, fill = '#FFE4C4')#塗りつぶし
canvas.place(x=0, y=0)

#エントリー
EditBox = tk.Entry(width=50)
EditBox.pack(ipadx=10,ipady=10)
EditBox.insert(tk.END,"ローマ字で地名を入力してね")


#ここで，valueにEntryの中身が入る
value = EditBox.get()

#チェックボックス(個室あり)
Val1 = tk.IntVar()
Val1.set(False)
private_room = tk.Checkbutton(text='個室あり', variable=Val1)
private_room.pack()
private_room.place(x=20,y=100)

#チェックボックス(禁煙席)
Val2 = tk.IntVar()
Val2.set(False)
smoke = tk.Checkbutton(text='禁煙席あり', variable=Val2)
smoke.pack()
smoke.place(x=20,y=120)

#チェックボックス(ランチあり)
Val3 = tk.IntVar()
Val3.set(False)
lunch = tk.Checkbutton(text='ランチあり', variable=Val3)
lunch.pack()
lunch.place(x=20,y=140)

#チェックボックス(wifiの有無)
Val4 = tk.IntVar()
Val4.set(False)
wifi = tk.Checkbutton(text='Wi-Fiあり', variable=Val4)
wifi.pack()
wifi.place(x=20,y=160)

#チェックボックス(食べ放題)
Val5 = tk.IntVar()
Val5.set(False)
free_food = tk.Checkbutton(text='食べ放題', variable=Val5)
free_food.pack()
free_food.place(x=20,y=180)

#チェックボックス（駐車場あり）
Val6 = tk.IntVar()
Val6.set(False)
parking = tk.Checkbutton(text='駐車場あり', variable=Val6)
parking.pack()
parking.place(x=20,y=200)
"""
class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super(RootWidget,self).__init__(cols=2)
        #Checkboxを作成
        self.label=Label(text=u"個室あり",font_size = "15sp", font_name = 'ipaexg00201/ipaexg.ttf')
        self.add_widget(self.label)
        self.private_room = CheckBox()
        self.private_room.bind(active=self.private_room)
        self.add_widget(self.private_room)

        self.label=Label(text=u"禁煙席あり",font_size = "15sp", font_name = 'ipaexg00201/ipaexg.ttf')
        self.add_widget(self.label)
        self.checkbox2 = CheckBox()
        self.checkbox2.bind(active=self.on_checkbox_active)
        self.add_widget(self.checkbox2)

        self.label=Label(text=u"ランチあり",font_size = "15sp", font_name = 'ipaexg00201/ipaexg.ttf')
        self.add_widget(self.label)
        self.checkbox3 = CheckBox()
        self.checkbox3.bind(active=self.on_checkbox_active)
        self.add_widget(self.checkbox3)

        self.label=Label(text=u"Wi-Fiあり",font_size = "15sp", font_name = 'ipaexg00201/ipaexg.ttf')
        self.add_widget(self.label)
        self.checkbox4 = CheckBox()
        self.checkbox4.bind(active=self.on_checkbox_active)
        self.add_widget(self.checkbox4)

        self.label=Label(text=u"食べ放題あり",font_size = "15sp", font_name = 'ipaexg00201/ipaexg.ttf')
        self.add_widget(self.label)
        self.checkbox5 = CheckBox()
        self.checkbox5.bind(active=self.on_checkbox_active)
        self.add_widget(self.checkbox5)

        self.label=Label(text=u"駐車場あり",font_size = "15sp", font_name = 'ipaexg00201/ipaexg.ttf')
        self.add_widget(self.label)
        self.checkbox6 = CheckBox()
        self.checkbox6.bind(active=self.on_checkbox_active)
        self.add_widget(self.checkbox6)
        #検索ボタンを作成
        self.btn1=Button(text=u"検索",size_hint = (0.5, 0.5),font_size = "15sp",font_name = 'ipaexg00201/ipaexg.ttf')
        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        layout.add_widget(self.btn1)
        self.add_widget(layout)
        #終了ボタンを作成
        self.btn2=Button(text=u"終了",size_hint = (0.5, 0.5),font_size = "15sp", font_name = 'ipaexg00201/ipaexg.ttf')
        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        layout.add_widget(self.btn2)
        self.add_widget(layout)

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active')
        else:
            print('The checkbox', checkbox, 'is inactive')

    def Nuryoku(self):
        layout = RootWidget() #FloatLayout()
        ti = TextInput(text='Hello world', multiline=False)
        ti.bind(on_text_validate=self.on_enter)
        layout.add_widget(ti)
        return self.layout
    def on_enter(self, ti):
        print("on_enter[%s]" % (ti.text))
 

class App_py(App):
    def build(self):
        self.root = RootWidget()
        self.title = 'Text Input Sample'
        self.icon = 'IMG_5141.jpg'
        return self.root

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(padding=30, orientation='vertical')

        self.label=Label(text="Time Display")
        self.add_widget(self.label)

        Clock.schedule_interval(self.TimerCallback, 1.0)

        self.textinput = TextInput(text='Hello world', multiline=False)
        self.add_widget(self.textinput)

    def TimerCallback(self,dt):
        time=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.textinput.text=time

"""
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "検索"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = tk.Button(self, text="終了", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        value = EditBox.get()
        print(value)
        Localname = value #検索する住所
        g = geocoder.google(Localname)
    
        if(g.lat == None):
            #EditBox.insert(tk.END,">>>値の入力が不正です！")
            #tk.Label(root,text="値の入力が不正です",width=40)
            print("Error/nもう一度入力してください") 
            error_window=tkmsg.showinfo('エラー','値の入力が不正です！')
       
        else:
            print(g.lat,g.lng) 
            url="http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=2e81cf18f550cb53&range=5&order=5"
            url=self.update_url(url,g.lat,g.lng)
            print(url)
            result = requests.get(url) 
            soup = BeautifulSoup(result.text, "html.parser")
            lb.insert(tk.END,str(value+'の検索結果です'))
            lb.insert(tk.END,'---------------------------------------------------------')
            for shop in soup.findAll('shop'):
                lb.insert(tk.END,shop.find('name').string)
            lb.insert(tk.END,'---------------------------------------------------------')
            lb.insert(tk.END,'検索結果は以上です')
            lb.insert(tk.END,'---------------------------------------------------------')
"""            
            
"""
    def update_url(self,url,lat,lng):
        url+="&lat="+str(lat)
        url+="&lng="+str(lng)
        url+="&private_room="+str(Val1.get())
        url+="&smoke="+str(Val2.get())
        url+="&lunch="+str(Val3.get())
        url+="&wifi="+str(Val4.get())
        url+="&free_food="+str(Val5.get())
        url+="&parking="+str(Val6.get())
        return url

lb = tk.Listbox(root,width=50)
lb.pack() 

def action(event):
    for i in lb.curselection():
        print(lb.get(i))
        s = lb.get(i)
        s_quote = urllib.parse.quote(s) 
        map_url = "https://www.google.co.jp/maps/place/"
        map_url+=str(s_quote)
        webbrowser.open(map_url)

              
lb.bind('<<ListboxSelect>>',action)
app = Application(master=root)
app.mainloop()
root.mainloop()
"""
App_py().run()
