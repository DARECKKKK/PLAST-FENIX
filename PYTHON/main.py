import psycopg2
import pandas as pd
from  configsql import set 

def connect():
    connection = None
    try:
        params = set()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)                             
        consulta1=pd.read_sql_query(sql=''' SELECT *  FROM ventas AS v
                                            JOIN productos AS p ON p.id_producto=v.id_producto
                                            JOIN personas AS pe ON pe.idclientes=v.idclientes
                                            JOIN distrito AS d ON d.iddistrito=pe.iddistrito
                                            JOIN provincia AS pro ON pro.idprovincia=d.idprovincia''',con=connection)
        consulta2=pd.read_sql_query(sql=''' SELECT *  FROM produccion AS pr
                                            JOIN productos AS p ON p.id_producto=pr.id_producto''',con=connection)   
                                                  
        with pd.ExcelWriter("powerbi.xlsx", engine="openpyxl") as writer:
            consulta1.to_excel(writer, sheet_name="ventas", index=False)
            consulta2.to_excel(writer, sheet_name="produccion", index=False)
        print("Exportación completada")                                                                  
        return consulta1,consulta2                                                                                
    except Exception as e:
        print("Error:", e) 

if __name__ == '__main__':
    gato = connect()

    
    
        


    
 
           
        
                   