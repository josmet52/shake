import tkinter as tk


class ShakeLib():

    def __init__(self, msg_list, msg_display):
        a = 0
        self.msg_list = msg_list
        self.msg_display = msg_display

    def manage_info(self, v_msg, v_color=0):
        """
            this function display a message 
            input : v_msg : message to display 
         """
        self.msg_list.insert(tk.END, v_msg)
        self.msg_list.see("end")
        self.msg_display.update()
