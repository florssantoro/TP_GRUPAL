# -*- coding: utf-8 -*-
"""TP GRUPO 2 - PENSAMIENTO COMPUTACIONAL

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bil7eNv8zbveQwj9le6uf9XbwI_y5aT9
"""

# TRABAJO PRÁCTICO - GRUPO 2
# Autores: Florencia Santoro, Paulina Alonso, Isabella Mastronardi y Agustina Invierno
# Materia: Pensamiento Computacional - TIC 2025
# Profesor: Daniel J. Feijó

#Usamos el IMPORT para llamar a una fincion ya creada (random) y poder utilizarlo luego en nuestro programa como una funcion ya hecha
import random

# DEFINICIÓN DE FUNCIONES (Puntos 1 a 8)

def crear_identificador(cadena_adn):
#Punto 1: Recibe una cadena de ADN y le modifica menos de 4 caracteres, entre 1 a 3 letras aleatorias para simular un identificador.

  lista_adn = list(cadena_adn)
  cantidad_de_cambios = random.randint (1,3)
  posiciones_a_cambiar = random.sample (range(len(lista_adn)), cantidad_de_cambios)
  #guardamos las posiciones en un rango llamado letra para modificarlas por otras
  for letra in posiciones_a_cambiar:
    letra_original = lista_adn[letra]
    opciones = ['A', 'T', 'G', 'C']
    opciones.remove(letra_original)
    nueva_letra = random.choice(opciones)
    lista_adn[letra] = nueva_letra
  return "".join(lista_adn)

def crear_muestra(identificador):
#Punto 2: Recibe un identificador y lo modifica entre 5 y 10 letras aleatorias para simular una muestra ya bastante afectada por el ambiente

  lista_adn = list(identificador)
  cantidad_de_cambios = random.randint (5,10)
  posiciones_a_cambiar = random.sample (range(len(lista_adn)), cantidad_de_cambios)
  #otra vez guardamos las letras modificadas en otro rango para cambiarlas por otras
  for letra in posiciones_a_cambiar:
    letra_original = lista_adn[letra]
    opciones = ['A', 'T', 'G', 'C']
    opciones.remove(letra_original)
    nueva_letra = random.choice(opciones)
    lista_adn[letra] = nueva_letra
  return "".join(lista_adn)

def crear_muestras(muestra_inicial):
#Punto 3: A partir de la primer muestra creada, genera 19 muestras mas aplicando repetidamente la función de creación.

    muestras = [muestra_inicial]
    #volvemos a guardar los datos cambiados
    for _ in range(19):
        nuevas_muestra = crear_muestra(muestras[-1]) #itera la funcion siempre a partir de la anterior
        muestras.append(nuevas_muestra)
    return muestras

def corregir_letras(muestra, identificador):
#Punto 4 (parte de la reconstrucción): Corrige una muestra comparándola letra por letra con el identificador.

  muestra_corregida = list(muestra)
  for letra in range(len(muestra)):
    if muestra[letra] != identificador[letra]:
      opciones = ['A', 'T', 'G', 'C']
      opciones.remove(muestra[letra])
      nueva_letra = random.choice(opciones)
      muestra_corregida[letra] = nueva_letra
    else:
      muestra_corregida[letra] = identificador[letra]
  return "".join(muestra_corregida)

def reconstruccion_identificador(muestra_actual, identificador):
#Punto 4: Reconstruye el identificador intentando corregir sucesivamente la muestra.

  muestra_corregida = crear_muestra(muestra_actual)
  intentos = 1
  print(f"\nINTENTO {intentos:2d}: {muestra_corregida}")
  while muestra_corregida != identificador:
    muestra_corregida = corregir_letras(muestra_corregida, identificador)
    intentos += 1
    print(f"INTENTO {intentos:2d}: {muestra_corregida}")
  print("\nSE REALIZARON", intentos, "INTENTOS")
  print("SU IDENTIFICADOR ERA:    ", identificador)
  print("SU RECONSTRUCCION ES:    ", muestra_corregida)
  return muestra_corregida

def crear_pares(cadena_adn):
#Punto 6: Devuelve la cadena complementaria de pares de ADN.

  pares = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
  cadena_pares = ""
  for letra in cadena_adn:
    cadena_pares += pares[letra]
  return cadena_pares

def comparar_coincidencias (cadena_adn1, cadena_adn2):
#Punto 7: Calcula el porcentaje de letras iguales entre dos cadenas del mismo largo.

  coicidencias = 0
  for letra in range(len(cadena_adn1)):
    if cadena_adn1[letra] == cadena_adn2[letra]:
      coicidencias += 1
  porcentaje_coincidencia = (coicidencias / len(cadena_adn1)) * 100
  return porcentaje_coincidencia

def comparar_muestras(muestra, especies):
#Punto 8: Devuelve la especie con mayor porcentaje de coincidencia con la muestra.

  mejor_coincidencia = 0
  especie_mas_parecida = ""

  for especie, cadena_adn_especie in especies.items():
    porcentaje_coincidencia = comparar_coincidencias(cadena_adn, cadena_adn_especie)
    if porcentaje_coincidencia > mejor_coincidencia:
      mejor_coincidencia = porcentaje_coincidencia
      especie_mas_parecida = especie
      return especie_mas_parecida
    else:
      return "No se encontró especie con coincidencia válida"

def porcentajes_muestras(muestra, especies):
#Punto 8 (extra): Devuelve un diccionario con el porcentaje de coincidencia para cada especie.

    resultados = {}
    for especie, adn in especies.items():
        if len(adn) < len(muestra):
            resultados[especie] = 0
        else:
            adn_recortado = adn[:len(muestra)]
            resultados[especie] = comparar_coincidencias(muestra, adn_recortado)
    return resultados

# VARIABLES GLOBALES Y EJECUCIÓN DEL PROGRAMA

# Diccionario de especies (cada valor es una cadena larga de ADN modelo)
especie = {
    "Tortuga": "ATTCGCACAATTCCTATCCTATTCGCACAATTCCTATCCTATTCGCACAATTCCTATCCTATTCGCACAATTCCTATCCTATTCGCACAATTCCTATCCT" * 1000,
    "Perro":   "ATGCTAGCTAGCTACCGTAAATGCTAGCTAGCTACCGTAAATGCTAGCTAGCTACCGTAAATGCTAGCTAGCTACCGTAAATGCTAGCTAGCTACCGTAA" * 1000,
    "Gato":    "TACGATCGATCGTACGATCGTACGATCGATCGTACGATCGTACGATCGATCGTACGATCGTACGATCGATCGTACGATCGTACGATCGATCGTACGATCG" * 1000,
    "Vaca":    "GGCTAACGTAGCTAGGCTAAGGCTAACGTAGCTAGGCTAAGGCTAACGTAGCTAGGCTAAGGCTAACGTAGCTAGGCTAAGGCTAACGTAGCTAGGCTAA" * 1000,
    "Caballo": "CTAGGCTAACCGTAGCTAGCCTAGGCTAACCGTAGCTAGCCTAGGCTAACCGTAGCTAGCCTAGGCTAACCGTAGCTAGCCTAGGCTAACCGTAGCTAGC" * 1000,
    "Cerdo":   "AATTCCGGTTCCAATTGGCCAATTCCGGTTCCAATTGGCCAATTCCGGTTCCAATTGGCCAATTCCGGTTCCAATTGGCCAATTCCGGTTCCAATTGGCC" * 1000,
    "Oveja":   "CCTAGGTAACCTAGGTAACCCCTAGGTAACCTAGGTAACCCCTAGGTAACCTAGGTAACCCCTAGGTAACCTAGGTAACCCCTAGGTAACCTAGGTAACC" * 1000,
    "Conejo":  "GGAATTCCGGAATTCCGGAAGGAATTCCGGAATTCCGGAAGGAATTCCGGAATTCCGGAAGGAATTCCGGAATTCCGGAAGGAATTCCGGAATTCCGGAA" * 1000,
    "Gallina": "TAGCGATAGCGATAGCGATATAGCGATAGCGATAGCGATATAGCGATAGCGATAGCGATATAGCGATAGCGATAGCGATATAGCGATAGCGATAGCGATA" * 1000,
    "Pato":    "GCTAGCTAGGATCCGATCGAGCTAGCTAGGATCCGATCGAGCTAGCTAGGATCCGATCGAGCTAGCTAGGATCCGATCGAGCTAGCTAGGATCCGATCGA" * 1000,
    "Paloma":  "AACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCC" * 1000,
    "Ganso":   "TTGGAACCTTGGAACCTTGGTTGGAACCTTGGAACCTTGGTTGGAACCTTGGAACCTTGGTTGGAACCTTGGAACCTTGGTTGGAACCTTGGAACCTTGG" * 1000,
    "Burro":   "CGATTCGGAACCGGATTCCACGATTCGGAACCGGATTCCACGATTCGGAACCGGATTCCACGATTCGGAACCGGATTCCACGATTCGGAACCGGATTCCA" * 1000,
    "Canario": "GGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCAT" * 1000
}

# Ingreso del ADN original y aplicacion de primeras fuciones
cadena_adn = input("INGRESE SU CADENA DE ADN: ")
identificador = crear_identificador(cadena_adn)
muestra = crear_muestra(identificador)
muestras = crear_muestras(muestra)

# Mostrar muestras
print("\nIDENTIFICADOR CREADO: ", identificador)
print("\nPRIMERA MUESTRA:     ", muestra)
print("\nLISTADO DE MUESTRAS:")
for i, m in enumerate(muestras, start=1):
    print(f"MUESTRA {i:2d}: {m}")

# Reconstrucción del identificador
print("\n\nINTENTOS DE RECONSTRUIR EL IDENTIFICADOR")
reconstruccion_identificador(cadena_adn, identificador)

# Mostrar pares
pares = crear_pares(cadena_adn)
print("\nCADENA DE PARES:")
print("CADENA ORIGINAL:", cadena_adn)
print("CADENA DE PARES:", pares)

# Porcentaje de coincidencia entre muestra e identificador (EJEMPLO DEL PUNTO 7)
porcentaje = comparar_coincidencias(identificador, muestra)
print("\nPORCENTAJE DE COINCIDENCIA: ", round(porcentaje, 2), "%")

# Especie más parecida y todos los porcentajes segun cada especie
especie_mas_parecida = comparar_muestras(cadena_adn, especie)
print("\n\nESPECIE MAS PARECIDA: ", especie_mas_parecida)

print("\nPORCENTAJE POR ESPECIE:")
porcentajes = porcentajes_muestras(cadena_adn, especie)
for especie, porc in porcentajes.items():
    print(f"{especie}: {porc:.2f}%")