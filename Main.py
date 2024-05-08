from tkinter import ttk, messagebox
import tkinter as tk
from PIL import ImageTk, Image
import pyodbc

def VGanado():
    global fondo
    #####################
    fondo = tk.Frame(VPrincipal, bg='light grey')
    fondo.place(relheight=1, relwidth=1)
    ##########################################
    FrameHead = tk.Frame(fondo, bg='green3')
    FrameHead.place(x=0, y=0, relwidth=1, height=60)
    FPL = tk.Label(FrameHead, text='Ganado de  la Granja Ucundinamarca', font=('Comic Sans MS', 25), bg='green3', fg='white')
    FPL.place(x=20, y=20)
    ######################
    Banner = Image.open('imagenes/banner_ganado.png')
    Banner = Banner.resize((1400,500))
    Banner = ImageTk.PhotoImage(Banner)
    FrameRe = tk.Frame(fondo)
    FrameRe.place(y=60,height=300,relwidth=1)
    FrameReL = tk.Label(FrameRe, image=Banner)
    FrameReL.place(relheight=1,relwidth=1)
    ######################
    FrameEs = tk.Frame(fondo,bg='light grey')
    FrameEs.place(relwidth=1,height=500,y=360)

    Vaca = Image.open('imagenes/vaca.png')
    Vaca = Vaca.resize((100,100))
    Vaca = ImageTk.PhotoImage(Vaca)
    Esp1L = tk.Frame(FrameEs,bg='azure')
    Esp1L.place(x=20,y=20,relwidth=.45,height=100)
    EsvL = tk.Label(Esp1L,text='Bovinos', font=('Comic Sans MS', 40),bg='azure')
    EsvL.place(relx=.3,y=20)
    Esv = tk.Label(Esp1L, image=Vaca,bg='azure')
    Esv.place(relx=.85,y=0,relheight=1,width=100)
    Esp1L.bind("<Button-1>", VGV)
    EsvL.bind("<Button-1>", VGV)
    Esv.bind("<Button-1>", VGV)

    Cerdo = Image.open('imagenes/cerdo.png')
    Cerdo = Cerdo.resize((100,100))
    Cerdo = ImageTk.PhotoImage(Cerdo)
    Esp2L = tk.Frame(FrameEs,bg='azure')
    Esp2L.place(x=20,y=200,relwidth=.45,height=100)
    EscL = tk.Label(Esp2L,text='Porcinos', font=('Comic Sans MS', 40),bg='azure')
    EscL.place(relx=.3,y=20)
    Esc = tk.Label(Esp2L, image=Cerdo,bg='azure')
    Esc.place(relx=.85,y=0,relheight=1,width=100)
    Esp2L.bind("<Button-1>", VGC)
    EscL.bind("<Button-1>", VGC)
    Esc.bind("<Button-1>", VGC)
    
    Cabra = Image.open('imagenes/cabra.png')
    Cabra = Cabra.resize((50,100))
    Cabra = ImageTk.PhotoImage(Cabra)
    Esp3L = tk.Frame(FrameEs,bg='azure')
    Esp3L.place(relx=.5,y=200,relwidth=.45,height=100)
    EscaL = tk.Label(Esp3L,text='Caprinos', font=('Comic Sans MS', 40),bg='azure')
    EscaL.place(relx=.3,y=20)
    Esca = tk.Label(Esp3L, image=Cabra,bg='azure')
    Esca.place(relx=.85,y=0,relheight=1,width=100)
    Esp3L.bind("<Button-1>", VGCa)
    EscaL.bind("<Button-1>", VGCa)
    Esca.bind("<Button-1>", VGCa)

    Gall = Image.open('imagenes/gallina.png')
    Gall = Gall.resize((100,100))
    Gall = ImageTk.PhotoImage(Gall)
    Esp5L = tk.Frame(FrameEs,bg='azure')
    Esp5L.place(relx=.5,y=20,relwidth=.45,height=100)
    EsgL = tk.Label(Esp5L,text='Avicultura', font=('Comic Sans MS', 40),bg='azure')
    EsgL.place(relx=.3,y=20)
    Esg = tk.Label(Esp5L, image=Gall,bg='azure')
    Esg.place(relx=.85,y=0,relheight=1,width=100)
    Esp5L.bind("<Button-1>", VGG)
    EsgL.bind("<Button-1>", VGG)
    Esg.bind("<Button-1>", VGG)

    B_Atras = tk.Button(fondo, text='Atras',bg='green3',command=AtrasG)
    B_Atras.place(y=680,x=30,width=50,height=25)

    VPrincipal.mainloop()
##############################
def VGV(event):
    def limpiar_campos():
            global END
            InEdad.delete(0, tk.END)
            CoRaza.delete(0, tk.END)
            InPeso.delete(0, tk.END)
            InNum.delete(0, tk.END)
    
    def Botones():
        with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                s=0
                z=0
                c=0
                d=0
                a=0
                for row in datos:
                    if row[5] == 'Vaca':
                            if row[0]=='Holstein':
                                s=s+1
                            if row[0]=='Gyr': 
                                z=z+1
                            if row[0]=='Jersey':
                                c=c+1
                            if row[0]=='Normando':
                                d=d+1
                            if row[0]=='Pardo suizo':
                                a=a+1
                if s>0:
                    F1 = tk.Button(FrameRaza,text='Holstein',bg='azure',font=('Comic Sans MS', 15))
                    F1.place(rely=.03,x=50,relwidth=.8,height=80)
                    F1.bind("<Button-1>", MostrarV0)
                if z>0: 
                    F2 = tk.Button(FrameRaza,text='Gyr',font=('Comic Sans MS', 15),bg='azure')
                    F2.place(rely=.23,x=50,relwidth=.8,height=80)
                    F2.bind("<Button-1>", MostrarV1)
                if c>0:
                    F3 = tk.Button(FrameRaza,text='Jersey',font=('Comic Sans MS', 15),bg='azure')
                    F3.place(rely=.43,x=50,relwidth=.8,height=80)
                    F3.bind("<Button-1>", MostrarV2)
                if d>0:
                    F4 = tk.Button(FrameRaza,text='Normando',font=('Comic Sans MS', 15),bg='azure')
                    F4.place(rely=.63,x=50,relwidth=.8,height=80)
                    F4.bind("<Button-1>", MostrarV3)
                if a>0:
                    F5 = tk.Button(FrameRaza,text='Pardo suizo',font=('Comic Sans MS', 15),bg='azure')
                    F5.place(rely=.83,x=50,relwidth=.8,height=80)
                    F5.bind("<Button-1>", MostrarV4)
    
    def AnadirV(): 
        IEdad = int(InEdad.get())
        IPeso = int(InPeso.get())
        IOreja = InNum.get()
        if IEdad>18:
            Rendimiento = (IPeso/IEdad)*20000
        else:
            Rendimiento=0

        if CoRaza.current() == 0:
            CRaza = 'Holstein'
        if CoRaza.current() == 1:
            CRaza = 'Gyr'
        if CoRaza.current() == 2:
            CRaza = 'Jersey'
        if CoRaza.current() == 3:
            CRaza = 'Normando'
        if CoRaza.current() == 4:
            CRaza = 'Pardo suizo'
        else:
            print(Rendimiento)
        if CRaza and IEdad and IPeso and IOreja:
            try:
                with cnn.cursor() as cur:
                    sql = '''INSERT INTO GanadoV (Edad, Raza, Peso, NOreja, Produccion,Especie) 
                            VALUES (?, ?, ?, ?, ?,?)'''
                    cur.execute(sql, (IEdad, CRaza, IPeso, IOreja, Rendimiento, 'Vaca'))
                    cnn.commit()
                    messagebox.showinfo("Éxito", "Cultivo agregado exitosamente")
                    limpiar_campos()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el Cultivo: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")
        Botones()
    def MostrarV0(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Vaca':
                            if row[0]=='Holstein':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay ganado de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los Cultivos: {str(e)}")
    def MostrarV1(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Vaca':
                            if row[0]=='Gyr':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                        messagebox.showerror("advertercia",f"no hay ganado de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los Cultivos: {str(e)}")
    def MostrarV2(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Vaca':
                            if row[0]=='Jersey':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                        messagebox.showerror("advertercia",f"no hay ganado de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los Cultivos: {str(e)}")
    def MostrarV3(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Vaca':
                            if row[0]=='Normando':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                        messagebox.showerror("advertercia",f"no hay ganado de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los Cultivos: {str(e)}")
    def MostrarV4(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c = 0
                for row in datos:
                    if row[5] == 'Vaca':
                            if row[0]=='Pardo suizo':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                        messagebox.showerror("advertercia",f"no hay ganado de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los Cultivos: {str(e)}")
    
    global FondoV
    fondo.destroy()
    ###############
    FondoV = tk.Frame(VPrincipal)
    FondoV.place(relheight=1,relwidth=1)
    ###################################
    FrameAn = tk.Frame(FondoV,bg='green3')
    FrameAn.place(relwidth=1,height=200)

    LRaza = tk.Label(FrameAn,text='Raza:',bg='green3',font=('Comic Sans MS', 25))
    LRaza.place(relx=.1,rely=.3)
    CoRaza = ttk.Combobox(FrameAn, values=['Holstein','Gyr','Jersey','Normando','Pardo suizo'],font=('Comic Sans MS', 25))
    CoRaza.place(relx=.1,rely=.5,width=200)

    LEdad = tk.Label(FrameAn, text='Edad:(meses)', bg='green3',font=('Comic Sans MS', 25))
    LEdad.place(relx=.3,rely=.3)
    InEdad = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InEdad.place(relx=.3,rely=.5,width=100)

    LPeso = tk.Label(FrameAn, text='Peso:(Kilos)', bg='green3',font=('Comic Sans MS', 25))
    LPeso.place(relx=.5,rely=.3)
    InPeso = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InPeso.place(relx=.5,rely=.5,width=100)

    LNum = tk.Label(FrameAn, text='Numero Oreja:', bg='green3',font=('Comic Sans MS', 25))
    LNum.place(relx=.7,rely=.3)
    InNum = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InNum.place(relx=.7,rely=.5,width=200)
    
    BtnA = tk.Button(FrameAn, text='Agregar',font=('Comic Sans MS', 15),bg='azure',command=AnadirV)
    BtnA.place(relx=.87,rely=.15,)
    BtnM = tk.Button(FrameAn, text='Modificar',font=('Comic Sans MS', 15),bg='azure')
    BtnM.place(relx=.87,rely=.4,)
    BtnE = tk.Button(FrameAn, text='Eliminar',font=('Comic Sans MS', 15),bg='azure')
    BtnE.place(relx=.87,rely=.7)
    BtnAt = tk.Button(FrameAn,text='Atras',font=('Comic Sans MS', 15),bg='azure',command=AtrasV)
    BtnAt.place(relx=.01,rely=.1)
    ###################################
    FrameRaza = tk.Frame(FondoV,bg='light gray')
    FrameRaza.place(relwidth=.5,height=545,y=200)
    #####################
    FrameG = tk.Frame(FondoV,bg='azure')
    FrameG.place(relwidth=.5,relheight=1,y=200,relx=.5)
    GridV = ttk.Treeview(FrameG, columns=("Raza","Edad","Peso","Numero oreja","Produccion"))
    GridV.column("#0", width=10)
    GridV.column("Raza", width=200)
    GridV.column("Edad",width=50)
    GridV.column("Peso",width=50)
    GridV.column("Numero oreja",width=100)
    GridV.heading("Raza", text='Raza')
    GridV.heading("Edad", text='Edad\n(meses)')
    GridV.heading("Peso", text="Peso\n(kilos)")
    GridV.heading("Numero oreja", text='Numero oreja')
    GridV.heading("Produccion", text='Produccion\n(Diaria)')
    GridV.place(x=0,y=0,relheight=1,width=680)
    Botones()
    #####################
    VPrincipal.mainloop()
##############################
def VGC(event):

    def limpiar_campos():
            global END
            InEdad.delete(0, tk.END)
            CoRaza.delete(0, tk.END)
            InPeso.delete(0, tk.END)
            InNum.delete(0, tk.END)
    def AnadirCe(): 
        IEdad = int(InEdad.get())
        IPeso = int(InPeso.get())
        IOreja = InNum.get()
        if IEdad>18:
            Rendimiento = (IPeso/IEdad)*20000
        else:
            Rendimiento=0

        if CoRaza.current() == 0:
            CRaza = 'San Pedreño'
        if CoRaza.current() == 1:
            CRaza = 'Zungo'
        if CoRaza.current() == 2:
            CRaza = 'Casco de Mula'
        else:
            pass
        if CRaza and IEdad and IPeso and IOreja:
            try:
                with cnn.cursor() as cur:
                    sql = '''INSERT INTO GanadoV (Edad, Raza, Peso, NOreja, Produccion,Especie) 
                            VALUES (?, ?, ?, ?, ?,?)'''
                    cur.execute(sql, (IEdad, CRaza, IPeso, IOreja, Rendimiento, 'Cerdo'))
                    cnn.commit()
                    messagebox.showinfo("Éxito", "Cerdo fue agregado exitosamente")
                    limpiar_campos()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el cerdo: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")
        Botones()
        limpiar_campos()

    def MostrarV0(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Cerdo':
                            if row[0]=='San Pedreño':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cerdos de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")
    def MostrarV1(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Cerdo':
                            if row[0]=='Zungo':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cerdos de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")
    def MostrarV2(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Cerdo':
                            if row[0]=='Casco de Mula':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cerdos de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")

    def Botones():
        with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                s=0
                z=0
                c=0
                for row in datos:
                    if row[5] == 'Cerdo':
                            if row[0]=='San Pedreño':
                                s=s+1
                            if row[0]=='Zungo': 
                                z=z+1
                            if row[0]=='Casco de Mula':
                                c=c+1
                if s>0:
                    F1 = tk.Button(FrameRaza,text='San Pedreño',bg='azure',font=('Comic Sans MS', 15))
                    F1.place(rely=.1,x=50,relwidth=.8,height=80)
                    F1.bind("<Button-1>", MostrarV0)
                if z>0: 
                    F2 = tk.Button(FrameRaza,text='Zungo',font=('Comic Sans MS', 15),bg='azure')
                    F2.place(rely=.4,x=50,relwidth=.8,height=80)
                    F2.bind("<Button-1>", MostrarV1)
                if c>0:
                    F3 = tk.Button(FrameRaza,text='Casco de Mula',font=('Comic Sans MS', 15),bg='azure')
                    F3.place(rely=.7,x=50,relwidth=.8,height=80)
                    F3.bind("<Button-1>", MostrarV2)
    global FondoC
    fondo.destroy()
    ###############
    FondoC = tk.Frame(VPrincipal)
    FondoC.place(relheight=1,relwidth=1)
    ###################################
    FrameAn = tk.Frame(FondoC,bg='green3')
    FrameAn.place(relwidth=1,height=200)

    LRaza = tk.Label(FrameAn,text='Raza:',bg='green3',font=('Comic Sans MS', 25))
    LRaza.place(relx=.1,rely=.3)
    CoRaza = ttk.Combobox(FrameAn, values=['San Pedreño','Zungo','Casco de Mula'],font=('Comic Sans MS', 25))
    CoRaza.place(relx=.1,rely=.5,width=200)

    LEdad = tk.Label(FrameAn, text='Edad:(meses)', bg='green3',font=('Comic Sans MS', 25))
    LEdad.place(relx=.3,rely=.3)
    InEdad = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InEdad.place(relx=.3,rely=.5,width=100)

    LPeso = tk.Label(FrameAn, text='Peso:(Kilos)', bg='green3',font=('Comic Sans MS', 25))
    LPeso.place(relx=.5,rely=.3)
    InPeso = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InPeso.place(relx=.5,rely=.5,width=100)

    LNum = tk.Label(FrameAn, text='Numero Oreja:', bg='green3',font=('Comic Sans MS', 25))
    LNum.place(relx=.7,rely=.3)
    InNum = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InNum.place(relx=.7,rely=.5,width=200)
    
    BtnA = tk.Button(FrameAn, text='Agregar',font=('Comic Sans MS', 15),bg='azure',command=AnadirCe)
    BtnA.place(relx=.87,rely=.15,)
    BtnM = tk.Button(FrameAn, text='Modificar',font=('Comic Sans MS', 15),bg='azure')
    BtnM.place(relx=.87,rely=.4,)
    BtnE = tk.Button(FrameAn, text='Eliminar',font=('Comic Sans MS', 15),bg='azure')
    BtnE.place(relx=.87,rely=.7)
    BtnAt = tk.Button(FrameAn,text='Atras',font=('Comic Sans MS', 15),bg='azure',command=AtrasC)
    BtnAt.place(relx=.01,rely=.1)
    ###################################
    FrameRaza = tk.Frame(FondoC,bg='light gray')
    FrameRaza.place(relwidth=.5,height=545,y=200)
    Botones()
    
    #####################
    FrameG = tk.Frame(FondoC,bg='azure')
    FrameG.place(relwidth=.5,relheight=1,y=200,relx=.5)
    GridV = ttk.Treeview(FrameG, columns=("Raza","Edad","Peso","Numero oreja","Produccion"))
    GridV.column("#0", width=10)
    GridV.column("Raza", width=200)
    GridV.column("Edad",width=50)
    GridV.column("Peso",width=50)
    GridV.column("Numero oreja",width=100)
    GridV.heading("Raza", text='Raza')
    GridV.heading("Edad", text='Edad\n(meses)')
    GridV.heading("Peso", text="Peso\n(kilos)")
    GridV.heading("Numero oreja", text='Numero oreja')
    GridV.heading("Produccion", text='Produccion\n(Diaria)')
    GridV.place(x=0,y=0,relheight=1,width=680)
    #####################
    VPrincipal.mainloop()
##############################
def VGCa(event):

    def limpiar_campos():
            global END
            InEdad.delete(0, tk.END)
            CoRaza.delete(0, tk.END)
            InPeso.delete(0, tk.END)
            InNum.delete(0, tk.END)
    def AnadirCa(): 
        IEdad = int(InEdad.get())
        IPeso = int(InPeso.get())
        IOreja = InNum.get()
        if IEdad>18:
            Rendimiento = (IPeso/IEdad)*20000
        else:
            Rendimiento=0

        if CoRaza.current() == 0:
            CRaza = 'Saanen'
        if CoRaza.current() == 1:
            CRaza = 'Toggenburg'
        if CoRaza.current() == 2:
            CRaza = 'Alpina'
        if CoRaza.current() == 3:
            CRaza = 'La Mancha'
        else:
            pass
        if CRaza and IEdad and IPeso and IOreja:
            try:
                with cnn.cursor() as cur:
                    sql = '''INSERT INTO GanadoV (Edad, Raza, Peso, NOreja, Produccion,Especie) 
                            VALUES (?, ?, ?, ?, ?,?)'''
                    cur.execute(sql, (IEdad, CRaza, IPeso, IOreja, Rendimiento, 'Cabra'))
                    cnn.commit()
                    messagebox.showinfo("Éxito", "Cabra fue agregada exitosamente")
                    limpiar_campos()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar la cabra: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")
        Botones()
        limpiar_campos()

    def Botones():
        with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                s=0
                z=0
                c=0
                d=0
                for row in datos:
                    if row[5] == 'Cabra':
                            if row[0]=='Saanen':
                                s=s+1
                            if row[0]=='Toggenburg': 
                                z=z+1
                            if row[0]=='Alpina':
                                c=c+1
                            if row[0]=='La Mancha':
                                d=d+1
                if s>0:
                    F1 = tk.Button(FrameRaza,text='Saanen',bg='azure',font=('Comic Sans MS', 15))
                    F1.place(rely=.1,x=50,relwidth=.8,height=80)
                    F1.bind("<Button-1>", MostrarV0)
                if z>0: 
                    F2 = tk.Button(FrameRaza,text='Toggenburg',font=('Comic Sans MS', 15),bg='azure')
                    F2.place(rely=.3,x=50,relwidth=.8,height=80)
                    F2.bind("<Button-1>", MostrarV1)
                if c>0:
                    F3 = tk.Button(FrameRaza,text='Alpina',font=('Comic Sans MS', 15),bg='azure')
                    F3.place(rely=.5,x=50,relwidth=.8,height=80)
                    F3.bind("<Button-1>", MostrarV2)
                if d>0:
                    F4 = tk.Button(FrameRaza,text='La Mancha',font=('Comic Sans MS', 15),bg='azure')
                    F4.place(rely=.7,x=50,relwidth=.8,height=80)
                    F4.bind("<Button-1>", MostrarV3)
    def MostrarV0(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Cabra':
                            if row[0]=='Saanen':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cabras de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")
    def MostrarV1(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Cabra':
                            if row[0]=='Toggenburg':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cabras de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")
    def MostrarV2(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Cabra':
                            if row[0]=='Alpina':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cabras de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")
    def MostrarV3(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Cabra':
                            if row[0]=='La Mancha':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cabras de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")
    
    global FondoCa
    fondo.destroy()
    FondoCa = tk.Frame(VPrincipal)
    FondoCa.place(relheight=1,relwidth=1)
    ######################################
    FrameAn = tk.Frame(FondoCa,bg='green3')
    FrameAn.place(relwidth=1,height=200)

    LRaza = tk.Label(FrameAn,text='Raza:',bg='green3',font=('Comic Sans MS', 25))
    LRaza.place(relx=.1,rely=.3)
    CoRaza = ttk.Combobox(FrameAn, values=['Saanen','Toggenburg','Alpina','La Mancha'],font=('Comic Sans MS', 25))
    CoRaza.place(relx=.1,rely=.5,width=200)

    LEdad = tk.Label(FrameAn, text='Edad:(meses)', bg='green3',font=('Comic Sans MS', 25))
    LEdad.place(relx=.3,rely=.3)
    InEdad = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InEdad.place(relx=.3,rely=.5,width=100)

    LPeso = tk.Label(FrameAn, text='Peso:(Kilos)', bg='green3',font=('Comic Sans MS', 25))
    LPeso.place(relx=.5,rely=.3)
    InPeso = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InPeso.place(relx=.5,rely=.5,width=100)

    LNum = tk.Label(FrameAn, text='Numero Oreja:', bg='green3',font=('Comic Sans MS', 25))
    LNum.place(relx=.7,rely=.3)
    InNum = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InNum.place(relx=.7,rely=.5,width=200)
    
    BtnA = tk.Button(FrameAn, text='Agregar',font=('Comic Sans MS', 15),bg='azure', command=AnadirCa)
    BtnA.place(relx=.87,rely=.15,)
    BtnM = tk.Button(FrameAn, text='Modificar',font=('Comic Sans MS', 15),bg='azure')
    BtnM.place(relx=.87,rely=.4,)
    BtnE = tk.Button(FrameAn, text='Eliminar',font=('Comic Sans MS', 15),bg='azure')
    BtnE.place(relx=.87,rely=.7)
    BtnAt = tk.Button(FrameAn,text='Atras',font=('Comic Sans MS', 15),bg='azure',command=AtrasCa)
    BtnAt.place(relx=.01,rely=.1)
    ###################################
    FrameRaza = tk.Frame(FondoCa,bg='light gray')
    FrameRaza.place(relwidth=.5,height=545,y=200)

    
    #####################
    FrameG = tk.Frame(FondoCa,bg='azure')
    FrameG.place(relwidth=.5,relheight=1,y=200,relx=.5)
    GridV = ttk.Treeview(FrameG, columns=("Raza","Edad","Peso","Numero oreja","Produccion"))
    GridV.column("#0", width=10)
    GridV.column("Raza", width=200)
    GridV.column("Edad",width=50)
    GridV.column("Peso",width=50)
    GridV.column("Numero oreja",width=100)
    GridV.heading("Raza", text='Raza')
    GridV.heading("Edad", text='Edad\n(meses)')
    GridV.heading("Peso", text="Peso\n(kilos)")
    GridV.heading("Numero oreja", text='Numero oreja')
    GridV.heading("Produccion", text='Produccion\n(Diaria)')
    GridV.place(x=0,y=0,relheight=1,width=680)
    Botones()
    #####################
    VPrincipal.mainloop()
##############################
def VGG(event):

    def limpiar_campos():
            global END
            InEdad.delete(0, tk.END)
            CoRaza.delete(0, tk.END)
            InPeso.delete(0, tk.END)
            InNum.delete(0, tk.END)
    def AnadirGa(): 
        IEdad = int(InEdad.get())
        IPeso = int(InPeso.get())
        IOreja = InNum.get()
        if IEdad>18:
            Rendimiento = (IPeso/IEdad)*20000
        else:
            Rendimiento=0

        if CoRaza.current() == 0:
            CRaza = 'Leghorn Blanca'
        if CoRaza.current() == 1:
            CRaza = 'Rhode Island Roja'
        if CoRaza.current() == 2:
            CRaza = 'New Hampshire'
        if CoRaza.current() == 3:
            CRaza = 'Cornish'
        if CoRaza.current() == 4:
            CRaza = 'Sussex Clara'
        else:
            pass
        if CRaza and IEdad and IPeso and IOreja:
            try:
                with cnn.cursor() as cur:
                    sql = '''INSERT INTO GanadoV (Edad, Raza, Peso, NOreja, Produccion,Especie) 
                            VALUES (?, ?, ?, ?, ?,?)'''
                    cur.execute(sql, (IEdad, CRaza, IPeso, IOreja, Rendimiento, 'Gallina'))
                    cnn.commit()
                    messagebox.showinfo("Éxito", "Galina fue agregada exitosamente")
                    limpiar_campos()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar la Gallina: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")
        Botones()
        limpiar_campos()

    def Botones():
        with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                s=0
                z=0
                c=0
                d=0
                a=0
                for row in datos:
                    if row[5] == 'Gallina':
                            if row[0]=='Leghorn Blanca':
                                s=s+1
                            if row[0]=='Rhode Island Roja': 
                                z=z+1
                            if row[0]=='New Hampshire':
                                c=c+1
                            if row[0]=='Cornish':
                                d=d+1
                            if row[0]=='Sussex Clara':
                                a=a+1
                if s>0:
                    F1 = tk.Button(FrameRaza,text='Leghorn Blanca',bg='azure',font=('Comic Sans MS', 15))
                    F1.place(rely=.03,x=50,relwidth=.8,height=80)
                    F1.bind("<Button-1>", MostrarV0)
                if z>0: 
                    F2 = tk.Button(FrameRaza,text='Rhode Island Roja',font=('Comic Sans MS', 15),bg='azure')
                    F2.place(rely=.23,x=50,relwidth=.8,height=80)
                    F2.bind("<Button-1>", MostrarV1)
                if c>0:
                    F3 = tk.Button(FrameRaza,text='New Hampshire',font=('Comic Sans MS', 15),bg='azure')
                    F3.place(rely=.43,x=50,relwidth=.8,height=80)
                    F3.bind("<Button-1>", MostrarV2)
                if d>0:
                    F4 = tk.Button(FrameRaza,text='Cornish',font=('Comic Sans MS', 15),bg='azure')
                    F4.place(rely=.63,x=50,relwidth=.8,height=80)
                    F4.bind("<Button-1>", MostrarV3)
                if a>0:
                    F5 = tk.Button(FrameRaza,text='Sussex Clara',font=('Comic Sans MS', 15),bg='azure')
                    F5.place(rely=.83,x=50,relwidth=.8,height=80)
                    F5.bind("<Button-1>", MostrarV4)
    def MostrarV0(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Gallina':
                            if row[0]=='Leghorn Blanca':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cabras de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")
    def MostrarV1(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Gallina':
                            if row[0]=='Rhode Island Roja':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cabras de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")
    def MostrarV2(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Gallina':
                            if row[0]=='New Hampshire':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cabras de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")
    def MostrarV3(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Gallina':
                            if row[0]=='Cornish':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cabras de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los cerdos: {str(e)}")
    def MostrarV4(event):
        GridV.delete(*GridV.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM GanadoV")
                datos = cur.fetchall()
                c=0
                for row in datos:
                    if row[5] == 'Gallina':
                            if row[0]=='Sussex Clara':
                                GridV.insert("",'end', values=(row[0], row[1], row[2], row[3], row[4]))
                                c=+1
                            else:
                                pass
                if c==0:
                    messagebox.showerror("advertercia",f"no hay cabras de esta raza")
                else:
                    pass
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de las gallinas: {str(e)}")

    global FondoGa
    fondo.destroy()
    FondoGa = tk.Frame(VPrincipal)
    FondoGa.place(relheight=1,relwidth=1)
    ####################################
    FrameAn = tk.Frame(FondoGa,bg='green3')
    FrameAn.place(relwidth=1,height=200)

    LRaza = tk.Label(FrameAn,text='Raza:',bg='green3',font=('Comic Sans MS', 25))
    LRaza.place(relx=.1,rely=.3)
    CoRaza = ttk.Combobox(FrameAn, values=['Leghorn Blanca','Rhode Island Roja','New Hampshire','Cornish','Sussex Clara'],font=('Great Vibes', 25))
    CoRaza.place(relx=.1,rely=.5,width=200)

    LEdad = tk.Label(FrameAn, text='Edad:(meses)', bg='green3',font=('Comic Sans MS', 25))
    LEdad.place(relx=.3,rely=.3)
    InEdad = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InEdad.place(relx=.3,rely=.5,width=100)

    LPeso = tk.Label(FrameAn, text='Peso:(Kilos)', bg='green3',font=('Comic Sans MS', 25))
    LPeso.place(relx=.5,rely=.3)
    InPeso = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InPeso.place(relx=.5,rely=.5,width=100)

    LNum = tk.Label(FrameAn, text='Numero Oreja:', bg='green3',font=('Comic Sans MS', 25))
    LNum.place(relx=.7,rely=.3)
    InNum = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InNum.place(relx=.7,rely=.5,width=200)
    
    BtnA = tk.Button(FrameAn, text='Agregar',font=('Comic Sans MS', 15),bg='azure',command=AnadirGa)
    BtnA.place(relx=.87,rely=.15,)
    BtnM = tk.Button(FrameAn, text='Modificar',font=('Comic Sans MS', 15),bg='azure')
    BtnM.place(relx=.87,rely=.4,)
    BtnE = tk.Button(FrameAn, text='Eliminar',font=('Comic Sans MS', 15),bg='azure')
    BtnE.place(relx=.87,rely=.7)
    BtnAt = tk.Button(FrameAn,text='Atras',font=('Comic Sans MS', 15),bg='azure',command=AtrasGa)
    BtnAt.place(relx=.01,rely=.1)
    ###################################
    FrameRaza = tk.Frame(FondoGa,bg='light gray')
    FrameRaza.place(relwidth=.5,height=545,y=200)

    Botones()
    
    #####################
    FrameG = tk.Frame(FondoGa,bg='azure')
    FrameG.place(relwidth=.5,relheight=1,y=200,relx=.5)
    GridV = ttk.Treeview(FrameG, columns=("Raza","Edad","Peso","Numero oreja","Produccion"))
    GridV.column("#0", width=10)
    GridV.column("Raza", width=200)
    GridV.column("Edad",width=50)
    GridV.column("Peso",width=50)
    GridV.column("Numero oreja",width=100)
    GridV.heading("Raza", text='Raza')
    GridV.heading("Edad", text='Edad\n(meses)')
    GridV.heading("Peso", text="Peso\n(kilos)")
    GridV.heading("Numero oreja", text='Numero oreja')
    GridV.heading("Produccion", text='Produccion\n(Diaria)')
    GridV.place(x=0,y=0,relheight=1,width=680)
    #####################
    VPrincipal.mainloop()
##############################
def VCultivo():

    def AnadirCul(): 
        INombre = InNombre.get()
        IArea = int(InArea.get())
        Rendimiento = 0
        if CoTipo.current() == 0:
            Rendimiento =  (((IArea*3)*1200000)-(IArea*1400000))
            CTipo = 'Cereales'
        if CoTipo.current() == 1:
            Rendimiento = (((IArea*1.5)*1100000)-(IArea*1300000))
            CTipo = 'Leguminosas'
        if CoTipo.current() == 2:
            Rendimiento = (((IArea * 15)*700000)-(IArea*20000000))
            CTipo = 'Hortalizas'
        if CoTipo.current() == 3:
            Rendimiento = (((IArea*20)*600000)-(IArea*1500000))
            CTipo = 'Tubérculos'
        else:
            print(Rendimiento)
        if CTipo and InNombre and InArea:
            try:
                with cnn.cursor() as cur:
                    sql = '''INSERT INTO Cultivos (Nombre, Tipo, AreaCultivo, Rendimiento) 
                            VALUES (?, ?, ?, ?)'''
                    cur.execute(sql, (INombre, CTipo, IArea, Rendimiento))
                    cnn.commit()
                    messagebox.showinfo("Éxito", "Cultivo agregado exitosamente")
                    #limpiar_campos()
                    #llenar_datos()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo agregar el Cultivo: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")
        limpiar_campos()
        MostrarCult()
    def limpiar_campos():
            global END
            InArea.delete(0, tk.END)
            InNombre.delete(0, tk.END)
            CoTipo.delete(0, tk.END)
    def MostrarCult():
        GridCu.delete(*GridCu.get_children())
        try:
            with cnn.cursor() as cur:
                cur.execute("SELECT * FROM Cultivos")
                datos = cur.fetchall()
                for row in datos:
                    GridCu.insert("",'end', values=(row[0], row[1], row[2], row[3]))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener los datos de los Cultivos: {str(e)}")
    def modificar():
        seleccion = GridCu.focus()
        if seleccion:
            detalles_Cultivo = GridCu.item(seleccion)
            nombre = detalles_Cultivo['values']
            nombre = nombre.pop(0)

            def guardar_modificaciones():
                nuevo_nombre = InNombre.get()
                IArea = int(InArea.get())

                if CoTipo.current() == 0:
                    Rendimiento =  (((IArea*3)*1200000)-(IArea*1400000))
                    CTipo = 'Cereales'
                if CoTipo.current() == 1:
                    Rendimiento = (((IArea*1.5)*1100000)-(IArea*1300000))
                    CTipo = 'Leguminosas'
                if CoTipo.current() == 2:
                    Rendimiento = (((IArea * 15)*700000)-(IArea*20000000))
                    CTipo = 'Hortalizas'
                if CoTipo.current() == 3:
                    Rendimiento = (((IArea*20)*600000)-(IArea*1500000))
                    CTipo = 'Tubérculos'
                with cnn.cursor() as cur:
                    sql = """Update Cultivos
                    set Nombre = ? , Tipo=?,AreaCultivo=?,Rendimiento=?
                    where Nombre = ?"""
                    cur.execute(sql,(nuevo_nombre,CTipo,IArea,Rendimiento,nombre))
                GridCu.item(seleccion, values=(nuevo_nombre, CTipo, IArea ))
                cnn.commit()
                ventana_modificar.destroy()

            ventana_modificar = tk.Toplevel()
            ventana_modificar.title("Alerta")

            nuevo_nombre_label = tk.Label(ventana_modificar, text="seguro que quiere modificar el Cultivo "+detalles_Cultivo['values'][0])
            nuevo_nombre_label.grid(row=0, column=0)


            guardar_button = tk.Button(ventana_modificar, text="Modificar", command=guardar_modificaciones)
            guardar_button.grid(row=8, columnspan=2)

        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione un cultivo para modificar")
    def eliminar():
        seleccion = GridCu.focus()
        if seleccion: 
            detalles_Cultivo = GridCu.item(seleccion)
            nombre = detalles_Cultivo['values']
            nombre = nombre.pop(0)
            try:
                with cnn.cursor() as cur:
                    sql = "DELETE FROM Cultivos WHERE Nombre = ?"
                    cur.execute(sql, (nombre))
                    cnn.commit()
                    messagebox.showinfo("Éxito", "Cultivo eliminado exitosamente")
                    MostrarCult() 
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el cultivo: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione un cultivo")
        MostrarCult()
    
    global FondoCu
    FondoCu = tk.Frame(VPrincipal, bg='light grey')
    FondoCu.place(relheight=1, relwidth=1)
    #####################################
    FrameAn = tk.Frame(FondoCu,bg='green3')
    FrameAn.place(relwidth=1,height=200)

    LTipo = tk.Label(FrameAn,text='Tipo:',bg='green3',font=('Comic Sans MS', 25))
    LTipo.place(relx=.1,rely=.2)
    CoTipo = ttk.Combobox(FrameAn, values=['Cereales','Leguminosas','Hortalizas','Tubérculos'],font=('Comic Sans MS', 25))
    CoTipo.place(relx=.1,rely=.5,width=200)

    LNombre = tk.Label(FrameAn, text='Nombre:', bg='green3',font=('Comic Sans MS', 25))
    LNombre.place(relx=.3,rely=.3)
    InNombre = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InNombre.place(relx=.3,rely=.5,width=200)

    LArea = tk.Label(FrameAn, text='Area de cultivo:(hectarea)', bg='green3',font=('Comic Sans MS', 25))
    LArea.place(relx=.5,rely=.3)
    InArea = tk.Entry(FrameAn,font=('Comic Sans MS', 25))
    InArea.place(relx=.5,rely=.5,width=150)

    
    BtnA = tk.Button(FrameAn, text='Agregar',font=('Comic Sans MS', 15),bg='azure',command=AnadirCul)
    BtnA.place(relx=.87,rely=.15,)
    BtnM = tk.Button(FrameAn, text='Modificar',font=('Comic Sans MS', 15),bg='azure',command=modificar)
    BtnM.place(relx=.87,rely=.4,)
    BtnE = tk.Button(FrameAn, text='Eliminar',font=('Comic Sans MS', 15),bg='azure',command=eliminar)
    BtnE.place(relx=.87,rely=.7)
    BtnAt = tk.Button(FrameAn,text='Atras',font=('Comic Sans MS', 15),bg='azure',command=AtrasCu)
    BtnAt.place(relx=.01,rely=.1)
    ##############################
    FrameTab = tk.Frame(FondoCu,bg='azure')
    FrameTab.place(relwidth=.75,relheight=1,y=200,relx=.3)
    GridCu = ttk.Treeview(FrameTab, columns=("Nombre","Tipo","Area de cultivo","Produccion"))
    GridCu.column("#0", width=1)
    GridCu.column("Nombre", width=200)
    GridCu.column("Tipo",width=100)
    GridCu.column("Area de cultivo",width=70)
    GridCu.heading("Nombre", text='Nombre')
    GridCu.heading("Tipo", text='Tipo')
    GridCu.heading("Area de cultivo", text="Area de cultivo\n(hectarea)")
    GridCu.heading("Produccion", text='Produccion\n(Cosecha)')
    GridCu.place(x=0,y=0,relheight=1,relwidth=1)
    ############################################
    ICultivo = Image.open('imagenes/Banner_cultivo.png')
    ICultivo = ICultivo.resize((500,800))
    ICultivo = ImageTk.PhotoImage(ICultivo)
    FrameIm = tk.Frame(FondoCu)
    FrameIm.place(relwidth=.3,relheight=1,y=200)
    LIm = tk.Label(FrameIm, image=ICultivo)
    LIm.pack()
    MostrarCult()



    VPrincipal.mainloop()
##############################
def VTotal():
    global FondoRe
    FondoRe = tk.Frame(VPrincipal, bg='green4')
    FondoRe.place(relheight=1, relwidth=1)

    ICultivo = Image.open('imagenes/banner_re.png')
    ICultivo = ICultivo.resize((1020,800))
    ICultivo = ImageTk.PhotoImage(ICultivo)

    ProTot=0
    with cnn.cursor() as cur:
        cur.execute("SELECT * FROM GanadoV")
        datos = cur.fetchall()
        for row in datos:
            ProTot= ProTot+row[4]
    with cnn.cursor() as cur:
        cur.execute("SELECT * FROM Cultivos")
        datos = cur.fetchall()
        for row in datos:
            ProTot= ProTot+row[3]
    LIF = tk.Label(FondoRe,bg='green4')
    LIF.place(relheight=1,relwidth=1)
    #####################################
    BtnAt = tk.Button(FondoRe,text='Atras',font=('Comic Sans MS', 15),bg='azure',command=AtrasRe)
    BtnAt.place(relx=.01,rely=.01)
    ######################

    total = '$'+str(ProTot)
    LT = tk.Label(FondoRe,text='Produccion Total de la granja',font=('Comic Sans MS', 50),bg='green4',anchor='center')
    LT.place(relwidth=1,rely=.1)
    LTP = tk.Label(FondoRe,text=total ,font=('Comic Sans MS', 100),bg='green4',anchor='center')
    LTP.place(relwidth=1,rely=.3)
    VPrincipal.mainloop()


    
##############################
def Salir(event):
    pass
##############################
def AtrasC():
    FondoC.destroy()
    VGanado()
def AtrasV():
    FondoV.destroy()
    VGanado()
def AtrasCa():
    FondoCa.destroy()
    VGanado()
def AtrasGa():
    FondoGa.destroy()
    VGanado()
##############################
def AtrasG():
    fondo.destroy()
    Vprincipal()
def AtrasCu():
    FondoCu.destroy()
    Vprincipal()
def AtrasRe():
    FondoRe.destroy()
    Vprincipal()
##############################
def Vprincipal():
    global Background

    #################################################
    Background = tk.Frame(VPrincipal, bg='light grey')
    Background.place(relheight=1, relwidth=1)
    ##################################################
    FrameHead = tk.Frame(VPrincipal, bg='light grey')
    FrameHead.place(x=0, y=0, relwidth=1, height=60)
    FPL = tk.Label(FrameHead, text='Granja Ucundinamarca', font=('Comic Sans MS', 25), bg='light grey')
    FPL.place(x=20, y=20)

    ##################################################

    FrameCul = tk.Frame(VPrincipal, bg='azure',)
    FrameCul.place(x=150, y=100, width=300, height=550)
    FrameCul.config(highlightbackground="black", highlightthickness=1)

    icul = Image.open('imagenes/cul.png')
    icul = icul.resize((250, 250))
    icul = ImageTk.PhotoImage(icul)
    CulL1 = tk.Label(FrameCul, image=icul, bg='azure')
    CulL1.place(x=0, y=50, width=290, height=290)
    CulL2 = tk.Label(FrameCul, text='CULTIVOS', bg='azure', anchor='center', font=('Comic Sans MS', 25))
    CulL2.place(relwidth=1, rely=.7)

    FrameCul.bind("<Button-1>", VCul)
    CulL1.bind("<Button-1>", VCul)
    CulL2.bind("<Button-1>", VCul)
    #######################################

    FrameGan = tk.Frame(VPrincipal, bg='azure')
    FrameGan.place(x=550, y=100, width=300, height=550)
    FrameGan.config(highlightbackground="black", highlightthickness=1)

    iGan = Image.open('imagenes/Gan.png')
    iGan = iGan.resize((300, 300))
    iGan = ImageTk.PhotoImage(iGan)
    GanL1 = tk.Label(FrameGan, image=iGan, bg='azure')
    GanL1.place(x=0, y=50, width=290, height=290)
    GanL2 = tk.Label(FrameGan, text='GANADO', bg='azure', anchor='center', font=('Comic Sans MS', 25))
    GanL2.place(relwidth=1, rely=.7)

    FrameGan.bind("<Button-1>", Vgan)
    GanL1.bind("<Button-1>", Vgan)
    GanL2.bind("<Button-1>", Vgan)
    ########################################

    FrameTo = tk.Frame(VPrincipal, bg='azure')
    FrameTo.place(x=950, y=100, width=300, height=550)
    FrameTo.config(highlightbackground="black", highlightthickness=1)

    iTo = Image.open('imagenes/total.png')
    iTo = iTo.resize((400, 400))
    iTo = ImageTk.PhotoImage(iTo)
    ToL1 = tk.Label(FrameTo, image=iTo, bg='azure')
    ToL1.place(x=0, y=50, width=290, height=290)
    ToL2 = tk.Label(FrameTo, text='REPORTE', bg='azure', anchor='center', font=('Comic Sans MS', 25))
    ToL2.place(relwidth=1, rely=.7)

    FrameTo.bind("<Button-1>", VTo)
    ToL2.bind("<Button-1>", VTo)
    ToL1.bind("<Button-1>", VTo)
    VPrincipal.mainloop()
##############################
def Vgan(event):
    Background.destroy()
    VGanado()
def VCul(event):
    Background.destroy()
    VCultivo()
def VTo(event):
    Background.destroy()
    VTotal()
DATABASE = 'Granja'
try:
    cnn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'Server=KAKAROTTO639\SQLEXPRESS;'
        'DATABASE='+DATABASE+';'
        'Trusted_Connection=yes;'
    )
    print('conexion exitosa')
except pyodbc.Error as e:
    messagebox.showerror("Error", f"No se pudo Conectar al servidor: {e}")
except Exception as ex:
    messagebox.showerror("Error", f"Se ha producido un error: {ex}")

##############################
if __name__ == "__main__":
    VPrincipal = tk.Tk()
    VPrincipal.title('Granja Ucundinamarca')
    VPrincipal.state('zoomed')
    Vprincipal()