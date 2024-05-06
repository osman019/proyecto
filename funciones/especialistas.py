import os 
import json
import funciones.globalesES as gfES
import modules.corefileES as cf
import ui.uiespecialistas as uie

def newespecialista():
    title =  """
    ***************************
    *REGISTRO DE ESPECIALISTAS*
    ***************************
    """
    gfES.borar_pantalla()
    print(title)
    identificacion = input("ingrese numero de identificacion : ")
    nomb_apell = input("ingrese su  nombre y apellido : ")
    corre_ele = input("ingrese su correo eletronico : ")
    num_consul = input("ingrese numero de consultorio : ")
    hora_atencion = input("ingrese el horario del medico : ")
    especialista = {'identificacion': identificacion,
               'nombre y apellido': nomb_apell,
               'numero de consultorio':num_consul,
               'horario de atencion': hora_atencion,
               'correo eletronico': corre_ele,}
    
    cf.AddData('dataespecialista',identificacion,especialista)
    gfES.centromedico.get('dataespecialista').update({identificacion:especialista})
    if(bool(input(
       'Desea registrar otro especialista S(Si) o Enter(No): '))):
        newespecialista()
    else:
        uie.Menuespecialistas(0)

def  SearchData():
    input('ingrese la identificacion del especialista : ')
    data= gfES.centromedico.get('dataespecialista')
    print(data)
    return data

def ModifyData():
   dataespecialista= SearchData()
   if dataespecialista:
      print("Datos actuales del especialista:")
      dataespecialista = ['nombre y apellidos', 'correo eletronico', 'numero de consultorio', 'hora de atencion']
      for key in dataespecialista:
         if bool(input(f"Desea modificar {key}? (Sí/Si o Enter para No): ")):
               new_value = input(f"Ingrese el nuevo valor para {key}: ")
               dataespecialista = new_value

      gfES.centromedico.get('dataespecialista').update({dataespecialista:'identificacion'})
      cf.UpdateFile(gfES.centromedico)
      print("Datos del paciente actualizados correctamente.")
   else:
        print("No se encontró ningún paciente con la identificación proporcionada.")
def removeespecialista(param):
   data = list(*param)
   identificacion = int(input("ingrese la identificacion del especialista que desea eliminar : "))
   if identificacion in data:
      confirmacion = input("¿esta seguro que  desea eliminar especialista? enter(si) n (no): ")
      if confirmacion.lower()== 'enter':
       del data [identificacion]
      print("usuario eliminado correctamentte")
   else:
      print("usuario no encontrado.")


