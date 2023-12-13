import keras
keras.__version__

from keras import models
from keras import layers
from keras import metrics
from keras import optimizers

import numpy as np
import json
import os
import csv
import pandas as pd
from tensorflow.keras.layers import LSTM
from tensorflow.keras import callbacks
from tensorflow.keras import layers
from numpy import array
from tensorflow.keras.models import Sequential
from keras.layers import Dropout

train_data = "test/train_v2.csv"
test_data = "new_totalCsv/train.csv"

def scheduler(epoch):
  if epoch <= 100:
    return 0.001
  elif epoch <= 150:
    return 0.0001
  elif epoch <= 200:
    return 0.00001
  elif epoch >= 250:
    return 0.000001
  else:
    return 0.0001 * np.exp(0.1 * (50 - epoch))
    
def read_data(path):
  video_data = []
  with open(path, mode='r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
      video_data.append(row)
  return video_data
 
all_data = read_data(train_data)

np.random.shuffle(all_data)
#split_point = len(all_data) // 90
#print("split point:", split_point)
#test_data = all_data[:split_point]
train_data = all_data


x_train = []
y_train = []

for record in train_data:
    x_train.append(record[1:])
    label = int(record[0])
    y_train.append(label)

def train_lstm_model(x_train, y_train):
  x_train = array(x_train)
  x_train = x_train.reshape((len(x_train), 1, len(x_train[0])))
  print("x_train.shape", x_train.shape)
  print(x_train[0])

  y_train = array(y_train)
  print("y_train.shape", y_train.shape)

  # imrpove log: use batch size 16 and add one more lstm layer

  lstm_model = Sequential()
  lstm_model.add(LSTM(16, 
                input_shape=(1, 54),
                return_sequences=True))
  #lstm_model.add(LSTM(8, return_sequences=True))
  lstm_model.add(Dropout(0.2))
  #lstm_model.add(LSTM(8, return_sequences=True))
  #lstm_model.add(Dropout(0.2))
  lstm_model.add(LSTM(8, return_sequences=False))
  lstm_model.add(layers.Dense(1, activation='sigmoid'))
  lstm_model.compile(optimizer='rmsprop',
                loss='binary_crossentropy',
                metrics=['acc',
                        metrics.AUC(), 
                        metrics.FalseNegatives(),
                        metrics.Recall(),
                        metrics.Precision(),
                        metrics.FalseNegatives(),
                        metrics.TrueNegatives(),
                        metrics.FalsePositives(),
                        metrics.TruePositives()])
  lstm_history = lstm_model.fit(x_train, y_train,
                      epochs=500,
                      batch_size=16,
                      validation_split=0.2,
                      callbacks=[callbacks.EarlyStopping(monitor='val_loss', patience=5),
                      callbacks.LearningRateScheduler(scheduler)])
  print("finish training lstm model")
  return lstm_model, lstm_history

lstm_model, lstm_history = train_lstm_model(x_train, y_train)

lstm_model.summary()
lstm_model.save("new5.h5")

# plotting the results

import matplotlib.pyplot as plt

def plotting_training(history):
  # Plot training & validation accuracy values
  plt.plot(history.history['acc'])
  plt.plot(history.history['val_acc'])
  plt.title('Model accuracy')
  plt.ylabel('Accuracy')
  plt.xlabel('Epoch')
  plt.legend(['Train', 'Test'], loc='upper left')
  plt.show()
  # Plot training & validation loss values
  loss = history.history['loss']
  val_loss = history.history['val_loss']
  epochs = range(1, len(loss) + 1)
  plt.figure()
  plt.plot(epochs, loss, 'bo', label="Training loss")
  plt.plot(epochs, val_loss, 'b', label='Validation loss')
  plt.title('Training and validation loss')
  plt.xlabel('epoch', fontsize=10)
  plt.ylabel('loss', fontsize=10)
  plt.ylim(0.0,0.5)
  plt.legend()
  plt.show()

plotting_training(lstm_history)

# test 
# for lstm
test_data = read_data(test_data)
x_test = []
y_test = []

for record in test_data:
  x_test.append(record[1:])
  label = int(record[0])
  y_test.append(label) 

x_test = array(x_test)
x_test = x_test.reshape((len(x_test), 1, len(x_test[0])))

y_test = array(y_test)

test_score = lstm_model.evaluate(x_test, y_test)
print(test_score)        


