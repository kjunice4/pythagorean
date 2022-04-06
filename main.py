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
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"         
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared-math,LLC © : Pythagorean Calculator"
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
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit KSquared-math,LLC ©"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc/subscribe')
                    
            Button:
                font_size: 75
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-math,LLC ©"
                    
            Image:
                source: 'KSquared_QR_code.png'
                size_hint_y: None
                height: 1000
                width: 1000
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
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
                font_size: 60
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-math?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Pythagorean Calculator v0.1"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
""")


#Pythagorean STEPS
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
                text: "Pythagorean Calculator"
                    
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
                        c.text = ""
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
                esc_key:
                    
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
                
            TextInput:
                id: c
                text: c.text
                multiline: False
                hint_text:"c ="
                font_size: 125
                size_hint_y: None
                height: 200
                padding: 10          
                input_filter: lambda text, from_undo: text[:3 - len(c.text)]  
                
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
                    Pythagorean.steps(a.text + "," + b.text + "," + c.text)    
                       
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
                
    layouts = []
    def steps(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            entry = str(entry).replace(" ","")
            entry = entry.split(",")
            print("entry",entry)
            
            i = 0
            while i< len(entry):
                if entry[i] == '':
                    print("found empty")
                    entry[i] = "0"
                    print("entry[" + str(i) + "] = " + entry[i])
                i = i + 1
            
            print("entry",entry)
            
            a = entry[0]
            print("a: ",a)
                
            b = entry[1]
            print("b: ",b)
                
            c = entry[2]
            print("c: ",c)
            
            c_squared = str(int(c)**2)
            print("c_squared",c_squared)
            
            # 3 + 4 = 5
            if int(entry[0]) > 0 and int(entry[1]) > 0 and int(entry[2]) > 0:
                print()
                print("Is this entry valid?")
                
                entry_evaled = str(eval(str(int(a)**2) + "+" + str(int(b)**2)))
                print("entry_evaled = ",entry_evaled)
                
                if str(entry_evaled) == str(c_squared):
                    print("entry_evaled = c")
                    self.ids.list_of_steps.add_widget(Label(text= str(a) + "\u00B2"  + " + " + str(b) + "\u00B2" + " = " + str(c) + "\u00B2", font_size = 50, size_hint_y= None, height=100))
                    
                    a_squared = str(int(a)**2)
                    b_squared = str(int(b)**2)
                    
                    ab = str(int(a_squared) + int(b_squared))
                    
                    self.ids.list_of_steps.add_widget(Label(text= str(a_squared) + " + " + str(b_squared) + " = " + str(c_squared), font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(ab) + " = " + str(c_squared), font_size = 50, size_hint_y= None, height=100))

                else:
                    print("entry_evaled does not = c!!!!!!!")
                    self.ids.list_of_steps.add_widget(Label(text= "Input does not equate to triangle!", font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
            
            # 3 + b = 5 OR a + 4 = 5
            elif int(entry[0]) >= 0 or int(entry[1]) >= 0 and int(entry[2]) >= 0:
                
                a_squared = str(int(a)**2)
                b_squared = str(int(b)**2)
                c_squared = str(int(c)**2)
                
                if int(entry[0]) > 0 and int(entry[1]) > 0:
                    print("a and b are valid")
                    print()
                    print("Solve for a!")
                    
                    self.ids.list_of_steps.add_widget(Label(text= str(a) + "\u00B2"  + " + " + str(b) + "\u00B2" + " = c\u00B2", font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(a_squared)  + " + " + str(b_squared) + " = c\u00B2", font_size = 50, size_hint_y= None, height=100))

                    a_plus_b = int(a_squared) + int(b_squared)
                    print("a_plus_b = ",a_plus_b)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "c\u00B2" + " = " + str(a_plus_b) , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "\u221a(" + " c\u00B2)" + " = " + "\u221a(" + str(a_plus_b) + ")" , font_size = 50, size_hint_y= None, height=100))

                    a_plus_b_root = str(float(a_plus_b)**.5)
                    print("a_plus_b_root = ",a_plus_b_root)

                    if a_plus_b_root[-2] == "." and a_plus_b_root[-1] == "0":
                        self.ids.list_of_steps.add_widget(Label(text= "c = " + format(float(a_plus_b_root),","), font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text= "c = " + "\u221a(" + format(float(a_plus_b),",") + ")", font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                                        
                    if a_plus_b_root == "0.0":
                        self.ids.list_of_steps.add_widget(Label(text= "0.0 cannot form a valid line for triangle" ,font_size = 50, size_hint_y= None, height=100))
                    
                elif int(entry[0]) > 0 and int(entry[2]) > 0:
                    print("a and c are valid")
                    print()
                    print("Solve for b!")
                    
                    self.ids.list_of_steps.add_widget(Label(text= str(a) + "\u00B2"  + " + " + "b\u00B2" + " = " + str(c) + "\u00B2", font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "b\u00B2" + " = " + str(c) + "\u00B2" + " - " + str(a) + "\u00B2" , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "b\u00B2" + " = " + str(c_squared) + " - " + str(a_squared) , font_size = 50, size_hint_y= None, height=100))
                    
                    c_minus_a = int(c_squared) - int(a_squared)
                    print("c_minus_a = ",c_minus_a)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "b\u00B2" + " = " + str(c_minus_a) , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "\u221a(" + " b\u00B2)" + " = " + "\u221a(" + str(c_minus_a) + ")" , font_size = 50, size_hint_y= None, height=100))
                    
                    c_minus_a_root = str(float(c_minus_a)**.5)
                    print("c_minus_a_root = ",c_minus_a_root)

                    if c_minus_a_root[-2] == "." and c_minus_a_root[-1] == "0":
                        self.ids.list_of_steps.add_widget(Label(text= "b = " + format(float(c_minus_a_root),","), font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text= "b = " + "\u221a(" + format(float(c_minus_a),",") + ")", font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                    if c_minus_a_root == "0.0":
                        self.ids.list_of_steps.add_widget(Label(text= "0.0 cannot form a valid line for triangle" ,font_size = 50, size_hint_y= None, height=100))
                    
                elif int(entry[1]) > 0 and int(entry[2]) > 0:
                    print("b and c are valid")
                    print()
                    print("Solve for a!")
                    
                    self.ids.list_of_steps.add_widget(Label(text= "a\u00B2"  + " + " + str(b) + "\u00B2" + " = " + str(c) + "\u00B2", font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "a\u00B2" + " = " + str(c) + "\u00B2" + " - " + str(b) + "\u00B2" , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "a\u00B2" + " = " + str(c_squared) + " - " + str(b_squared) , font_size = 50, size_hint_y= None, height=100))
                    
                    c_minus_b = int(c_squared) - int(b_squared)
                    print("c_minus_b = ",c_minus_b)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "a\u00B2" + " = " + str(c_minus_b) , font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "\u221a(" + " a\u00B2)" + " = " + "\u221a(" + str(c_minus_b) + ")" , font_size = 50, size_hint_y= None, height=100))
                    
                    c_minus_b_root = str(float(c_minus_b)**.5)
                    print("c_minus_b_root = ",c_minus_b_root)

                    if c_minus_b_root[-2] == "." and c_minus_b_root[-1] == "0":
                        self.ids.list_of_steps.add_widget(Label(text= "a = " + format(float(c_minus_b_root),","), font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text= "a = " + "\u221a(" + format(float(c_minus_b),",") + ")", font_size = 50, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                    if c_minus_b_root == "0.0":
                        self.ids.list_of_steps.add_widget(Label(text= "0.0 cannot form a valid line for triangle" ,font_size = 50, size_hint_y= None, height=100))
                    
                
            else:
                print("Invalid length")                
            
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
        
        if entry[0].count("-") > 0 or entry[1].count("-") > 0 or entry[2].count("-") > 0:
            print("entry neg: ",entry)
            self.ids.list_of_steps.add_widget(Label(text= "Cannot have negative sides of a triangle!" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
        
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass 
           
class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))
sm.add_widget(updates(name="updates"))
sm.add_widget(Pythagorean(name="Pythagorean"))     
sm.current = "Homepage"   


class Pythagorean(App):
    def __init__(self, **kwargs):
        super(Pythagorean, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    Pythagorean().run()
