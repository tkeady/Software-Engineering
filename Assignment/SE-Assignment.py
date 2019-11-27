import tkinter as tk
import os, sys
import requests
import json
from urllib.request import urlopen

city = skye
url = urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&appid=2e535070ac9219e3c58f19ac7227c197&q='.format(city)).read()
url = json.loads(url)
data = url['weather']
data = data[0]

weather = data['main']

root = tk.Tk()
weatherpic = tk.PhotoImage(file=os.path.join(sys.path[0], 'insert-picture-here.gif'))

root.title("F1 Updater")
root.resizable(width=False, height=False)
root.geometry("1200x800+200+100")
root.configure(bg="#4d4d4d")

top_left_frame = tk.Frame(root, highlightbackground="white", highlightcolor="white", highlightthickness=1, padx=5, bg="black")
location_frame = tk.Frame(top_left_frame, bg="black")
date_frame = tk.Frame(top_left_frame, pady=10, bg="black")
time_frame = tk.Frame(top_left_frame, bg="black")
top_right_frame = tk.Frame(root, highlightbackground="white", highlightcolor="white", highlightthickness=1, padx=0, bg="black")
overview_frame = tk.Frame(top_right_frame, bg="black")
photo_frame = tk.Frame(top_right_frame, bg="black")
bottom_frame = tk.Frame(root, highlightbackground="white", highlightcolor="white", highlightthickness=1, padx=5, bg="black")

root.rowconfigure([1,3,4,5,6,7,8], weight=1)
root.rowconfigure([0,2,8], minsize=8)
root.columnconfigure([1,3], weight=1)
root.columnconfigure([0,2,4], minsize=6)

top_right_frame.grid(row=1, column=3, sticky='nsew')
top_left_frame.grid(row=1, column=1, sticky='nsew')
bottom_frame.grid(row=3, column=1, columnspan=3, rowspan=6, sticky='nsew')

tk.Label(top_right_frame, text="Weather Forecast", bg="black", fg="red", font=('Helvetica', 22, 'bold'), pady=15).pack()
tk.Label(top_left_frame, text="Next Race", bg="black", fg="red", font=('Helvetica', 22, 'bold'), pady=15).pack()
tk.Label(location_frame, text="Location: ", bg="black", fg="red", font=('Helvetica', 18, 'bold')).pack(side='left')
tk.Label(location_frame, text="Enter Location Here", bg="black", fg="white", font=('Helvetica', 14, 'bold')).pack(side='left')
tk.Label(date_frame, text="Date: ", bg="black", fg="red", font=('Helvetica', 18, 'bold')).pack(side='left')
tk.Label(date_frame, text="Enter Date Here", bg="black", fg="white", font=('Helvetica', 14, 'bold')).pack(side='left')
tk.Label(time_frame, text="Time: ", bg="black", fg="red", font=('Helvetica', 18, 'bold')).pack(side='left')
tk.Label(time_frame, text="Enter Time Here", bg="black", fg="white", font=('Helvetica', 14, 'bold')).pack(side='left')
tk.Label(overview_frame, text="Overview: ", bg="black", fg="red", font=('Helvetica', 18, 'bold')).pack(side='left')
tk.Label(overview_frame, text=weather, bg="black", fg="white", font=('Helvetica', 14, 'bold')).pack(side='left')
tk.Label(photo_frame, image=weatherpic).pack()

location_frame.pack(fill='x')
date_frame.pack(fill='x')
time_frame.pack(fill='x')
overview_frame.pack(fill='x')
photo_frame.pack()

root.mainloop()
