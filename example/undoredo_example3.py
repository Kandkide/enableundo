# coding: utf-8
import tkinter as tk
# Allow importing modules from the perspective of one directory above.
if __name__ == '__main__':
    import os, sys; sys.path.append(os.path.join(os.path.dirname(__file__), '..' ))
    
from enableundo import EnableUndoRedo


class TextWdgt:
    def __init__(self, master):
        self.state = EnableUndoRedo()
        self.entry = tk.Entry()
        self.entry.bind('<Return>', self.when_return_on_entry)
        self.entry.pack(fill='x')
        self.text = tk.Text(master)
        master.bind('<Control-Key-u>', self.undo)
        master.bind('<Control-Key-r>', self.redo)
        self.text.pack()

        self.entry.insert(tk.END, "Type any word and press enter")
        self.entry.select_range(0, tk.END)
        self.entry.focus_set()

    def undo(self, *args):
        self.state.undo()
        self.text.delete(1.0, tk.END)
        if self.state.state is not None:
            self.text.insert(tk.END, self.state.state)

    def redo(self, *args):
        self.state.redo()
        self.text.delete(1.0, tk.END)
        if self.state.state is not None:
            self.text.insert(tk.END, self.state.state)

    def when_return_on_entry(self, *args):
        self.text.insert(tk.END, self.entry.get())
        self.state.state = self.text.get(1.0, tk.END)
        self.text.insert(tk.END, '\n')
        self.entry.delete(0, tk.END)
        
def main():
    root = tk.Tk()
    root.title("Ctrl-U: Undo, Ctrl-R: Redo")

    TextWdgt(root)

    root.mainloop()

# main()
