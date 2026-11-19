import folium
import csv

lista_solo_gijon=[]

#Para leer un CSV

c = open("pois.csv")
with c as file:
    r = csv.DictReader(file, delimiter=';')
    campos = (r.fieldnames)
    print (campos)
    print (len(r.fieldnames))
    for row in r:
        print(f"El campo {campos[0]} vale {row[campos[0]]}")
        print(f"En {row[campos[0]]} está {row[campos[1]]} que es {row[campos[2]]}")
        #según voy imprimiendo guardo en una lista los que sean de Gijón
        if row['Ciudad']=='Gijón':
            lista_solo_gijon.append(row)

# Para escribir un CSV

# Escribir los puntos filtrados en un nuevo archivo CSV
with open('pois solo Gijón.csv', 'w', newline='') as csvfile:
    fieldnames = [campos[0],campos[1],campos[2],campos[3],campos[4]]
    csv_dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_dict_writer.writeheader()  # Escribir los encabezados
    csv_dict_writer.writerows(lista_solo_gijon)  # Escribir los puntos filtrados


