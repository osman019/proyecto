import os 
import json
import funciones.globalesCT as gfCT
import modules.corefileCT as cf
import ui.uicitas as uict
def newcita():
    title = """
    ******************
    *  AGENDAR CITAS *
    ******************
    """
    gfCT.borar_pantalla()
    print(title)
    print("tenga encuenta que las especialidades que tenemos disponibles son: \n*Pediatria\n*Endocrinologia\n*Ginecologia\n*Dermatologia\n*Optometria ")
    identificacion = input("ingrese numero de identificacion : ")
    nombre_y_apellido = input("ingrese nombre y apellido : ")   
    corre_eletronico = input("ingrese el correo eletronico : ")
    ingrese_fecha = input("ingrese fecha : " )
    especialidad = input("ingrese el tipo de cita : ")
    cita = {'identificacion': identificacion,
            'especialidad': especialidad,
            'nombre y apellido': nombre_y_apellido,
            'correo eletronico':corre_eletronico,
            'ingrese fecha':ingrese_fecha,}
    cf.AddData('datacitas',identificacion,cita)
    gfCT.centromedico.get('datacitas').update({identificacion:cita})
    if(bool(input(' desea agendar otra cita si(si)0 enter (no)'))):
        newcita()
    else:
        uict.menucitas(0)
def SearchData():
    input('ingrese la identificacion del paciente: ')
    data=gfCT.centromedico.get('datacitas')
    return data 

def ModifyData():
   datacitas = SearchData()
   if datacitas:
      print("Datos actuales del paciente:")
      datacitas = ['nombre y apellidos','identificacion', 'correo electronico', 'fechas', 'especialista']
      for key in datacitas:
         if bool(input(f"Desea modificar {key}? (Sí/Si o Enter para No): ")):
               new_value = input(f"Ingrese el nuevo valor para {key}: ")
               datacitas = new_value

      gfCT.centromedico.get('datacitas').update({datacitas:'datacitas'})
      cf.UpdateFile(gfCT.centromedico)
      print("Datos de la cita actualizados correctamente.")
   else:
        print("No se encontró ningún paciente con la identificación proporcionada.")
        
