from pathlib import Path
import tensorflow as tf
import numpy as np
from pyarabic import araby
from keras.utils import pad_sequences

BASE_DIR = Path(__file__).resolve(strict=True).parent
#
with open(f"{BASE_DIR}/poetry_model.h5", "rb") as f:
    model = tf.keras.models.load_model(f)

label2name = ['saree', 'kamel', 'mutakareb', 'mutadarak', 'munsareh', 'madeed',
              'mujtath', 'ramal', 'baseet', 'khafeef', 'taweel', 'wafer', 'hazaj', 'rajaz']

maxlen = 100
char2idx = {' ': 1, '#': 2, 'ء': 3, 'آ': 4, 'أ': 5, 'ؤ': 6, 'إ': 7, 'ئ': 8, 'ا': 9, 'ب': 10,
            'ة': 11, 'ت': 12, 'ث': 13, 'ج': 14, 'ح': 15, 'خ': 16, 'د': 17, 'ذ': 18, 'ر': 19, 'ز': 20,
            'س': 21, 'ش': 22, 'ص': 23, 'ض': 24, 'ط': 25, 'ظ': 26, 'ع': 27, 'غ': 28, 'ف': 29, 'ق': 30,
            'ك': 31, 'ل': 32, 'م': 33, 'ن': 34, 'ه': 35, 'و': 36, 'ى': 37, 'ي': 38}


def classify(sentence):
    #   sentence = process_review(sentence)
    sentence = araby.strip_tashkeel(sentence)
    sequence = [char2idx[char] for char in sentence]
    sequence = pad_sequences([sequence], maxlen=maxlen, padding='post', value=0)

    pred = model.predict(sequence)[0]
    return label2name[np.argmax(pred, 0).astype('int')], np.max(pred)
