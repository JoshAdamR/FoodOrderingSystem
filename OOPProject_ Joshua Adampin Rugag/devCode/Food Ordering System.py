import _tkinter
import io
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import os

try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "Bambangan.FoodOrderingSys.App.V1.0.0.3"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

except ImportError:
    pass

def databasecreation():
    file = 'Database\MenuDatabase.txt' #Database creation
    f = open(file, 'a')
    f.close()
    sep = ';'
    return file, sep


def sellerwin(logwin): #Create and open seller window to advertise menu

    #DEFINE or SETUPS
    global file, sep

    #Destroy previous window
    try: logwin.destroy()
    except: pass

    #FUNCTIONS    
    def addnewbtn(): #add new menu button function

        #DEFINE or SETUPS
        global file, sep

        #FUNCTIONS
        def confirm(e1, e2): #Confirm to add new item - button function
            global file, sep
            duplicate = 0
            with open(file, "r") as f:
                lines = f.read().split('\n')
            f = open(file, 'a')
            try:
                if str(e1.get()) != '':
                    price = round(float(e2.get()), 2)
                    price = format(price, "0.2f")
                    newdata = e1.get() + sep + price
                    for line in lines:
                        if line == newdata:
                            duplicate=1
                    if duplicate != 1:
                        f.write(newdata)
                        f.write('\n')
                        f.close()
                        addnew_closing()
                        sellwin.destroy()
                        sellerwin(logwin)
                    else:
                        messagebox.showerror(title='Duplicate Item Error', message= 'Item already existed in database', parent=addnew)
                        addnew.lift()
                 
                else:
                    messagebox.showerror(title='Input Error', message= 'Invalid input', parent=addnew)
                    addnew.lift()
            except:
                messagebox.showerror(title='Input Error', message= 'Invalid input', parent=addnew)
                addnew.lift()
        


        

        def addnew_closing(): #This function will be called when the addnew window closes
            addnew.grab_release()
            addnew.destroy()


        def enter(a):
            confirm(eitem, eprice)


        #GUIS or WIDGETS
        addnew = Toplevel(sellwin)
        addnew.title("Add New Item")
        addnew.geometry("380x30")
        addnew.resizable(False, False)
        addnew.configure(background='#ffef82')
        addnew.iconbitmap("food.ico")
        sellwin.eval(f'tk::PlaceWindow {str(addnew)} center')
        addnew.protocol("WM_DELETE_WINDOW", addnew_closing) #when addnew window closes
        addnew.grab_set()

        #Labels
        lblitem = Label(addnew, text="Item")
        lblprice = Label(addnew, text="Price")

        lblitem.grid(row=0, column=0)
        lblprice.grid(row=0, column=2)

        lblitem.configure(background='#ffef82')
        lblprice.configure(background='#ffef82')

        #Entries
        eitem = Entry(addnew)
        eprice = Entry(addnew)

        eitem.grid(row=0, column=1)
        eprice.grid(row=0, column=3)     

        eitem.configure(background='#fff9d1')
        eprice.configure(background='#fff9d1')       
        
        #Buttons
        cnfrmbtn = Button(addnew, text='Confirm', command=lambda: confirm(eitem, eprice))
        cnfrmbtn.configure(background='#fff9d1')
        cnfrmbtn.grid(row=0, column=4)

        #Binds
        addnew.bind("<Return>", enter)

        addnew.mainloop()


    def ed(): #edit menu button function
        
        #DEFINE or SETUPS
        global file, sep
        selected_item = tbl.selection()[0]


        #FUNCTIONS
        def confirm(e1, e2, selected_item): #Confirm to add new item - button function
            duplicate = 0
            with open(file, "r") as f:
                lines = f.readlines()
            try:
                if str(e1.get()) != '':
                    price = round(float(e2.get()), 2)
                    price = format(price, "0.2f")
                    newdata = e1.get() + sep + price + '\n'
                    for line in lines:
                        if line == newdata:
                            duplicate=1
                    if duplicate != 1:
                        lines[int(selected_item)-1] = newdata
                        with open(file, 'w') as f:
                            f.writelines(lines)
                        edwin_closing()
                        sellwin.destroy()
                        sellerwin(logwin)
                    else:
                        messagebox.showerror(title='Duplicate Item Error', message= 'Item already existed in database', parent=edwin)
                        edwin.lift()
                 
                else:
                    messagebox.showerror(title='Input Error', message= 'Invalid input', parent=edwin)
                    edwin.lift()
            except:
                messagebox.showerror(title='Input Error', message= 'Invalid input', parent=edwin)
                edwin.lift()
        

        def edwin_closing(): #This function will be called when the edwin window closes
            edwin.grab_release()
            edwin.destroy()


        def enter(a):
            confirm(eitem, eprice, selected_item)


        #GUIS or WIDGETS
        edwin = Toplevel(sellwin)
        edwin.title("Edit Item")
        edwin.geometry("380x30")
        edwin.resizable(False, False)
        edwin.configure(background='#ffef82')
        edwin.iconbitmap("food.ico")
        sellwin.eval(f'tk::PlaceWindow {str(edwin)} center')
        edwin.protocol("WM_DELETE_WINDOW", edwin_closing) #when edwin window closes
        edwin.grab_set()

        #Labels
        lblitem = Label(edwin, text="Item")
        lblprice = Label(edwin, text="Price")

        lblitem.grid(row=0, column=0)
        lblprice.grid(row=0, column=2)

        lblitem.configure(background='#ffef82')
        lblprice.configure(background='#ffef82')

        #Entries
        eitem = Entry(edwin)
        eprice = Entry(edwin)

        eitem.grid(row=0, column=1)
        eprice.grid(row=0, column=3)     

        eitem.configure(background='#fff9d1')
        eprice.configure(background='#fff9d1')       
        
        #Buttons
        cnfrmbtn = Button(edwin, text='Confirm', command=lambda: confirm(eitem, eprice, selected_item))
        cnfrmbtn.configure(background='#fff9d1')
        cnfrmbtn.grid(row=0, column=4)

        #Binds
        edwin.bind("<Return>", enter)

        edwin.mainloop()

    
    def backs(): #Return btn function
        sellwin.destroy()
        login()


    def rmall(): #remove all btn function
        global file
        f = open(file, 'w')
        f.write('')
        f.close()
        sellwin.destroy()
        sellerwin(logwin)


    def rm(): #remove selected btn function
        global file, sep
        selected_item = tbl.selection()[0]
        delete = tbl.set(selected_item, '#2') + sep + tbl.set(selected_item, '#3')

        with open(file, "r") as f:
            lines = f.readlines()
        with open(file, "w") as f:
            for line in lines:
                if line.strip("\n") != delete:
                    f.write(line)

        sellwin.destroy()            
        sellerwin(logwin)

    def updatesellwin(): #function that update table with click button action
        try:
            f = open(file, 'r')
            line = f.read().split('\n')
            f.close()
        except io.UnsupportedOperation: pass
        cnt = 0
        try:
            for i in range(len(line)):
                data = line[i].split(sep)
                cnt += 1
                try:
                    tbl.insert(parent='', index='end', iid=cnt, text='', values=(cnt, data[0], data[1]))
                except(TclError, IndexError):
                    cnt -= 1
                    pass
        except UnboundLocalError: pass

    def disbtn(a):
        try:
            selected_item = tbl.selection()[0]
            rmbtn['state'] = NORMAL
            edbtn['state'] = NORMAL
        except IndexError:
            rmbtn['state'] = DISABLED
            edbtn['state'] = DISABLED

    #GUI & WIDGETS
    sellwin = Tk()
    sellwin.title("Edit Menu")
    sellwin.geometry("325x325")
    sellwin.resizable(False, False)
    #sellwin.overrideredirect(1)
    sellwin.iconbitmap("food.ico")
    sellwin.eval('tk::PlaceWindow . c   Senter')
    sellwin.configure(background='#ffef82')

    
    #Frames
    empty_frame = Frame(sellwin)
    tbl_frame = Frame(sellwin)
    btn_frame = Frame(sellwin)

    empty_frame.grid(row=1, column=0, columnspan=1)
    tbl_frame.grid(row=1, column=1, columnspan=3)
    btn_frame.grid(row=2, column=1, columnspan=3)

    empty_frame.configure(background='#ffef82')
    tbl_frame.configure(background='#ffef82')
    btn_frame.configure(background='#ffef82')

    style = ttk.Style(sellwin)
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="#e6e0b3", foreground="black")
    style.configure("Treeview", background="#faf3c5", foreground="black")

    #Table scroll
    tbl_scrolly = Scrollbar(tbl_frame)
    tbl_scrolly.pack(side=RIGHT, fill=Y)

    #Menu list table
    tbl = ttk.Treeview(tbl_frame, yscrollcommand=tbl_scrolly.set, selectmode='browse')
    tbl['columns'] = ("Id", "Items", "Price")
    tbl.column("#0", width=0, minwidth=0)
    tbl.column("Id", anchor=W, width=50)
    tbl.column("Items", anchor=W, width=120)
    tbl.column("Price", anchor=W, width=120)

    tbl.heading("#0", text="Id", anchor=W)
    tbl.heading("Id", text="Id.", anchor=W)
    tbl.heading("Items", text="Items", anchor=W)
    tbl.heading("Price", text="RM", anchor=W)

    tbl.pack()
    tbl_scrolly.config(command=tbl.yview)

    #Labels
    lbl_empty = Label(empty_frame)
    lbl_empty.grid()
    lbl_empty.configure(background='#ffef82')
    lbltitle = Label(sellwin, text='Menu List')
    lbltitle.configure(background='#ffef82')
    lbltitle.grid(row=0, column=1, sticky=W)

    #Buttons
    btn_back = Button(btn_frame, text="Return", command=backs)
    addbtn = Button(btn_frame, text="Add", command=addnewbtn)
    rmbtn = Button(btn_frame, text="Delete", command=rm)
    rmabtn = Button(btn_frame, text="Delete All", command=rmall)
    rmbtn['state'] = DISABLED
    edbtn = Button(btn_frame, text="Edit", command=ed)
    edbtn['state'] = DISABLED

    btn_back.grid(row=1,column =1, sticky=SW)
    addbtn.grid(row=0, column=1, ipadx=20, ipady=10)
    rmbtn.grid(row=0, column=2, ipadx=15, ipady=10)
    rmabtn.grid(row=0, column=3, ipadx=15, ipady=10)
    edbtn.grid(row=0, column=4, ipadx=20, ipady=10)
    
    btn_back.configure(background='#faf3c5')
    addbtn.configure(background='#faf3c5')
    rmbtn.configure(background='#faf3c5')
    rmabtn.configure(background='#faf3c5')
    edbtn.configure(background='#faf3c5')

    #Binds
    sellwin.bind("<Button>", disbtn)

    #Print items on table from database
    updatesellwin()


    sellwin.mainloop()


def buyerwin(logwin): #create and open buyer window
    #DEFINE or SETUPS
    global file, sep
    qtt = []

    #Destroy previous window
    logwin.destroy() 

    #FUNCTIONS
    def backb(): #return btn function
        buywin.destroy()
        login()


    def addbtn(): #add to cart btn function
        global file, sep
        selected_item = menutbl.selection()
        for i in selected_item:
            with open(file, "r") as f:
                lines = f.read().split('\n')
                data = lines[int(i) - 1].split(sep)
                qtt[int(i)-1] += 1
                try:
                    carttbl.insert(parent='', index='end', iid=i, text='', values=(int(i), data[0], data[1], qtt[int(i)-1]))
                except _tkinter.TclError:
                    carttbl.set(i, '#4', qtt[int(i) - 1])
        currlblnum('<Button>')  
        updatewin()


    def plsbtn(): #'+' btn funtion
        global file
        selected_item = carttbl.selection()
        for i in selected_item:
            qtt[int(i) - 1] += 1
            carttbl.set(i, '#4', qtt[int(i) - 1])
        currlblnum('<Button>')    
        updatewin()
        

    def mnsbtn(): #'-' btn function
        global file
        selected_item = carttbl.selection()
        for i in selected_item:
            qtt[int(i) - 1] -= 1
            carttbl.set(i, '#4', qtt[int(i) - 1])
            if qtt[int(i) - 1] <= 0:
                carttbl.delete(i)
                lblnum.delete(0, END)
        currlblnum('<Button>')
        updatewin()


    def currlblnum(a): #A function to check the current selected item's quantity
        try:
            curitem = carttbl.focus()
            lblnum.delete(0, END)
            lblnum.insert(0, qtt[int(curitem) - 1])
        except ValueError:
            pass


    def changeqtt(a): #A function to change the quantity with type input 
        selected_item = carttbl.selection()
        for i in selected_item:
            try: qtt[int(i) - 1] = int(lblnum.get())
            except: messagebox.showerror(title='Input Error', message= "Invalid input")
            carttbl.set(i, '#4', qtt[int(i) - 1])
            if qtt[int(i) - 1] <= 0:
                carttbl.delete(i)
                lblnum.delete(0, END)
        updatewin()


    def get_all_children(tree, item=""): #A function to find the total list in table
        children = tree.get_children(item)
        for child in children:
            children += get_all_children(tree, child)
        return children


    def totalpay(children): #Function to calculate the total cost
        totale.config(state=NORMAL)
        total = 0
        for i in children:
            try:
                getprice = float(carttbl.set(i, '#3'))
                getqtt = float(carttbl.set(i, '#4'))
                total += (getprice * getqtt)
            except _tkinter.TclError:
                pass
        total = round(float(total), 2)
        total = format(total, "0.2f")
        totale.delete(0, END)
        totale.insert(0, total)
        totale.config(state=DISABLED)


    def updatewin(): #function that update total value with click button action
        buywin.bind('<Button-1>', totalpay(get_all_children(carttbl)))

    def yourpurchase(children, carttbl): #return items bought as itemlist
        itemlist = []
        for i in children:
            try:
                getitems = carttbl.set(i, '#2')
                getprice = carttbl.set(i, '#3')
                getqtt = carttbl.set(i, '#4')
            except _tkinter.TclError:
                pass
            itemlist.append(str(getitems) + "\t\tRM " + str(getprice) + '\tx' + str(getqtt))
        return itemlist

    def paybtn(): #Go to item window and display itemlist
        paywin = Tk()
        paywin.title("Receipt")
        paywin.eval('tk::PlaceWindow . center')
        #paywin.overrideredirect(1)
        paywin.configure(background='#fff9d4')
        lblthanks = Label(paywin,text="Thank You For Purchasing!")
        lblthanks.grid(row=0, columnspan=2, sticky=W)
        lblthanks.configure(background='#fff9d4')
        lblyil = Label(paywin,text="Your Item List:")
        lblyil.grid(row=1, columnspan=2, sticky=W)
        lblyil.configure(background='#fff9d4')
        itemlist = yourpurchase(get_all_children(carttbl), carttbl)
        i = 0
        try:
            for i in range(len(itemlist)):
                
                lbllist = Label(paywin, text=itemlist[i])
                lbllist.grid(row=i+2, columnspan=2, sticky=W)
                lbllist.configure(background='#fff9d4')

            lblttl = Label(paywin,text="Total: RM " + totale.get())
            lblttl.grid(row=i+3, columnspan=2, sticky=NE)
            lblttl.configure(background='#fff9d4')
        except (tkinter.TclError, UnboundLocalError): pass
        buywin.destroy()
        def paywin_closing():
            paywin.destroy()
            login()
        mm = Button(paywin, text='Main Menu', command= paywin_closing)
        mm.grid(row=i+4, rowspan=2, sticky=SE)
        qt = Button(paywin, text='Exit', command= paywin.destroy)
        qt.grid(row=i+4, column=1, rowspan=2, sticky=SW)
        mm.configure(background='#fffce8')
        qt.configure(background='#fffce8')
        paywin.protocol("WM_DELETE_WINDOW", paywin_closing) #when paywin window closes


    def updatemenu():
        f = open(file, 'r')
        line = f.read().split('\n')
        f.close()
        cnt = 0
        for i in range(len(line)):
            data = line[i].split(sep)
            try:
                cnt += 1
                menutbl.insert(parent='', index='end', iid=cnt, text='', values=(cnt, data[0], data[1]))
            except(TclError, IndexError):
                cnt -= 1

        with open(file, "r") as f:
            lines = f.read().split('\n')
            for line in range(len(lines) - 1):
                qtt.append(0)


    #GUI & WIDGETS
    buywin = Tk()
    buywin.title("Menu")
    buywin.geometry("630x300")
    buywin.resizable(False, False)
    buywin.eval('tk::PlaceWindow . center')
    buywin.configure(background='#fff9d1')
    buywin.iconbitmap("food.ico")
    #buywin.overrideredirect(1)
    
    #Frames
    empty_frame = Frame(buywin)
    menutbl_frame = Frame(buywin)
    carttbl_frame = Frame(buywin)
    rm_frame = Frame(buywin)
    buy_frame = Frame(buywin)

    empty_frame.grid(row=1, column=0, columnspan=1)
    menutbl_frame.grid(row=1, column=1, columnspan=3)
    carttbl_frame.grid(row=1, column=4, columnspan=3)
    rm_frame.grid(row=2, column=5, sticky=W)
    buy_frame.grid(row=3, column=5, columnspan=2, sticky=W)

    empty_frame.configure(background='#fff9d1')
    menutbl_frame.configure(background='#fff9d1')
    carttbl_frame.configure(background='#fff9d1')
    rm_frame.configure(background='#fff9d1')
    buy_frame.configure(background='#fff9d1')

    #Buttons
    btn_back = Button(buywin, text="Return", command=backb)
    addtocartbtn = Button(buywin, text='Add to Cart', command=addbtn)
    plusbtn = Button(rm_frame, text='+', command=plsbtn)
    minusbtn = Button(rm_frame, text='-', command=mnsbtn)
    buybtn = Button(buy_frame, text='Pay', command=paybtn)

    btn_back.grid(row=2,column =1, sticky=W)
    addtocartbtn.grid(row=2, column=3, sticky=E)
    plusbtn.grid(row=0, column=1, ipadx=5, stick=W)
    minusbtn.grid(row=0, column=3, ipadx=5, stick=E)
    buybtn.grid(row=0, column=2, ipadx=10)

    btn_back.configure(background='#e6e0b3')
    addtocartbtn.configure(background='#e6e0b3')
    plusbtn.configure(background='#e6e0b3')
    minusbtn.configure(background='#e6e0b3')
    buybtn.configure(background='#e6e0b3')

    #Labels
    menulbl = Label(buywin, text='Menu')
    cartlbl = Label(buywin, text='Cart')
    lbl_empty = Label(empty_frame)
    rmlbl = Label(rm_frame, text='Quantity')
    lbltotal = Label(buy_frame, text='Total(RM): ')

    menulbl.grid(row=0, column=1, sticky=W)
    cartlbl.grid(row=0, column=4, sticky=W)
    lbl_empty.grid()
    rmlbl.grid(row=0, column=0, sticky=E)
    lbltotal.grid(row=0, column=0)

    menulbl.configure(background='#fff9d1')
    cartlbl.configure(background='#fff9d1')
    lbl_empty.configure(background='#fff9d1')
    rmlbl.configure(background='#fff9d1')
    lbltotal.configure(background='#fff9d1')

    #Entries
    lblnum = Entry(rm_frame, width=5)
    totale = Entry(buy_frame, width=10)
    totale.insert(0, '0.00')
    totale.config(state=DISABLED, disabledbackground='#e6e0b3', disabledforeground='black')

    lblnum.grid(row=0, column=2)
    totale.grid(row=0, column=1)

    #Table scroll
    menutbl_scrolly = Scrollbar(menutbl_frame)
    carttbl_scrolly = Scrollbar(carttbl_frame)

    menutbl_scrolly.pack(side=RIGHT, fill=Y)
    carttbl_scrolly.pack(side=RIGHT, fill=Y)
    
    #Table heading
    style = ttk.Style(buywin)
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="#e6e0b3", foreground="black")
    style.configure("Treeview", background="#faf3c5", foreground="black")

    #Menu table
    menutbl = ttk.Treeview(menutbl_frame, yscrollcommand=menutbl_scrolly.set)
    menutbl['columns'] = ("Id", "Items", "Price")
    menutbl.column("#0", width=0, minwidth=0)
    menutbl.column("Id", anchor=W, width=50)
    menutbl.column("Items", anchor=W, width=120)
    menutbl.column("Price", anchor=W, width=120)

    menutbl.heading("#0", text="Id", anchor=W)
    menutbl.heading("Id", text="Id.", anchor=W)
    menutbl.heading("Items", text="Items", anchor=W)
    menutbl.heading("Price", text="RM", anchor=W)

    menutbl.pack()
    menutbl_scrolly.config(command=menutbl.yview)

    #Cart table
    carttbl = ttk.Treeview(carttbl_frame, yscrollcommand=carttbl_scrolly.set, selectmode='browse')
    carttbl['columns'] = ("Id", "Items", "Price", "Quantity")
    carttbl.column("#0", width=0, minwidth=0)
    carttbl.column("Id", anchor=W, width=50)
    carttbl.column("Items", anchor=W, width=120)
    carttbl.column("Price", anchor=W, width=60)
    carttbl.column("Quantity", anchor=W, width=60)

    carttbl.heading("#0", text="Id", anchor=W)
    carttbl.heading("Id", text="Id.", anchor=W)
    carttbl.heading("Items", text="Items", anchor=W)
    carttbl.heading("Price", text="RM", anchor=W)
    carttbl.heading("Quantity", text="Quantity", anchor=W)

    carttbl.pack()
    carttbl_scrolly.config(command=carttbl.yview)

    #Binds
    buywin.bind('<Button-1>', currlblnum)        
    buywin.bind('<Return>', changeqtt)
    buywin.bind('<Button>', changeqtt)

    #Display items from database to menu
    updatemenu()

    buywin.mainloop()


def login(): #Login window  

    #FUNCTIONS
    def admlogwindow(logwin):

        #SETUPS
        bullet = "\u2022"

        #FUNCTIONS
        def admlogwin_closing():
            admlogwin.grab_release()
            admlogwin.destroy()
            logwin.lift()


        def admlogin(eid, epass, logwin):
            global ID, PASS
            idn = eid.get()
            if idn != '':
                idn = idn.strip()
            idname = idn
            passw = epass.get()
            if (idname == ID) and (passw == PASS):
                sellerwin(logwin)
            elif (idname == ID):
                messagebox.showerror(title='Access Denied', message= 'Wrong Password', parent=admlogwin)
                eid.delete(0,END)
                epass.delete(0,END)
                admlogwin.lift()
            else:
                messagebox.showerror(title='Access Denied', message= "ID doesn't exist", parent=admlogwin)
                eid.delete(0,END)
                epass.delete(0,END)
                admlogwin.lift()


        def enter(a):
            admlogin(eid, epass, logwin)


        #GUIS & WIDGETS
        admlogwin = Toplevel(logwin)
        admlogwin.title("Admin Login")
        admlogwin.geometry("380x30")
        admlogwin.resizable(False, False)
        admlogwin.configure(background='#ffef82')
        logwin.eval(f'tk::PlaceWindow {str(admlogwin)} center')
        admlogwin.iconbitmap("food.ico")
        admlogwin.protocol("WM_DELETE_WINDOW", admlogwin_closing) #when admlogwin window closes
        admlogwin.grab_set()

        #Labels
        lblid = Label(admlogwin, text="ID: ")
        lblpass = Label(admlogwin, text="Password: ")

        lblid.grid(row=0, column=0)
        lblpass.grid(row=0, column=2)

        lblid.configure(background='#ffef82')
        lblpass.configure(background='#ffef82')

        #Entries
        eid = Entry(admlogwin)
        epass = Entry(admlogwin, show = bullet)

        eid.grid(row=0, column=1)
        epass.grid(row=0, column=3)      

        eid.configure(background='#fff9d1')
        epass.configure(background='#fff9d1')   
        
        #Buttons
        logbtn = Button(admlogwin, text='Login', command=lambda: admlogin(eid, epass, logwin))
        logbtn.configure(background='#fff9d1') 
        logbtn.grid(row=0, column=4)
        

        admlogwin.bind("<Return>", enter)

        admlogwin.mainloop()


    #GUI & WIDGETS
    logwin = Tk()
    logwin.title("Login")
    logwin.geometry("220x200")
    logwin.resizable(False, False)
    logwin.eval('tk::PlaceWindow . center')
    logwin.configure(background='#fae05c')
    #logwin.overrideredirect(1)
    logwin.iconbitmap("food.ico")
    lbltitle = Label(logwin,text='BAMBANGAN CAFE')
    lbltitle.grid(row=0, ipady=14)
    lbltitle.configure(background='#fae05c')
    
    #Buttons
    buyerbtn = Button(logwin, text='ORDER', command=lambda: buyerwin(logwin))
    sellerbtn = Button(logwin, text='EDIT MENU', command=lambda: admlogwindow(logwin))
    qbtn = Button(logwin, text='EXIT', command= logwin.destroy)
    
    buyerbtn.grid(row=1, ipadx=85, ipady=12)
    sellerbtn.grid(row=2, ipadx=75, ipady=12)
    qbtn.grid(row=3, ipadx=94, ipady=12)

    buyerbtn.configure(background='#e6e0b3')
    sellerbtn.configure(background='#e6e0b3')
    qbtn.configure(background='#ffeb7a')

    logwin.mainloop()


#Program starts here

#ID and Password for administrative log in
ID = "__admin__"
PASS = "__admin__"

file, sep = databasecreation() #file creation

login()
