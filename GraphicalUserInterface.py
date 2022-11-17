import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from PIL import Image, ImageTk
import IOHandler
from IOHandler import IOHandler
from Person import Person


class GraphicalUserInterface(object):
    __IO = IOHandler()
    __iterator = 0

    def __init__(self):
        self.lblConfResults = None

        self.window = None

        self.lblId = None
        self.txtId = None

        self.lblConfId = None
        self.txtConfId = None

        self.imageLoader = None
        self.imageRenderer = None
        self.imgId = None

        self.lblResults = None
        self.txtResults = None

        self.lblConfResults = None
        self.txtConfResults = None

        self.imgResult = None

        self.lblSearchId = None
        self.txtSearchId = None

        self.btnPrev = None
        self.btnSearch = None
        self.btnNext = None


    def show(self):
        self.create_window()
        self.create_widgets()
        self.window.mainloop()

    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Rendszerprogamozás - Python - QRDF3V")
        self.window.geometry('630x650')

    def create_widgets(self):

        self.id_str_var = StringVar()
        self.cnfmd_id_str_var = StringVar()
        self.results_str_var = StringVar()
        self.cnfmd_results_str_var = StringVar()
        self.id_img_string_var = StringVar()
        self.results_img_string_var = StringVar()
        self.search_cond_string_var = StringVar()

        self.__value_setting(0)

        # Identifier Row
        self.lblId = tk.Label(self.window, text="Identifier:")
        self.lblId.grid(column=0, row=0, sticky=W, padx=(20, 0), pady=(55, 0))

        self.txtId = tk.Label(self.window, textvariable=self.id_str_var)
        self.txtId.grid(column=1, row=0, sticky=W, pady=(55, 0))

        # Confirmed Identifier Row
        self.lblConfId = tk.Label(self.window, text="Confirmed identifier:")
        self.lblConfId.grid(column=0, row=1, sticky=W, padx=(20, 0), pady=(0, 50))
        self.txtConfId = tk.Entry(self.window, textvariable=self.cnfmd_id_str_var)
        self.txtConfId.grid(column=1, row=1, sticky=W, pady=(0, 50))

        # Identifier image label
        self.imgId = Label(self.window)

        # Results Row
        self.lblResults = tk.Label(self.window, text="Results:")
        self.lblResults.grid(column=0, row=2, sticky=W, padx=(20, 0), pady=(20, 0))
        self.txtResults = tk.Label(self.window, textvariable=self.results_str_var)
        self.txtResults.grid(column=1, row=2, sticky=W, columnspan=3, pady=(20, 0))

        # Confirmed results Row
        self.lblConfResults = tk.Label(self.window, text="Confirmed identifier:")
        self.lblConfResults.grid(column=0, row=3, sticky=W, padx=(20, 0), pady=(20, 5))
        self.txtConfResults = tk.Entry(self.window, width='75', textvariable=self.cnfmd_results_str_var)
        self.txtConfResults.grid(column=1, row=3, sticky=W, columnspan=3, pady=(20, 5))

        # Results image label
        self.imgResult = Label(self.window)

        # Searcher Row
        self.lblSearchId = tk.Label(self.window, text="Identifier: ")
        self.lblSearchId.grid(column=1, row=5, sticky=E)
        self.txtSearchId = tk.Entry(self.window, width='25', textvariable=self.search_cond_string_var)
        self.txtSearchId.grid(column=2, row=5, sticky=W, pady=10)

        # Buttons Row
        self.btnPrev = tk.Button(self.window, text="Show previous", command=self.__prev_update)
        self.btnPrev.grid(column=0, row=6, sticky=W, padx=(20, 0))
        self.btnSearch = tk.Button(self.window, text="Search", command= lambda : self.__search_by_cnfmd_id(self.search_cond_string_var))
        self.btnSearch.grid(column=2, row=6, sticky=S, padx=(0, 40))
        self.btnNext = tk.Button(self.window, text="Show next", command=self.__next_update)
        self.btnNext.grid(column=3, row=6, sticky=E, padx=(0, 20))


    def __text_var_setter(self, i):
        self.id_str_var.set(self.__IO.jsonPersons[i].get_id())
        self.cnfmd_id_str_var.set(self.__IO.jsonPersons[i].get_confirmed_id())
        self.results_str_var.set(self.__IO.jsonPersons[i].get_results())
        self.cnfmd_results_str_var.set(self.__IO.jsonPersons[i].get_confirmed_results())

    def __id_image_var_setter(self, i):
        self.id_img_string_var.set(IOHandler().abs_pic_path_creator(self.__IO.jsonPersons[i].get_id_image()))
        self.imageLoader = Image.open(self.id_img_string_var.get())
        self.imageRenderer = ImageTk.PhotoImage(self.imageLoader)
        self.imgId = Label(self.window, image=self.imageRenderer)
        self.imgId.image = self.imageRenderer
        self.imgId.grid(column=2, row=0, rowspan=2, columnspan=2, sticky=W, padx=20, pady=20)

    def __result_image_var_setter(self, i):
        self.results_img_string_var.set(IOHandler().abs_pic_path_creator(self.__IO.jsonPersons[i].get_result_image()))
        self.imageLoader = Image.open(self.results_img_string_var.get())
        self.imageRenderer = ImageTk.PhotoImage(self.imageLoader)
        self.imgResult = Label(self.window, image=self.imageRenderer)
        self.imgResult.image = self.imageRenderer
        self.imgResult.grid(column=0, row=4, sticky=S, columnspan=4)

    def __value_setting(self, i):
        self.__text_var_setter(i)
        self.__id_image_var_setter(i)
        self.__result_image_var_setter(i)

    def __next_update(self):
        self.__save_to_obj(self.__iterator)
        self.__iterator = IOHandler().next_value_iterate(self.__iterator)
        self.__value_setting(self.__iterator)

    def __prev_update(self):
        self.__save_to_obj(self.__iterator)
        self.__iterator = IOHandler().prev_value_iterate(self.__iterator)
        self.__value_setting(self.__iterator)

    def __save_to_obj(self, i=0):
        self.__IO.jsonPersons[i].set_confirmed_id(self.cnfmd_id_str_var.get())
        self.__IO.jsonPersons[i].set_confirmed_results(IOHandler().string_converter(self.cnfmd_results_str_var.get()))
        self.__IO.output_handler()

    def __search_by_cnfmd_id(self, condition):
        for i, obj in enumerate(self.__IO.jsonPersons):
            if condition.get() == (obj.get_confirmed_id()):
                self.__value_setting(i)
