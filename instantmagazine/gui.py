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
from utils import *
 
class InstantMagazineApp(tk.Frame):
    def __init__(self, master):
      
        tk.Frame.__init__(self,
                          master,
                          width=520,
                          height=400)
      
        self.master.title('InstantMagazine: easy html5 magazine generator ')
 
        self.pack_propagate(0)
 
        self.pack()
 
        self.destinationFolderVar = tk.StringVar()
        self.destinationFolderInput = tk.Entry(self,
                                  textvariable=self.destinationFolderVar,justify='center',font = "Helvetica 24 bold")
        self.destinationFolderVar.set('january_edition')
 
        self.go_button = tk.Button(self,
                                   text='Go',
                                   command=self.processPDF)
								   
        self.browseButton = tk.Button(self, text='Select a PDF file', command=self.openFileAction)						   
        
        self.path = tk.StringVar()
        self.messageWaitLabel = tk.StringVar()
        self.labelPath = tk.Label(self, textvariable=self.path)
        self.folderInputLabel = tk.Label(self, text="Type a name for the destination folder: ")
        self.waitLabel = tk.Label(self, textvariable=self.messageWaitLabel)
        
        
        self.count = tk.IntVar()
        self.skipSharedFolder = tk.Checkbutton(self, text="Only create resource files (skip share viewer files)", variable=self.count)
        self.text = tk.Text(self, state='disabled', width=50, height=8)
     
        self.separator = tk.ttk.Separator(self,orient=HORIZONTAL)
    
      
        self.browseButton.pack(fill=tk.X, side=tk.TOP)
        self.labelPath.pack(fill=tk.X, side=tk.TOP)
        self.text.pack(fill=tk.X, side=tk.TOP)
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.folderInputLabel.pack(fill=tk.X, side=tk.TOP)
        self.waitLabel.pack(fill=tk.X, side=tk.BOTTOM)
        self.destinationFolderInput.pack(fill=tk.X, side=tk.TOP)
        self.separator.pack(fill=tk.X, side=tk.BOTTOM, ipady=8)
        self.skipSharedFolder.pack(fill=tk.X, side=tk.BOTTOM, ipady=8)
       
    def openFileAction(self):
        file = tk.filedialog.askopenfilename(title = "choose your file",filetypes = (("Pdf Files","*.pdf"),("all files","*.*")))
        pdfInfoOutput = check_output("pdfinfo "+file, shell=True)
        self.text.configure(state='normal')
        self.text.insert('end', pdfInfoOutput)
        self.text.configure(state='disabled')
        self.path.set(file)
        
    def processPDF(self):
        self.showWaitMessage()
        if not os.path.exists("dist/viewer/"+self.destinationFolderVar.get()):
            os.makedirs("dist/viewer/"+self.destinationFolderVar.get())
        if self.count.get() == 0:
            sourcePath = os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) + "/library/wowbook/shared"
            destPath =   os.path.abspath(os.path.join(os.path.dirname(__file__),"..")) + "/dist/shared"
            if not os.path.exists(destPath):
                copyFolder(self, sourcePath, destPath)
        check_output("pdftoppm -png -scale-to  1500"+self.path.get()+" dist/viewer/"+self.destinationFolderVar.get()+"/page", shell=True) #1500
        totalPagesNumber = str(getTotalPages(self, "dist/viewer/"+self.destinationFolderVar.get())) 
        replaceTotalNumber(self, "library/viewer/template.html","var totalPages = "+totalPagesNumber+";\n") 
        openBrowserDialog(self)
        self.messageWaitLabel.set("")
	
    def showWaitMessage(self):
        self.messageWaitLabel.set("Exporting PDF to HTML5 flip magazine, this process might take serveral minutes...")
        self.update()
      
    def run(self):
        ''' Run the app '''
        self.mainloop()
 
app = InstantMagazineApp(tk.Tk())
app.run()
