# -*- coding: utf-8 -*-
from code_hw import ClassifyImages

#Primero se va a construir el vocabulario.
#El archivo se llama "imagedb.zip".
#El numero de iteraciones es 100.
#El nombre del modelo que se va a obtener es "vocabulario_sin_pca.pkl".
#La bandera es False ya que no se aplicara PCA a los vectores sift.
#El ultimo valor es el nombre de el PCA que se debio de haber obtenido anteriormente.
ClassifyImages.generate_bag_of_features("imagedb.zip","vocabulario_sin_pca.pkl","bolsas_caracteristicas_sin_pca.pkl")
