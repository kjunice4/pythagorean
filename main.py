from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen


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
                app.root.current = "Pythagorean"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Pythagorean Step by Step Solver"
            on_release:
                app.root.current = "Pythagorean"
                root.manager.transition.direction = "left" 

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
                text: "Pythagorean Step by Step Solver"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Clear Entry"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 1, 0 , 0 , 1
                    on_release:
                        a.text = ""
                        b.text = ""
                        
                Button:
                    id: steps
                    text: "Clear Answers"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()
                        
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
                text: "a^2 + b^2 = c^2"       
                   
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                Label:
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    text: "a :"
                                                        
                TextInput:
                    id: a
                    text: a.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:4 - len(a.text)]  
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5        
        
                Label:
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    text: "b :"
                                                    
                TextInput:
                    id: b
                    text: b.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10          
                    input_filter: lambda text, from_undo: text[:4 - len(b.text)]  
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
    
                Button:
                    id: steps
                    text: "Calculate"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 1 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        Pythagorean.steps(a.text + "," + b.text)    
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    

""")

class Pythagorean(Screen):
    layouts = []
    def steps(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        entry = str(entry).replace(" ","")
        entry = list(entry.split(","))
        while float(entry[0]) > 0 and float(entry[1]) > 0:
            print("entry ;", entry)
            entry = str(entry[0]) + "^2 " + "+ " + str(entry[1]) + "^2 = c^2"
            self.ids.list_of_steps.add_widget(Label(text="Pythagorean : " + entry, font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
            try:
                equal_sign = entry.find("=")
                entry_a_b = entry[:equal_sign].replace(" ","")
                list_a_b = entry_a_b.split("+")
                print("list_a_b",list_a_b)
                
                c = entry[equal_sign+1:].replace(" ","")
                
                a = list_a_b[0]
                a_solved = str(eval(str(a).replace("^","**")))
                print("a_solved",a_solved)
                self.ids.list_of_steps.add_widget(Label(text="Entry a : " + a + " = " + format(float(a_solved),","), font_size = 50, size_hint_y= None, height=100))
    
                b = list_a_b[1]
                b_solved = str(eval(str(b).replace("^","**")))
                print("b_solved",b_solved)           
                
                self.ids.list_of_steps.add_widget(Label(text="Entry b : " + b + " = " + format(float(b_solved),","), font_size = 50, size_hint_y= None, height=100))
                
                ab_added = str(float(a_solved) + float(b_solved))
                
                self.ids.list_of_steps.add_widget(Label(text="Add " + format(float(a_solved),",") + " + " + format(float(b_solved),",") + " = " + ab_added , font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= c + " = " + format(float(ab_added),","), font_size = 50, size_hint_y= None, height=100))
                solved = str(float(ab_added)**.5)
                print("solved",solved)
                if solved[-2] == "." and solved[-1] == "0":
                    self.ids.list_of_steps.add_widget(Label(text= "√(" + c + ") = " + "√(" + format(float(ab_added),",") + ")", font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "c = " + format(float(solved),","), font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    break
                else:
                    self.ids.list_of_steps.add_widget(Label(text= "√(" + c + ") = " + "√(" + format(float(ab_added),",") + ")", font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "c = " + "√(" + format(float(ab_added),",") + ")", font_size = 50, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    break
                
            except Exception:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
                self.layouts.append(layout)
                break
        print("entry neg: ",entry)
        if entry[0].count("-") > 0 or entry[1].count("-") > 0:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 50, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "_________________________________________________________________________________________________________________________________________________________" ,font_size = 50, size_hint_y= None, height=100))
            self.layouts.append(layout)
        
class Homepage(Screen):
    pass            
           
sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Pythagorean(name="Pythagorean"))     
sm.current = "Homepage"   


class Pythagorean(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Pythagorean().run()
    

