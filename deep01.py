# principais
import cv2
import os 
import random
import numpy as np
import matplotlib.pyplot as plt

# importando o tensorflow - funcinal API
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Layer, Input, Dense, Conv2D, MaxPooling2D, Flatten

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

#estrutura das pastas
POS_PATH = os.path.join('dataset', 'positive')
NEG_PATH = os.path.join('dataset', 'negative')
ANC_PATH = os.path.join('dataset', 'anchor')

#criando as pastas
os.makedirs(POS_PATH, exist_ok=True)
os.makedirs(NEG_PATH, exist_ok=True)
os.makedirs(ANC_PATH, exist_ok=True)