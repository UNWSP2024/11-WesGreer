# GUI Show Info Program
# Written By Wesley Greer on 4/15/2026
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
# Create frames for info and buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
# Create a label to show info once triggered
        self.value = tkinter.StringVar()
        self.address_label = tkinter.Label(self.top_frame, textvariable = self.value)
# Create show info and quit buttons
        self.address_button = tkinter.Button(self.bottom_frame, text = 'Show Info', command = self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)
# pack the label, buttons, and frames
        self.address_label.pack()
        self.address_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()
# define show info 
    def show_info(self):
        self.value.set("""Wesley Scott Greer 
        3050 45th St. 
        Albert Lea, MN 39489""")

my_gui = MyGUI()
