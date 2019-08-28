from guizero import App, Text, PushButton, TextBox, info, Combo
def do_something():
    #info("Booking", "Turning Off")
    print (system_state.get())
    
app = App(title="Charley Bot", width=300, height=200, layout="grid")
header = Text(app, text="System is:", size="40", color="blue", grid=[0,0], align="left")
system_state = Combo(app,options=["- Choose -","On","Off"], grid=[2,0], align="left")
turn_off_btn = PushButton(app, command=do_something, text="Print Data", grid=[3,0])
app.display
 
