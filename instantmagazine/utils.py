from subprocess import check_output
import tkinter as tk
import os, os.path
import webbrowser
import shutil, errno
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import HORIZONTAL
from tempfile import mkstemp
from shutil import move
from os import remove, close
    
def getTotalPages(self, directory):
    list_dir = []
    list_dir = os.listdir(directory)
    count = 0
    for file in list_dir:
        if file.endswith(".png"): # eg: '.txt'
            count += 1
    return count    
          
def copyFolder(self, src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise

def replaceTotalNumber(self, file_path, value):
    line_number = 63
    fh_r = open(file_path)
    fh, abs_path = mkstemp()
    fh_w = open(abs_path, 'w')

    for i, line in enumerate(fh_r):
        if i == line_number - 1:
            fh_w.write(value + line)
        else:
            fh_w.write(line)

    fh_r.close()
    close(fh)
    fh_w.close()

    move(abs_path, "dist/viewer/"+self.destinationFolderVar.get()+"/index.html")        
    
def openBrowserDialog(self):
    result = messagebox.askokcancel("Success! ", "PDF file has been successfully exported to html5, do you want to see the result in a browser?")
    if result is True:
        browserLocalUrl = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) + "/dist/viewer/"+self.destinationFolderVar.get()+"/index.html"
        webbrowser.open_new(browserLocalUrl)
    else:
        print ("User clicked Cancel")
                  
 