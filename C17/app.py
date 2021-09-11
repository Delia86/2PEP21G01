""""Create application with GUI in python that allows user to specify several timezones and will pull show time in UI for each timezone user provides

- documentation and type hints (20p)
- UI for user input of timezones (10p)
- UI for user input of timezones (10p)
- retrieve information from API server (10p)
- use of parallel execution to pull multiple time zones (20p)
- application correctly processes input and returns time (30)
"""

import tkinter
import time
import requests
import json
from multiprocessing import Queue

url = f'http://worldtimeapi.org/api/timezone'

main_window=tkinter.Tk()
main_window.title('Timezones')

class TimeZone():
    """Class for getting timezones"""

    def __init__(self, root_window: tkinter.Tk):
        self.root_window = root_window

        self.label=tkinter.Label(self.root_window,text='Text Label')
        self.label.grid(row=0,column=0)
        self.text_entry=tkinter.Entry(self.root_window)
        self.text_entry.grid(row=1,column=0,columnspan=1)
        self.button1 = tkinter.Button(self.root_window,text='Submit', command=self.insert_timezone)
        self.button1.grid(row=2, column=0)

    def timezone_getter(self,q,location='Paris'):

        response = requests.get(url)
        my_timezone_str = response.text
        my_timezone = json.loads(my_timezone_str)
        zone_list = list(filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone)))
        for zone in zone_list:
            q.put(zone)

    def insert_timezone(self):
        """Allows user to input location"""

        location= self.text_entry.get()
        print('Print something')

    def run(self):
        self.root_window.mainloop()





timezones=TimeZone(main_window)
timezones.run()