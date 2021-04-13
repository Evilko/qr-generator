import tkinter as tk
from tkinter import ttk
import qrcode
from pathlib import *

DEFAULT_PATH = Path.cwd() / 'result'


class MainWindow:

    # FIXME: Допилить адаптивность дизайна главного окна
    # TODO: Автоматическая вставка ссылок из буфера обмена при его изменении
    # TODO: Добавить настройки генерации qr-кодов:
    #  1. Само окно с выбором настроек генерации
    #  2. Выбор пути для сохранения кодов
    #  3?. Разные шаблоны для имён итоговых файлов
    #  4?. Превью для настроек
    # TODO: Добавить инфы в README.md

    def __init__(self, root):
        self.root = root
        self.root.title('QR-генератор')
        self.links_list = []
        self.links_list_var = tk.StringVar(value=self.links_list)
        self.root.geometry('600x400+200+100')

        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        ttk.Style().configure('Gen.TButton', justify='center')
        ttk.Style().configure('Credits.TLabel', foreground='grey')
        ttk.Style().configure('Red.TFrame', background='red')
        ttk.Style().configure('Green.TFrame', background='green')
        ttk.Style().configure('Blue.TFrame', background='blue')

        # Главный фрейм окна
        self.mainframe = ttk.Frame(root, padding=5, style='Green.TFrame')
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.mainframe.columnconfigure(0, weight=1)

        # Основной фрейм, в котором будет список ссылок и кнопки управления списком
        self.frm_links = ttk.Frame(self.mainframe, padding=3, style='Red.TFrame')

        # Фрейм с кнопками для списка
        self.frm_links_buttons = ttk.Frame(self.frm_links)

        # Кнопки
        self.btn_add = ttk.Button(self.frm_links_buttons, text='Добавить', command=self.add_link)
        self.btn_remove = ttk.Button(self.frm_links_buttons, text='Удалить', command=self.remove)
        self.btn_clear = ttk.Button(self.frm_links_buttons, text='Очистить список', command=self.clear_list)

        # Фрейм со списком ссылок
        self.frm_links_list = ttk.Frame(self.frm_links, width=300, height=400,style='Green.TFrame')
        self.links_listbox = tk.Listbox(self.frm_links_list, height=10, listvariable=self.links_list_var)
        self.links_scroll = ttk.Scrollbar(self.frm_links_list, orient=tk.VERTICAL, command=self.links_listbox.yview)
        self.links_listbox['yscrollcommand'] = self.links_scroll.set

        # Фрейм с кнопками для генерации кодов и вызова окна настроек
        self.frm_process_buttons = ttk.Frame(self.mainframe, style='Blue.TFrame')

        # Кнопки генерации и настроек
        self.btn_generate = ttk.Button(self.frm_process_buttons, text='Генерировать\nкод',
                                       command=self.generate, style='Gen.TButton')
        self.btn_options = ttk.Button(self.frm_process_buttons, text='Опции')

        # Разработчик =)
        self.lbl_credits = ttk.Label(self.mainframe, text='\u00A9 Андриясов А. А., 2021', style='Credits.TLabel')

        self.draw()

    def remove(self):
        selected_positions = self.links_listbox.curselection()
        if len(selected_positions) > 0:
            for pos in selected_positions:
                self.links_list.pop(pos)
            self.links_list_var.set(self.links_list)

    def add_link(self):
        content = self.root.clipboard_get()
        if content not in self.links_list and content.startswith('http'):
            self.links_list.append(content)
            self.links_list_var.set(self.links_list)

    def clear_list(self):
        self.links_list.clear()
        self.links_list_var.set(self.links_list)

    def generate(self):
        if len(self.links_list) == 0:
            return
        if not DEFAULT_PATH.exists():
            DEFAULT_PATH.mkdir()
        for index, link in enumerate(self.links_list):
            img = qrcode.make(link)
            img.save(DEFAULT_PATH / f'{index}.png')

    def draw(self):
        self.mainframe.grid(row=0, column=0, sticky='wnes')
        self.frm_links.grid(row=0, column=0, sticky='wnes')
        self.frm_links_buttons.grid(row=0, column=0, sticky='w')
        self.btn_add.grid(row=0, column=0)
        self.btn_remove.grid(row=0, column=1, padx=(3, 3))
        self.btn_clear.grid(row=0, column=2)
        self.frm_links_list.grid(row=1, column=0, pady=5, sticky='ew')
        self.links_listbox.grid(row=0, column=0)
        self.links_scroll.grid(row=0, column=1, sticky='ns')
        self.frm_process_buttons.grid(row=1, column=0, sticky='ew')
        self.btn_generate.grid(row=0, column=0, padx=(0, 3))
        self.btn_options.grid(row=0, column=1, sticky='ns')
        self.lbl_credits.grid(row=2, column=0, sticky='es', pady=(10, 0))


def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
