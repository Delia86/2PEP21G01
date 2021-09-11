"""Create Python UI application that will:

retrieve timezones from this link: (50p)
http://worldtimeapi.org/api/timezone
Allow the user to select a timezone and open a new window indicating the time in the selected timezone using this link: (50p)
http://worldtimeapi.org/api/timezone// Detailed description:
all windows must have title (5p)
all modules classes and methods must be documented (10p)
type hints should be used whenever possible (5p)
at least two unittests created for at lest one function (20p)
all timezones are displayed. (30p)
each timezone clicked will open a new window and show time in that timezone (20p)
retrieving time to display is done async or in separate thread or process (10p)
Note: You can choose to pack new Frame or open new window for each displayed time. For new window you can use tkinter.TopLevel(main_window)"""



import tkinter
import time
from functools import partial
import requests
import json
from multiprocessing import Queue



url = f'http://worldtimeapi.org/api/timezone'

main_window=tkinter.Tk()
main_window.title('Timezones')

class TimeZones():
    """Class for creating timezones"""

    def __init__(self, root_window: tkinter.Tk):
        self.root_window = root_window

        self.label=tkinter.Label(self.root_window,text='Text Label')
        self.label.grid(row=0,column=0)
        self.timezone_getter()
        self.get_time()


    def timezone_getter(self,location='Europe'):
        """function which gets all the cities in Europe"""
        response = requests.get(url)
        my_timezone_str = response.text
        my_timezone = json.loads(my_timezone_str)
        self.zone_list = list(filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone)))

    def get_city_time(self,city):
        city_time=requests.get(f'http://worldtimeapi.org/api/timezone/Europe/{city}')
        with open('time','r')as file:
            file.read(city_time)


    def get_time(self):
        print('timeszones are:')
        counter=1
        for city in self.zone_list:
            command = partial(self.get_city_time,city)
            zones = tkinter.Button(self.root_window, text=str(city), command=command)
            zones.grid(row=counter,column=0)
            counter+=1

    def run(self):
        self.root_window.mainloop()



timezones=TimeZones(main_window)
timezones.run()
