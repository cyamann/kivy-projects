from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window

Window.size = (350, 350)
class CalculatorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_string("""
BoxLayout:
    orientation: 'vertical'
    size_hint_x: None
    width : 300
    size: '340dp', '300dp' 
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    
    BoxLayout:
        TextInput:
            id: display
            font_size: 24
            halign: 'right'
            multiline: False
            size: '340dp', '300dp'
    

    GridLayout:
        cols: 4
        spacing: '5dp'
        pos_hint: {'center_x': 0.6, 'center_y': 0.2}
        MDRaisedButton:
            text: '7'
            on_release: app.update_display('7')
        MDRaisedButton:
            text: '8'
            on_release: app.update_display('8')
        MDRaisedButton:
            text: '9'
            on_release: app.update_display('9')
        MDRaisedButton:
            text: '/'
            on_release: app.update_display('/')

        MDRaisedButton:
            text: '4'
            on_release: app.update_display('4')
        MDRaisedButton:
            text: '5'
            on_release: app.update_display('5')
        MDRaisedButton:
            text: '6'
            on_release: app.update_display('6')
        MDRaisedButton:
            text: '*'
            on_release: app.update_display('*')

        MDRaisedButton:
            text: '1'
            on_release: app.update_display('1')
        MDRaisedButton:
            text: '2'
            on_release: app.update_display('2')
        MDRaisedButton:
            text: '3'
            on_release: app.update_display('3')
        MDRaisedButton:
            text: '-'
            on_release: app.update_display('-')

        MDRaisedButton:
            text: '.'
            on_release: app.update_display('.')
        MDRaisedButton:
            text: '0'
            on_release: app.update_display('0')
        MDRaisedButton:
            text: '='
            on_release: app.calculate()
        MDRaisedButton:
            text: '+'
            on_release: app.update_display('+')
""")

    def update_display(self, value):
        self.root.ids.display.text += value

    def calculate(self):
        try:
            result = str(eval(self.root.ids.display.text))
            self.root.ids.display.text = result
        except Exception as e:
            self.root.ids.display.text = 'Error'


if __name__ == '__main__':
    CalculatorApp().run()
