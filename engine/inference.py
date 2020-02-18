import numpy as np
from tensorflow.keras.models import load_model

model = load_model("./rps3_2.h5")

to_num = {'R':1, 'P':2, 'S':3}
to_char = {1:'R', 2:'P', 3:'S'}
c_moves = {'R':'P', 'P':'S', 'S':'R'}
run = True
p_move = ''
c_move = 'R'
x_test = []
y_test = []
x_temp = []
flag = 0
p_score = 0
c_score = 0

def check(p_move, c_move):
  global flag, run, p_score, c_score
  if p_move == "end":
    run = False
  if p_move == 'R':
    if c_move == 'P':
      c_score += 1
      flag = 0
      print(f'Your Loss\nYour Score:Computer Score :: {p_score}:{c_score}')
    elif c_move == 'S':
      p_score += 1
      print(f'You Won!!\nYour Score:Computer Score :: {p_score}:{c_score}')
      flag += 1
    else:
      flag += 1
      print("Draw")
    return 1

  if p_move == 'P':
    if c_move == 'S':
      c_score += 1
      flag = 0
      print(f'Your Loss\nYour Score:Computer Score :: {p_score}:{c_score}')
    elif c_move == 'R':
      p_score += 1
      print(f'You Won!!\nYour Score:Computer Score :: {p_score}:{c_score}')
      flag += 1
    else:
      flag += 1
      print("Draw")
    return 1

  if p_move == 'S':
    if c_move == 'R':
      c_score += 1
      flag = 0
      print(f'Your Loss\nYour Score:Computer Score :: {p_score}:{c_score}')
    elif c_move == 'P':
      p_score += 1
      print(f'You Won!!\nYour Score:Computer Score :: {p_score}:{c_score}')
      flag += 1
    else:
      flag += 1
      print("Draw")
    return 1
  return -1

while run:
  p_move = input('Enter your move: ')
  if check(p_move, c_move) == -1:
    print("Wrong input, Use R or P or S")
  else:
    if flag >= 4:
      # print('Change in Strategy Detected')
      x_temp = []
      flag = 0
    elif run == False:
      break
    if len(x_temp) >= 18:
      x_temp.pop(0)
      x_temp.pop(0)
    x_temp.append(to_num[p_move])
    x_temp.append(to_num[c_move])
    x_test = []
    for i in x_temp:
      x_test.append(i)
    pad_len = 18-len(x_test)
    for i in range(pad_len):
      x_test.append(0)
    pred_move = to_char[model.predict_classes(np.array([x_test], dtype='float32'))[0]]
    c_move = c_moves[pred_move]
