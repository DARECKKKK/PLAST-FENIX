from configparser import ConfigParser
def set(filename="database.ini",section="postgresql"):    
    parser=ConfigParser()
    parser.read(filename)
    diccionario={}
    if parser.has_section(section):
        gatos=parser.items(section)
        for gato in gatos:
            diccionario[gato[0]]=gato[1]                        
    return diccionario
  


