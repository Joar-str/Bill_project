from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty, ListProperty
from kivy.storage.jsonstore import JsonStore


class MainApp(MDApp):
    scr2 = ObjectProperty()
    scr3 = ObjectProperty()
    text_color = ListProperty()

    def build(self):

        self.sm = ScreenManager()
        self.sm.add_widget(Builder.load_file('kv/Screen_one.kv'))
        self.sm.add_widget(Builder.load_file('kv/Screen_two.kv'))
        self.sm.add_widget(Builder.load_file('kv/Screen_three.kv'))

        return self.sm

    def reset(self):
        self.sm.get_screen('scr2').ids.text_name.text = ''
        self.sm.get_screen('scr2').ids.text_name2.text = ''
        self.sm.get_screen('scr2').ids.text_name3.text = ''
        self.sm.get_screen('scr2').ids.text_name4.text = ''
        self.sm.get_screen('scr2').ids.text_name5.text = ''
        self.sm.get_screen('scr2').ids.text_name6.text = ''

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.stored_data = JsonStore('data.json')

    def update_label1(self):

        #Function that updates all labels on screen three.

        text_name = self.sm.get_screen('scr2').ids.text_name.text
        scr3_label1 = self.sm.get_screen('scr3').ids['screen3_label1']
        scr3_label1.text = str(text_name)

    def update_label2(self):

        text_name2 = self.sm.get_screen('scr2').ids.text_name2.text
        scr3_label2 = self.sm.get_screen('scr3').ids['screen3_label2']
        scr3_label2.text = str(text_name2)

    def update_label3(self):

        text_name3 = self.sm.get_screen('scr2').ids.text_name3.text
        scr3_label3 = self.sm.get_screen('scr3').ids['screen3_label3']
        scr3_label3.text = str(text_name3)

    def update_label4(self):

        text_name4 = self.sm.get_screen('scr2').ids.text_name4.text
        scr3_label4 = self.sm.get_screen('scr3').ids['screen3_label4']
        scr3_label4.text = str(text_name4)

    def update_label5(self):

        text_name5 = self.sm.get_screen('scr2').ids.text_name5.text
        scr3_label5 = self.sm.get_screen('scr3').ids['screen3_label5']
        scr3_label5.text = str(text_name5)

    def update_label6(self):

        text_name6 = self.sm.get_screen('scr2').ids.text_name6.text
        scr3_label6 = self.sm.get_screen('scr3').ids['screen3_label6']
        scr3_label6.text = str(text_name6)




MainApp().run()
