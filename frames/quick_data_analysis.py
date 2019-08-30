""" This is the quick_data_analysis module of Biovarase."""
import tkinter as tk
from calendarium import Calendarium

__author__ = "1966bc aka giuseppe costanzi"
__copyright__ = "Copyleft"
__credits__ = ["hal9000",]
__license__ = "GNU GPL Version 3, 29 June 2007"
__version__ = "4.2"
__maintainer__ = "1966bc"
__email__ = "giuseppecostanzi@gmail.com"
__date__ = "2019-8-30"
__status__ = "Production"



class Widget(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(name='quick_data_analysis')

        self.attributes('-topmost', True)
        self.transient(parent)
        self.resizable(0, 0)
        self.parent = parent
        self.engine = kwargs['engine']
        self.engine.center_me(self)
        self.init_ui()

    def init_ui(self):

        w = self.engine.get_init_ui(self)

        r = 0
        c = 0

        self.analysis_date = Calendarium(self, "Set a date")
        self.analysis_date.get_calendarium(w, r, c)

        self.engine.get_export_cancel(self, self)


    def on_open(self):

        sql = "SELECT date(recived) FROM results WHERE enable= 1 ORDER BY recived DESC LIMIT 1;"

        rs = self.engine.read(False, sql,)

        msg = "Quick Data Analysis last data {0}".format(rs[0])

        self.analysis_date.year.set(int(rs[0][0:4]))
        self.analysis_date.month.set(int(rs[0][5:7]))
        self.analysis_date.day.set(int(rs[0][8:10]))

        self.title(msg)


    def on_export(self, evt=None):

        if self.analysis_date.get_date(self) == False:return

        args = (self.analysis_date.get_date(self),)
        self.engine.get_quick_data_analysis(args)
        self.on_cancel()

    def on_cancel(self, evt=None):
        self.destroy()

