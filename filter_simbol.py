import numpy as np
symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"

sentence = "ini-= adalah percobaan ? * () menghapus tanda baca pada ^^* kalimat"

for i in symbols:
    #print(sentence)
    sentence = np.char.replace(sentence, i, ' ')

print(sentence) 
