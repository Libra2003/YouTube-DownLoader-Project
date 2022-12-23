from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
link = simpledialog.askstring(title="YouTube Downloader", prompt="Video Link: ")

yt = YouTube(link)

print("This Screen will automatically close when the downloading is complete")
print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('/Users/pak/Desktop/Youtube Download')

