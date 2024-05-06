import funciones.globales as gf
import modules.corefiles as cf
import funciones.citas as ct
import main
def menucitas(op : int):
    title ="""
    *******************************
    *   ADMINISTRACION DE CITAS   *
    *******************************
    """
    menucitasop= '1.Agendar cita\n2.buscar cita\n3.Editar cita\n4.Eliminar cita\n5.Menu principal'
    gf.borar_pantalla()
    if (op != 5):
       print(title)
       print(menucitasop)
       try:
           op= int(input(": "))
       except ValueError:
           print("opcion invalida")
           gf.pausar_pantalla
           menucitasop(0)
       else:
           match(op):
               case 1:
                   ct.newcita()
               case 2:
                   ct.SearchData    
               case 3:
                   ct.ModifyData()
               case 4:
                   pass
               case 5:
                   main.mainmenu(0)
               case _:
                   print("la opcion ingreseda no esta displonible")
                   gf.pausar_pantalla()   
                
