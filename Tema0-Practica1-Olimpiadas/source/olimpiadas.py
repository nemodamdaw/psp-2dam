import csv
from collections import namedtuple
Atleta = namedtuple('Atleta', 'nombre,edad,pais,peso')
#pepe,20,italia,87.3
def leer_olimpiadas(nombre):
    registros=[]
    with open(nombre, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for linea in lector:
            nombre = linea[0]
            edad = int(linea[1])
            pais = linea[2]
            peso = float(linea[3])
            tupla=Atleta(nombre,edad,pais,peso)
            registros.append(tupla)
    return registros

def edad_media(registros):
    res=0.0
    for r in registros:
        res+=r.edad
    return res/len(registros)

# private List<Atleta> registros;
# Map<String,Integer> numAtletasPorPais(){
#     Map<String,Integer> d= new HashMap<>();
#     for(Atleta r: registros){
#         String clave=r.pais();
#         if(d.containsKey(clave)){
#             d.put(clave,d.get(clave)+1)
#         }
#         else{
#             d.put(clave,1);
#         }
#     }
#     return d;
# }

def num_atletas_por_pais(registros):
    d={}
    for r in registros:
        clave = r.pais
        if clave in d:
            d[clave]+=1
        else:
            d[clave]=1
    return d


# def nombre_atletas_por_pais(registros):
#     """
#     metodo que devuelve un diccionario cuyas
#     claves son los paises y su valor una
#     lista con los nombres de cada atleta de 
#     ese pais
#     """
#     d={}
#     for r in registros:
#         clave = r.pais
#         if clave in d:
#             d[clave].append(r.nombre)
#         else:
#             d[clave]=[r.nombre]
#     return d
    
def nombre_atletas_por_pais(registros):
    """
    metodo que devuelve un diccionario cuyas
    claves son los paises y su valor una
    lista con los nombres de cada atleta de 
    ese pais
    """
    d={}
    for r in registros:
        clave = r.pais
        if clave in d:
            d[clave]+=[r.nombre]
        else:
            d[clave]=[r.nombre]


    return d

def atleta_mayor_peso(registros):
    return max(registros, key= lambda t:t.peso).nombre

# def pais_mayor_peso_medio(registros):
#     d1={}
#     for r in registros:
#         clave=r.pais
#         if clave in d1:
#             d1[clave]+=r.peso
#         else:
#             d1[clave]=r.peso
#     d2=num_atletas_por_pais(registros)
#     d3={}
#     for clave in d1:
#         d3[clave]=d1[clave]/d2[clave]

#     return max(d3.items(), key= lambda t:t[1])[0]

def pais_mayor_peso_medio(registros):
    d1={}
    for r in registros:
        clave=r.pais
        if clave in d1:
            d1[clave]+=[r.peso]
        else:
            d1[clave]=[r.peso]

    d2={}
    for clave in d1:
        d2[clave]= sum(d1[clave])/len(d1[clave])
   
    return max(d2.items(), key= lambda t:t[1])[0]

#[2,0,3,7]
# def metodozip(registros):
#     lis=[]
#     registros=sorted(registros,key=lambda t:t.edad)
#     for a,b in zip(registros,registros[1:]):
#         lis.append(b.edad-a.edad)

#     return max(lis)

def metodozip(registros):
    
    registros=sorted(registros,key=lambda t:t.edad)
    lis=[b.edad-a.edad for a,b in zip(registros,registros[1:])]


    return max(lis)