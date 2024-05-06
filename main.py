import modules.corefiles as cf
import modules.corefileCT as mdCT
import modules.corefileES as mdES
import funciones.globales as gf
import ui.uiespecialistas as uie
import ui.uicitas as uict
import ui.uipacientes as  up

def mainmenu(op):
    title = """
    ***************************
    *        BIENVENIDO       *
    *     AL CENTRO MEDICO    *    
    ***************************
    
    ELIGA UNA OPCION DISPLONIBLE
    """
    
    mainmenuop = "1.gestion de especialistas\n2.gestion de pacientes\n3.gestion citas \n4.salir"
    gf.borar_pantalla
    if (op !=3):
     print(title)
     print(mainmenuop)
     try:
        opcion = int(input(':)'))
     except ValueError:
        print('error en la opcion ingresada ')
        gf.pausar_pantalla()
        mainmenu(0)
     else:
        match(opcion):
           case 1:
              uie.Menuespecialistas(0)
           case 2:
               up.MenuPacinetes(0)
           case 3:
               uict.menucitas(0)
           case 4:  
              print("hasta luego") 
           case _:
              print('opcion ingresada no esta en el menu de opciones')
              gf.pausar_pantalla
              mainmenu(0)


if __name__ == '__main__':
   cf.MY_DATABASE= 'data/pacientes.json'
   mdCT.MY_DATABASECT= 'data/citas.json'
   mdES.MY_DATABASEES= 'data/especialistas.json'
   cf.checkFile(gf.centromedico)
   mainmenu(0)              

