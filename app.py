# -*- coding: utf-8 -*-
import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.button import Label,Button
from kivy.config import Config
from kivy.uix.textinput import TextInput #テキストボックス作成
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

import geocoder
from bs4 import BeautifulSoup
import requests
import webbrowser
import urllib.parse
import xml.etree.ElementTree as et

resource_add_path('/Users/euro_c/Documents/Python演習課題/Kivy/ipaexg00201')
LabelBase.register(DEFAULT_FONT, 'ipaexg00201/ipaexg.ttf')

#class TestApp(App):
class Rootapp(App):
    def hoi(self):
        title = 'Text Input Sample'
        icon = 'IMG_C3A0B03A7006-1.jpeg'

    def build(self):
        layout = FloatLayout()
        ti = TextInput(text='入力してください',multiline=False)
        ti.bind(on_text_validate=self.on_enter)
        layout.add_widget(ti)
        return layout

    def on_enter(self, ti):
        print("on_enter[%s]" % (ti.text))
        Localname = ti.text
        #検索する住所
        location = requests.get("https://www.geocoding.jp/api?q=" + Localname)
        res = et.fromstring(location.text)
        print(res)

        if(res):
            print(res[2][0].text, res[2][1].text)
            url="http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=2e81cf18f550cb53&range=5&order=5&lat=" + "&lat=" + res[2][0].text + "&lng=" + res[2][1].text
            print(url)
            result = requests.get(url)
            # print(result.text)
            soup = BeautifulSoup(result.text,"html.parser")
            for shop in soup.findAll('shop'):
                print(shop.find('name').string)
                # lb.insert(shop.find('name').string)
        else:
            print("Error/nもう一度入力してください") 


if __name__ == "__main__":
    Rootapp().run()

