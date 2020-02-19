import numpy as np
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.keras.models import load_model

model = load_model(sys.argv[1])

to_num = {'R': 1, 'P': 2, 'S': 3}
to_char = {1: 'R', 2: 'P', 3: 'S'}
c_moves = {'R': 'P', 'P': 'S', 'S': 'R'}

def inference(x_temp):
    x_test = []
    for i in x_temp[::2]:
        x_test.append(i)
    pad_len = 18-len(x_test)
    for i in range(pad_len):
        x_test.append(0)
    print(x_test)
    pred_move = to_char[model.predict_classes(
        np.array([x_test], dtype='float32'))[0]]
    c_move = c_moves[pred_move]
    return c_move


print(inference(sys.argv[2]))
sys.stdout.flush()
