
import funciones.globales as gf
import modules.corefiles as cf
import main
import funciones.medicos as st


def Menumedicos(op : int):
    title = """
    ************************
    * MODULO ADMIN MEDICOS *
    ************************
    """
    MenumedicosOp = 'Agregar\n2. Editar\n3. Eliminar\n4. salir'
    gf.borar_pantalla()
    if(op != 4):
      print(title)
      print(MenumedicosOp)
      try:
       op = int(input(":)"))
      except ValueError:
        print("opcion invalida")
        gf.pausar_pantalla()
        Menumedicos(0)
      else: 
        match (op):
          case 1: 
            st.newmedico()
          case 2:
            st.MofifyData()
          case 3:
            pass
          case 4: 
            main.mainmenu(0) 
          case _:
                print("la opcion ingresada no esta disponible en las opciones")
                gf.pausar_pantalla


        











