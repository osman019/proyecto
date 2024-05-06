import modules.corefiles as cf
import funciones.globales as gf
import funciones.pacientes as fp
import main 
def MenuPacinetes(op : int):
    title = """
    ***************************
    * MODULO AMIND PACIENTES  *
    ***************************
    """
    MenuPacinetesop = '1.Buscar paciente\n2.agregar pacientes\n3.editar informacion del paciente\n4.Menu principal '
    gf.borar_pantalla()
    if (op != 4):
     print(title)
     print(MenuPacinetesop)
    try:
       op = int(input(":)"))
    except ValueError:
        print("opcion invalida")
        gf.pausar_pantalla()
        MenuPacinetesop(0)
    else: 
        match (op):
           case 1: 
              fp.SearchData()
           case 2: 
            fp.newpaciente()
           case 3:
            fp.ModifyData()
           case 4: 
            main.mainmenu(0)
           case _:
            print("la opcion ingresada no estadisplonible en las opciones")
            gf.pausar_pantalla
            