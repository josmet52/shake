import tkinter as tk


class ShakeLib():

    def __init__(self, msg_list, msg_display):
        
        self.msg_list = msg_list
        self.msg_display = msg_display

    def manage_info(self, v_msg, v_color = 0):
        """
            this function display a message 
            input : v_msg : message to display 
         """
        self.msg_list.insert(tk.END, v_msg)
        self.msg_list.see("end")
        
        if v_color > 0:
            if v_color == 1:
                self.msg_list.itemconfig(tk.END, fg='black')
            elif v_color == 2:
                self.msg_list.itemconfig(tk.END, fg='blue')
            elif v_color == 3:
                self.msg_list.itemconfig(tk.END, fg='green')
            elif v_color == 4:
                self.msg_list.itemconfig(tk.END, fg='red')
            elif v_color == 5:
                self.msg_list.itemconfig(tk.END, fg='red')
                self.msg_list.itemconfig(tk.END, bg='yellow')
                
        self.msg_display.update()
        
    def run_shake(self, verbose_onoff):
        if verbose_onoff : self.manage_info("run shake", 1)
        
    def run_settings(self, verbose_onoff):
        if verbose_onoff : self.manage_info("run settings", 1)
