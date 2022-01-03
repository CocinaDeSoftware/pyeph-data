# PyEPH Data

Almacenamiento estandarizado de las bases de microdatos de las Encuesta Permanante de Hogares publicadas por INDEC y el resto de las bases de datos necesarias para el tratamiento de las EPH. 

## Descripcion

En este repositorio se albergan:
        - Las bases de datos de las EPH de 1996 en adelante
        - Diccionario de aglomerados y regiones de las EPH
        - La serie de tiempo de la Canasta Básica Alimentaria (CBA) y Canasta Básica Total (CBT) regional
        - Los valores de adulto equivalente por sexo y edad
        - La tabla de Clasificación de Actividades Económicas para Encuestas Sociodemográficas (CAES)
        - La tabla de Clasificación Nacional de Ocupaciones (CNO)

Desde 1996 hasta 2018 las bases fueron solicitadas con éxito y almacenadas por Instituto Humai
Desde 2019 en adelante fueron obtenidas desde el sitio oficial de INDEC estandarizando el nombre para la facil obtencion y manipulacion de los datos en la libreria pyeph

## Especificaciones de nombre

eph_{base_type}_{year}_{freq}_{period}.csv 