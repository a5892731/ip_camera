from resources.gui.widgets.labelframe import labelframe

def build_main_window(self):
    def draw_window_attributes():
        '''gui attributes'''
        self.window.title("GUI_program_name")
        self.window.attributes('-fullscreen', True)
        self.window.geometry("{}x{}".format(self.window_width, self.window_height))
        #icon = PhotoImage(file = "files/icon.png")
        #self.window.resizable(width=False, height=False)
        #self.window.iconphoto(True, icon) # icon in upper, left corner of program window
        self.window.config(background = "#cfd1cf") # "hex color picker" search in google

    def main_window_grid():
        '''In the main window, insert the table with labels'''
        def left_menu_cell():
            self.window.columnconfigure(0, minsize=100)
            self.window.rowconfigure(0, minsize=self.window_height)

            self.left_menu_label = labelframe(label=self.window, column=0, row=0)

        def main_cell():
            self.window.columnconfigure(1, minsize = self.window_width - 100)
            #self.window.rowconfigure(0, minsize=self.window_height)

            self.main_label = labelframe(label=self.window, column=1, row=0)

        '''----------------------------------------------------------------------------------------------------------'''
        left_menu_cell()
        main_cell()

    def draw_default_labels():
        '''draw default labels on program start'''
        self.left_menu_bar()
        self.centrtal_window()

    '''--------------------------------------------------------------------------------------------------------------'''
    draw_window_attributes()
    main_window_grid() #  <=============================================================== create here your main window shape
    draw_default_labels()

def update_window(self):

    '''camera tasks'''
    if self.camera1.connecton:
        try:
            '''update camera label 
            label from resources.gui.labels._central_window'''
            self.camera1.refresh_image(video_image_max_side_size = self.camera_1_size)
            self.camera_viev1.config(image=self.camera1.image)

        except:
            print("no video")
        '''*/'''

    try:
        self.window.update_idletasks()
        self.window.update()
    except:
        print("Program closed")
        quit()




