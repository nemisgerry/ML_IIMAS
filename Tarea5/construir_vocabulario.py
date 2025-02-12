# -*- coding: utf-8 -*-
from code_hw import ClassifyImages

#Primero se va a construir el vocabulario.
#El archivo se llama "imagedb.zip".
#El numero de iteraciones es 100.
#El nombre del modelo que se va a obtener es "vocabulario_sin_pca.pkl".
#La bandera es False ya que no se aplicara PCA a los vectores sift.
#El ultimo valor es el nombre de el PCA que se debio de haber obtenido anteriormente.
ClassifyImages.construct_vocabulary_sift("imagedb.zip",100,"vocabulario_sin_pca.pkl",False,"pca_sift.pkl")
