import json 
import os 

MY_DATABASEES = 'data/especialistas.json'

def NewFile(*param):
     with open(MY_DATABASEES,"w") as wf:
      json.dump(param[0],wf,indent=4)

def UpdateFile(*param):
   with open(MY_DATABASEES,'w') as fw:
      json.dump(param[0],fw,indent=5)

def AddData(*param):
   data = list(param)
   with open(MY_DATABASEES,"r+") as rwf:
      data_file=json.load(rwf)
      if (len(param) > 1):
         data_file[data[0]].update({data[1]:data[2]})
      else:
         data_file.update([param[0]])
      # data_file[llavePrincipal].update({codigo:info})
      rwf.seek(0)
      json.dump(data_file,rwf,indent=4)  

def ReadFile():
   with open(MY_DATABASEES,"r") as rf:
      return json.load(rf)

def checkFile(*param):
   data = list(param)
   if(os.path.isfile(MY_DATABASEES)):
      if(len(param)):
         data[0].update(ReadFile())
      else:
         if(len(param)):
            NewFile(data[0])         
                         