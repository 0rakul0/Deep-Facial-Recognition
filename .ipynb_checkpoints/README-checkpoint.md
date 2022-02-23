# Deep Facial Recognition
 uso de deep learn para reconhecimento facial

# instalação das dependencias
    - caso tenha uma placa nvida, instale o cuda-toolkit
   pip install tensorflow tensorflow-gpu opencv-python matplotlib 

   - caso use uma placa readom, instale o tire o tensorflow-gpu
   pip install tensorflow opencv-python matplotlib keras

# camadas do tensorFlow
# utilizando GPU
    - Evite erros OOM definindo o crescimento do consumo de memória da GPU
    - Para melhorar a performance, utilize o tensorflow-gpu
    """py
        gpus = tf.config.experimental.list_physical_devices('GPU')
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    """
# Criando a pasta DATA