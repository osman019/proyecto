import funciones.globales as gf
import modules.corefiles as cf
import main
import funciones.especialistas as st

def Menuespecialistas(op : int):
    title = """
    **********************************
    * ADMINISTRACION DE ESPECIALISTAS*
    **********************************
    """
    MenumedicosOp = '1.buscar especialista \n2.Agregar especialista\n3.Editar informacion de especialista\n4.Eliminar especialista\n5.Menu principal'
    gf.borar_pantalla()
    if(op != 5):
      print(title)
      print(MenumedicosOp)
      try:
           op = int(input(":)"))
      except ValueError:
        print("opcion invalida")
        gf.pausar_pantalla()
        MenumedicosOp(0)
      else: 
        match (op):
          case 1:
            st.SearchData()
          case 2: 
            st.newespecialista()
          case 3:
            st.ModifyData()
          case 4:
            st.removeespecialista()
          case 5: 
            main.mainmenu(0) 
          case _:
                print("la opcion ingresada no esta disponible en las opciones")
                gf.pausar_pantalla


        











