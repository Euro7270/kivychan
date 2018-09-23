# -*- coding: utf-8 -*-
import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.button import Label,Button
from kivy.config import Config
from kivy.uix.textinput import TextInput #テキストボックス作成
from kivy.uix.floatlayout import FloatLayout
import geocoder
from bs4 import BeautifulSoup
import requests
import webbrowser
import urllib.parse

class TestApp(App):
    def appearance(self):
#       self.root = Rootapp()
        self.title = 'Text Input Sample'
        self.icon = 'IMG_C3A0B03A7006-1.jpeg'
        return 

class Rootapp(App):
    def build(self):
        layout = FloatLayout()
        ti = TextInput(text='国会議事堂',multiline=False,font_name = 'ipaexg00201/ipaexg.ttf')
        ti.bind(on_text_validate=self.on_enter)
        layout.add_widget(ti)
        return layout

    def on_enter(self, ti):
        print("on_enter[%s]" % (ti.text))
#        ti = TextInput.get()
        Localname = ti.text 
        print(Localname)
        #検索する住所
        g = geocoder.google(Localname)
    
        if(g.lat == None):
            print("Error/nもう一度入力してください") 
            #error_window = massegebox.showinfo('エラー','値の入力が不正です！')
        else:
            print(g.lat,g.lng) 
            url="http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=2e81cf18f550cb53&range=5&order=5"
            url=self.update_url(url,g.lat,g.lng)
            print(url)
            result = requests.get(url) 
            soup = BeautifulSoup(result.text, "html.parser")

if __name__ == "__main__":
    Rootapp().run()
TestApp().run()
