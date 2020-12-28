import tkinter as tk
from tkinter import ttk


class MainWindow:
    def __init__(self, root):
        root.title('Qr-генератор')
        mainframe = ttk.Frame(root).grid(row=0, column=0)

        frm_linklist = ttk.Frame(mainframe).grid(row=0, column=0, columnspan=2)
        btn_remove = ttk.Button(frm_linklist, text='Удалить', command=self.remove)
        btn_clear = ttk.Button(frm_linklist, text='Очистить список', command=self.clear)
        frm_list = ttk.Frame(frm_linklist)
        btn_remove.grid(row=0, column=0)
        btn_clear.grid(row=0, column=1)
        frm_list.grid(row=1, column=0, columnspan=2)

        btn_generation = ttk.Button(mainframe, text='Сгенерировать\nкоды')
        btn_options = ttk.Button(mainframe, text='Опции')
        btn_generation.grid(row=1, column=0)
        btn_options.grid(row=1, column=1)

    def remove(self):
        pass

    def clear(self):
        pass


def main():
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()

# from tkinter import *
# from tkinter import ttk
#
#
# class FeetToMeters:
#
#     def __init__(self, root):
#
#         root.title("Feet to Meters")
#
#         mainframe = ttk.Frame(root, padding="3 3 12 12")
#         mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#         root.columnconfigure(0, weight=1)
#         root.rowconfigure(0, weight=1)
#
#         self.feet = StringVar()
#         feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
#         feet_entry.grid(column=2, row=1, sticky=(W, E))
#         self.meters = StringVar()
#
#         ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
#         ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)
#
#         ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
#         ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#         ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
#
#         for child in mainframe.winfo_children():
#             child.grid_configure(padx=5, pady=5)
#
#         feet_entry.focus()
#         root.bind("<Return>", self.calculate)
#
#     def calculate(self, *args):
#         try:
#             value = float(self.feet.get())
#             self.meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
#         except ValueError:
#             pass
#
#
# root = Tk()
# FeetToMeters(root)
# root.mainloop()