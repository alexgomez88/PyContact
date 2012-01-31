import gtk
import matplotlib
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
from matplotlib.backends.backend_gtkagg import NavigationToolbar2GTKAgg as NavigationToolbar
from matplotlib.figure import Figure

class Results:
    def __init__(self):
    	#Crear Ventana
        self.window = gtk.Window()
        #Definir tamano de la ventana
        self.window.set_default_size(800,500)
        #Titulo de la ventana
        self.window.set_title("Analisis de contacto")
        #Conecta el cerrar de la ventana con cerrar el programa
        self.window.show_all()
        self.window.show()

class GUI:
    def click_analize(self, widget, data=None):
		anal=Results()
		return anal

    def __init__(self):
    	#Crear Ventana
        self.window = gtk.Window()
        #Definir tamano de la ventana
        self.window.set_default_size(800,500)
        #Titulo de la ventana
        self.window.set_title("MetroContactCCS - Beta")
        #Conecta el cerrar de la ventana con cerrar el programa
        self.window.connect("destroy",lambda x: gtk.main_quit())

        #Elementos de diseno para la creacion del programa.

        #Divisiones Verticales
        self.vbox1=gtk.VBox()
        self.vbox2=gtk.VBox()
        self.vbox2.set_size_request(320,-1)
        self.vbox3=gtk.VBox()
        self.vbox4=gtk.VBox()
        self.vboxA1=gtk.VBox()
        self.vboxB1=gtk.VBox()
        self.vboxA2=gtk.VBox()
        self.vboxB2=gtk.VBox()
        self.vbox101=gtk.VBox()
        self.vbox102=gtk.VBox()
        self.vboxgrafA1=gtk.VBox()
        self.vboxgrafB1=gtk.VBox()
        self.vboxgrafA2=gtk.VBox()
        self.vboxgrafB2=gtk.VBox()
        self.vboxgraf101=gtk.VBox()
        self.vboxgraf102=gtk.VBox()

        #Divisiones Horizontales
        self.hbox1=gtk.HBox()
        self.hbox2=gtk.HBox()
        self.hboxg101=gtk.HBox()
        self.hboxg102=gtk.HBox()
        self.statusbar=gtk.Statusbar()

        #Areas graficas
        fig101 = Figure(figsize=(5,4), dpi=100)
        self.canvas101 = FigureCanvas(fig101)
        fig102 = Figure(figsize=(5,4), dpi=100)
        self.canvas102 = FigureCanvas(fig102)

        #Encabezados
        self.title1=gtk.Label('Indique el archivo CSV con la data del sistema de adquisicion de datos.')
        self.title1.set_line_wrap(True)
        self.title1.set_justify(gtk.JUSTIFY_CENTER)
        self.title2=gtk.Label('Resumen del analisis del contacto en la rueda.')
        self.title2.set_line_wrap(True)
        self.title2.set_justify(gtk.JUSTIFY_CENTER)
        self.title3=gtk.Label("Resumen del analisis del contacto en el eje.")
        self.title3.set_line_wrap(True)
        self.title3.set_justify(gtk.JUSTIFY_CENTER)
        self.title4=gtk.Label("Graficos de los datos filtrados para analisis.")
        self.title4.set_line_wrap(True)
        self.title4.set_justify(gtk.JUSTIFY_CENTER)
        self.autor_label=gtk.Label("Creado por Alejandro Gomez para Metro de Caracas C.A.")

        #Etiquetas sobre variables de estudio en la rueda A1
        self.loadmaxV_A1=gtk.Label('Carga Vertical Maxima: 0.00 kN')
        self.loadminV_A1=gtk.Label('Carga Vertical Minima: 0.00 kN')
        self.loadpromV_A1=gtk.Label('Carga Vertical Promedio: 0.00 kN')
        self.loadmaxL_A1=gtk.Label('Carga Lateral Maxima: 0.00 kN')
        self.loadminL_A1=gtk.Label('Carga Lateral Minima: 0.00 kN')
        self.loadpromL_A1=gtk.Label('Carga Lateral Promedio: 0.00 kN')
        self.loadmaxLong_A1=gtk.Label('Carga Longitudinal Maxima: 0.00 kN')
        self.loadminLong_A1=gtk.Label('Carga Longitudinal Minima: 0.00 kN')
        self.loadpromLong_A1=gtk.Label('Carga Longitudinal Promedio: 0.00 kN')
        self.posMax_A1=gtk.Label('Posicion Maxima: 0.00 mm')
        self.posMin_A1=gtk.Label('Posicion Minima: 0.00 mm')
        self.posprom_A1=gtk.Label('Posicion Promedio: 0.00 mm')

        #Etiquetas sobre variables de estudio en la rueda B1
        self.loadmaxV_B1=gtk.Label('Carga Vertical Maxima: 0.00 kN')
        self.loadminV_B1=gtk.Label('Carga Vertical Minima: 0.00 kN')
        self.loadpromV_B1=gtk.Label('Carga Vertical Promedio: 0.00 kN')
        self.loadmaxL_B1=gtk.Label('Carga Lateral Maxima: 0.00 kN')
        self.loadminL_B1=gtk.Label('Carga Lateral Minima: 0.00 kN')
        self.loadpromL_B1=gtk.Label('Carga Lateral Promedio: 0.00 kN')
        self.loadmaxLong_B1=gtk.Label('Carga Longitudinal Maxima: 0.00 kN')
        self.loadminLong_B1=gtk.Label('Carga Longitudinal Minima: 0.00 kN')
        self.loadpromLong_B1=gtk.Label('Carga Longitudinal Promedio: 0.00 kN')
        self.posMax_B1=gtk.Label('Posicion Maxima: 0.00 mm')
        self.posMin_B1=gtk.Label('Posicion Minima: 0.00 mm')
        self.posprom_B1=gtk.Label('Posicion Promedio: 0.00 mm')

        #Etiquetas sobre variables de estudio en la rueda A2
        self.loadmaxV_A2=gtk.Label('Carga Vertical Maxima: 0.00 kN')
        self.loadminV_A2=gtk.Label('Carga Vertical Minima: 0.00 kN')
        self.loadpromV_A2=gtk.Label('Carga Vertical Promedio: 0.00 kN')
        self.loadmaxL_A2=gtk.Label('Carga Lateral Maxima: 0.00 kN')
        self.loadminL_A2=gtk.Label('Carga Lateral Minima: 0.00 kN')
        self.loadpromL_A2=gtk.Label('Carga Lateral Promedio: 0.00 kN')
        self.loadmaxLong_A2=gtk.Label('Carga Longitudinal Maxima: 0.00 kN')
        self.loadminLong_A2=gtk.Label('Carga Longitudinal Minima: 0.00 kN')
        self.loadpromLong_A2=gtk.Label('Carga Longitudinal Promedio: 0.00 kN')
        self.posMax_A2=gtk.Label('Posicion Maxima: 0.00 mm')
        self.posMin_A2=gtk.Label('Posicion Minima: 0.00 mm')
        self.posprom_A2=gtk.Label('Posicion Promedio: 0.00 mm')

        #Etiquetas sobre variables de estudio en la rueda B1
        self.loadmaxV_B2=gtk.Label('Carga Vertical Maxima: 0.00 kN')
        self.loadminV_B2=gtk.Label('Carga Vertical Minima: 0.00 kN')
        self.loadpromV_B2=gtk.Label('Carga Vertical Promedio: 0.00 kN')
        self.loadmaxL_B2=gtk.Label('Carga Lateral Maxima: 0.00 kN')
        self.loadminL_B2=gtk.Label('Carga Lateral Minima: 0.00 kN')
        self.loadpromL_B2=gtk.Label('Carga Lateral Promedio: 0.00 kN')
        self.loadmaxLong_B2=gtk.Label('Carga Longitudinal Maxima: 0.00 kN')
        self.loadminLong_B2=gtk.Label('Carga Longitudinal Minima: 0.00 kN')
        self.loadpromLong_B2=gtk.Label('Carga Longitudinal Promedio: 0.00 kN')
        self.posMax_B2=gtk.Label('Posicion Maxima: 0.00 mm')
        self.posMin_B2=gtk.Label('Posicion Minima: 0.00 mm')
        self.posprom_B2=gtk.Label('Posicion Promedio: 0.00 mm')

        #Etiqueta sobre variables de estudio del eje 101
        self.hunting_101=gtk.Label('Frecuencia de Hunting: 0 rad/s')
        self.trochamax_101=gtk.Label('Diferencia de trocha max: 0.00 mm')
        self.percep_101=gtk.Label('Peralte: 0.00')

        #Etiqueta sobre variables de estudio del eje 102
        self.hunting_102=gtk.Label('Frecuencia de Hunting: 0 rad/s')
        self.trochamax_102=gtk.Label('Diferencia de trocha max: 0.00 mm')
        self.percep_102=gtk.Label('Peralte: 0.00')

        #Ficheros
        self.fichero1=gtk.Notebook()
        self.fichero2=gtk.Notebook()
        self.fichero3=gtk.Notebook()

        #Frames
        self.frameA1=gtk.Frame('Resumen del Analisis de la Rueda A1')
        self.frameB1=gtk.Frame('Resumen del Analisis de la Rueda B1')
        self.frameA2=gtk.Frame('Resumen del Analisis de la Rueda A2')
        self.frameB2=gtk.Frame('Resumen del Analisis de la Rueda B2')
        self.frame101=gtk.Frame('Resumen del Analisis en el eje 101')
        self.frame102=gtk.Frame('Resumen del Analisis en el eje 102')
        self.frame_map=gtk.Frame(self.title4.get_label())

        #Botones de accion:
        self.fileselect=gtk.FileChooserButton("Selecciona el archivo")
        self.load_data_button=gtk.Button("Cargar Data")
        self.load_data_button.connect("clicked", self.click_analize)

        #Visualizacion de la parte grafica (Checkboxs)
        #A1
        self.checkVLoadA1=gtk.CheckButton('Cargas Verticales')
        self.checkLLoadA1=gtk.CheckButton('Cargas Laterales')
        self.checkLongLoadA1=gtk.CheckButton('Cargas Longitudinales')
        self.checkPosA1=gtk.CheckButton('Posicion del punto de contacto')
        #B1
        self.checkVLoadB1=gtk.CheckButton('Cargas Verticales')
        self.checkLLoadB1=gtk.CheckButton('Cargas Laterales')
        self.checkLongLoadB1=gtk.CheckButton('Cargas Longitudinales')
        self.checkPosB1=gtk.CheckButton('Posicion del punto de contacto')
        #101
        self.checkSpeed1=gtk.CheckButton('Velocidad en el eje')
        #A2
        self.checkVLoadA2=gtk.CheckButton('Cargas Verticales')
        self.checkLLoadA2=gtk.CheckButton('Cargas Laterales')
        self.checkLongLoadA2=gtk.CheckButton('Cargas Longitudinales')
        self.checkPosA2=gtk.CheckButton('Posicion del punto de contacto')
        #B2
        self.checkVLoadB2=gtk.CheckButton('Cargas Verticales')
        self.checkLLoadB2=gtk.CheckButton('Cargas Laterales')
        self.checkLongLoadB2=gtk.CheckButton('Cargas Longitudinales')
        self.checkPosB2=gtk.CheckButton('Posicion del punto de contacto')
        #102
        self.checkSpeed2=gtk.CheckButton('Velocidad en el eje')
        #Barra de progreso
        self.progreswatch=gtk.ProgressBar()

        #Ubicacion en el el programa
        self.window.add(self.vbox1) #Division vertical de la ventana
        self.vbox1.pack_start(self.hbox1) #Area superior divida horizontalmente
        #------------------------------------
        #Area Izquierda
        self.hbox1.pack_start(self.vbox2,False,True,6)
        self.vbox2.pack_start(self.title1,False,False,1)
        self.vbox2.pack_start(self.hbox2,False,False,1)
        self.hbox2.pack_start(self.fileselect,True,True,5)
        self.hbox2.pack_start(self.load_data_button,False,True,5)
        self.vbox2.pack_start(self.progreswatch,False,True,5)
        self.vbox2.pack_start(self.title2,False,False,1)
        self.vbox2.pack_start(self.fichero1,False,True,5)
        #Ficha A1
        self.fichero1.append_page(self.frameA1,tab_label=gtk.Label('Rueda A1'))
        self.frameA1.add(self.vboxA1)
        self.vboxA1.pack_start(self.loadmaxV_A1)
        self.vboxA1.pack_start(self.loadminV_A1)
        self.vboxA1.pack_start(self.loadpromV_A1)
        self.vboxA1.pack_start(self.loadmaxL_A1)
        self.vboxA1.pack_start(self.loadminL_A1)
        self.vboxA1.pack_start(self.loadpromL_A1)
        self.vboxA1.pack_start(self.loadmaxLong_A1)
        self.vboxA1.pack_start(self.loadminLong_A1)
        self.vboxA1.pack_start(self.loadpromLong_A1)
        self.vboxA1.pack_start(self.posMax_A1)
        self.vboxA1.pack_start(self.posMin_A1)
        self.vboxA1.pack_start(self.posprom_A1)
        #Ficha B1
        self.fichero1.append_page(self.frameB1,tab_label=gtk.Label('Rueda B1'))
        self.frameB1.add(self.vboxB1)
        self.vboxB1.pack_start(self.loadmaxV_B1)
        self.vboxB1.pack_start(self.loadminV_B1)
        self.vboxB1.pack_start(self.loadpromV_B1)
        self.vboxB1.pack_start(self.loadmaxL_B1)
        self.vboxB1.pack_start(self.loadminL_B1)
        self.vboxB1.pack_start(self.loadpromL_B1)
        self.vboxB1.pack_start(self.loadmaxLong_B1)
        self.vboxB1.pack_start(self.loadminLong_B1)
        self.vboxB1.pack_start(self.loadpromLong_B1)
        self.vboxB1.pack_start(self.posMax_B1)
        self.vboxB1.pack_start(self.posMin_B1)
        self.vboxB1.pack_start(self.posprom_B1)
        #Ficha A2
        self.fichero1.append_page(self.frameA2,tab_label=gtk.Label('Rueda A2'))
        self.frameA2.add(self.vboxA2)
        self.vboxA2.pack_start(self.loadmaxV_A2)
        self.vboxA2.pack_start(self.loadminV_A2)
        self.vboxA2.pack_start(self.loadpromV_A2)
        self.vboxA2.pack_start(self.loadmaxL_A2)
        self.vboxA2.pack_start(self.loadminL_A2)
        self.vboxA2.pack_start(self.loadpromL_A2)
        self.vboxA2.pack_start(self.loadmaxLong_A2)
        self.vboxA2.pack_start(self.loadminLong_A2)
        self.vboxA2.pack_start(self.loadpromLong_A2)
        self.vboxA2.pack_start(self.posMax_A2)
        self.vboxA2.pack_start(self.posMin_A2)
        self.vboxA2.pack_start(self.posprom_A2)
        #Ficha B2
        self.fichero1.append_page(self.frameB2,tab_label=gtk.Label('Rueda B2'))
        self.frameB2.add(self.vboxB2)
        self.vboxB2.pack_start(self.loadmaxV_B2)
        self.vboxB2.pack_start(self.loadminV_B2)
        self.vboxB2.pack_start(self.loadpromV_B2)
        self.vboxB2.pack_start(self.loadmaxL_B2)
        self.vboxB2.pack_start(self.loadminL_B2)
        self.vboxB2.pack_start(self.loadpromL_B2)
        self.vboxB2.pack_start(self.loadmaxLong_B2)
        self.vboxB2.pack_start(self.loadminLong_B2)
        self.vboxB2.pack_start(self.loadpromLong_B2)
        self.vboxB2.pack_start(self.posMax_B2)
        self.vboxB2.pack_start(self.posMin_B2)
        self.vboxB2.pack_start(self.posprom_B2)

        self.vbox2.pack_start(self.title3,False,False,1)
        self.vbox2.pack_start(self.fichero2,False,True,5)

        #Ficha 101
        self.fichero2.append_page(self.frame101,tab_label=gtk.Label('Eje Delantero 101'))
        self.frame101.add(self.vbox101)
        self.vbox101.pack_start(self.hunting_101)
        self.vbox101.pack_start(self.trochamax_101)
        self.vbox101.pack_start(self.percep_101)
        #Ficha 102
        self.fichero2.append_page(self.frame102,tab_label=gtk.Label('Eje Posterior 102'))
        self.frame102.add(self.vbox102)
        self.vbox102.pack_start(self.hunting_102)
        self.vbox102.pack_start(self.trochamax_102)
        self.vbox102.pack_start(self.percep_102)
        #------------------------------------
        #Area Derecha
        self.hbox1.pack_start(self.frame_map,True,True,6)
        self.frame_map.add(self.fichero3)
        #Ficha Derecha 101
        self.fichero3.append_page(self.vbox3,tab_label=gtk.Label('Eje Delantero 101'))
        self.vbox3.pack_start(self.canvas101)
        self.vbox3.pack_start(self.hboxg101,False,True,6)
			#A1
        self.hboxg101.pack_start(self.vboxgrafA1)
        self.vboxgrafA1.pack_start(gtk.Label('Rueda A1'))
        self.vboxgrafA1.pack_start(self.checkVLoadA1)
        self.vboxgrafA1.pack_start(self.checkLLoadA1)
        self.vboxgrafA1.pack_start(self.checkLongLoadA1)
        self.vboxgrafA1.pack_start(self.checkPosA1)
			#B1
        self.hboxg101.pack_start(self.vboxgrafB1)
        self.vboxgrafB1.pack_start(gtk.Label('Rueda B1'))
        self.vboxgrafB1.pack_start(self.checkVLoadB1)
        self.vboxgrafB1.pack_start(self.checkLLoadB1)
        self.vboxgrafB1.pack_start(self.checkLongLoadB1)
        self.vboxgrafB1.pack_start(self.checkPosB1)
			#101
        self.hboxg101.pack_start(self.vboxgraf101)
        self.vboxgraf101.pack_start(gtk.Label('Eje 101'))
        self.vboxgraf101.pack_start(self.checkSpeed1)
        #Ficha Izquierda 102
        self.fichero3.append_page(self.vbox4,tab_label=gtk.Label('Eje Posterior 102'))
        self.vbox4.pack_start(self.canvas102)
        self.vbox4.pack_start(self.hboxg102,False,True,6)
        	#A2
        self.hboxg102.pack_start(self.vboxgrafA2)
        self.vboxgrafA2.pack_start(gtk.Label('Rueda A2'))
        self.vboxgrafA2.pack_start(self.checkVLoadA2)
        self.vboxgrafA2.pack_start(self.checkLLoadA2)
        self.vboxgrafA2.pack_start(self.checkLongLoadA2)
        self.vboxgrafA2.pack_start(self.checkPosA2)
			#B1
        self.hboxg102.pack_start(self.vboxgrafB2)
        self.vboxgrafB2.pack_start(gtk.Label('Rueda B2'))
        self.vboxgrafB2.pack_start(self.checkVLoadB2)
        self.vboxgrafB2.pack_start(self.checkLLoadB2)
        self.vboxgrafB2.pack_start(self.checkLongLoadB2)
        self.vboxgrafB2.pack_start(self.checkPosB2)
			#101
        self.hboxg102.pack_start(self.vboxgraf102)
        self.vboxgraf102.pack_start(gtk.Label('Eje 102'))
        self.vboxgraf102.pack_start(self.checkSpeed2)
        #------------------------------------
        #Pie del programa
        self.vbox1.pack_start(self.statusbar,False,True,5)
        self.statusbar.pack_start(self.autor_label,False,False,5) # StatusBar


        self.window.show_all()
        self.window.show()

app = GUI()
anal=0
gtk.main()
