from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 60
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Pythagorean Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
            
            Button:
                text: "Pythagorean Calculator"   
                font_size: 75
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Pythagorean"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Visit KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Other apps from KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/subscribe')   
                
            Button:
                font_size: 75
                background_color: 0, 0 , 0 , 1
                size_hint_y: None
                height: 400
                text: "Donate to KSquared,LLC"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/about-ksquared')
            
""")


#EXPONENTS STEPS
Builder.load_string("""
<Pythagorean>
    id:Pythagorean
    name:"Pythagorean"
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Pythagorean Solver"
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        a.text = ""
                        b.text = ""
                        list_of_steps.clear_widgets()            
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "a\u00B2 + b\u00B2 = c\u00B2"       
                                                        
            TextInput:
                id: a
                text: a.text
                multiline: False
                hint_text: "a ="
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10
                input_filter: lambda text, from_undo: text[:3 - len(a.text)]  
                    
            TextInput:
                id: b
                text: b.text
                multiline: False
                hint_text:"b ="
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10          
                input_filter: lambda text, from_undo: text[:3 - len(b.text)]  
                
            Button:
                id: steps
                text: "Calculate"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Pythagorean.steps(a.text + "," + b.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class Pythagorean(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Pythagorean, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            print("Its working ESC = 27 LENGTH")
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        print("Length is almost working")        
        if sm.current != "Homepage":
            print("Its working List")
            sm.transition.direction = 'right'
            sm.current = sm.previous()
            
    layouts = []
    def steps(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            entry = str(entry).replace(" ","")
            entry = list(entry.split(","))
            while float(entry[0]) > 0 and float(entry[1]) > 0:
                print("entry ;", entry)
                entry = str(entry[0]) + "\u00B2 " + "+ " + str(entry[1]) + "\u00B2 = c\u00B2"
                self.ids.list_of_steps.add_widget(Label(text= entry, font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                equal_sign = entry.find("=")
                entry_a_b = entry[:equal_sign].replace(" ","")
                list_a_b = entry_a_b.split("+")
                print("list_a_b",list_a_b)
                
                c = entry[equal_sign+1:].replace(" ","")
                
                a = list_a_b[0]
                a_solved = str(eval(str(a).replace("\u00B2","**2")))
                print("a_solved",a_solved)
                self.ids.list_of_steps.add_widget(Label(text="Entry a : " + a + " = " + format(float(a_solved),","), font_size = 60, size_hint_y= None, height=100))
    
                b = list_a_b[1]
                b_solved = str(eval(str(b).replace("\u00B2","**2")))
                print("b_solved",b_solved)           
                
                self.ids.list_of_steps.add_widget(Label(text="Entry b : " + b + " = " + format(float(b_solved),","), font_size = 60, size_hint_y= None, height=100))
                
                ab_added = str(float(a_solved) + float(b_solved))
                
                self.ids.list_of_steps.add_widget(Label(text="Add " + format(float(a_solved),",") + " + " + format(float(b_solved),",") + " = " + ab_added , font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= c + " = " + format(float(ab_added),","), font_size = 60, size_hint_y= None, height=100))
                solved = str(float(ab_added)**.5)
                print("solved",solved)
                
                if solved[-2] == "." and solved[-1] == "0":
                    self.ids.list_of_steps.add_widget(Label(text= "\u221a(" + c + ") = " + "\u221a(" + format(float(ab_added),",") + ")", font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "c = " + format(float(solved),","), font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    break
                else:
                    self.ids.list_of_steps.add_widget(Label(text= "\u221a(" + c + ") = " + "\u221a(" + format(float(ab_added),",") + ")", font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "c = " + "\u221a(" + format(float(ab_added),",") + ")", font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    break
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
        print("entry neg: ",entry)
        if entry[0].count("-") > 0 or entry[1].count("-") > 0:
            self.ids.list_of_steps.add_widget(Label(text= "Cannot have negative sides of a triangle!" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
        
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass 
           
sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(Pythagorean(name="Pythagorean"))     
sm.current = "Homepage"   


class Pythagorean(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Pythagorean().run()
 
