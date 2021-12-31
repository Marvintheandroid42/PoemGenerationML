import os
import tensorflow as tf
import numpy as np
from tensorflow._api.v2 import data

filePath = tf.keras.utils.get_file(
    "shakespeare.txt", "https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt")

text = open(filePath, 'rb').read().decode(encoding='utf-8') 

vocab = sorted(set(text))

# charectar to integer representation (unqiue charecters and integer represetnation dictionary)
char2idx = {u: i for i, u in enumerate(vocab)}
# integer to charectar represetnation
idx2char = np.array(vocab)
# look up the idx representation of the charectars in the text and store it as an array of idx reprentations
textAsInt = np.array([char2idx[char] for char in text])

seqLength = 100
examplesPerEpoch = len(text)//(seqLength+1)

# split idx representations into indidvidual slices
charDataset = tf.data.Dataset.from_tensor_slices(textAsInt)

# Preparing the batches of data
sequences = charDataset.batch(seqLength+1, drop_remainder=True)

# splitting the labels and the input data


def splitInputTarget(chunk):
    inputText = chunk[:-1]
    targetText = chunk[1:]
    return inputText, targetText


# repreating the splitting function for all the sequences in the dataset
dataset = sequences.map(splitInputTarget)

BATCH_SIZE = 64
BUFFER_SIZE = 10000

# Prepare the batches and randomizing it
dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

vocabSize = len(vocab)
embeddingDim = 256
rnnUnits = 1024


def buildModel(vocabSize, embeddingDim, rnnUnits, batchSize):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(
            vocabSize, embeddingDim, batch_input_shape=[batchSize, None]),
        tf.keras.layers.GRU(rnnUnits, return_sequences=True,
                            stateful=True, recurrent_initializer="glorot_uniform"),
        tf.keras.layers.Dense(vocabSize)
    ])
    return model


model = buildModel(vocabSize=len(vocab), embeddingDim=embeddingDim,
                   rnnUnits=rnnUnits, batchSize=BATCH_SIZE)

# Loss Function


def loss(labels, logits):
    return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)


model.compile(optimizer="adam", loss=loss)

checkpointDir = "./training_checkpoint"
checkpointPrefix = os.path.join(checkpointDir, "chkpt_{epoch}")
checkpointCallback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpointPrefix, save_weights_only=True)

EPOCHS = 25

# TRAIN
#history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpointCallback])

# REBUILD FROM EXISTING TRAINING

model = buildModel(vocabSize, embeddingDim, rnnUnits, batchSize=1)

model.load_weights(tf.train.latest_checkpoint(checkpointDir))

model.build(tf.TensorShape([1, None]))

model.summary()

# generating text


def generateText(model, startString):
    # of charectars generated
    numGenerate = 10000
    # convert start string into idx
    inputRep = [char2idx[s] for s in startString]
    inputRep = tf.expand_dims(inputRep, 0)

    txtGenerated = []
    # Handles randomness through a scale factor (smaller means predictable(increase for more randomness))
    tempreture = 1.0
    model.reset_states()
    for i in range(numGenerate):
        predictions = model(inputRep)
        predictions = tf.squeeze(predictions, 0)
        predictions = predictions/tempreture
        predictedID = tf.random.categorical(
            predictions, num_samples=1)[-1, 0].numpy()

        inputRep = tf.expand_dims([predictedID], 0)
        txtGenerated.append(idx2char[predictedID])
    return (startString + "".join(txtGenerated))


prompts = ["ROMEO: ", "PUCK: ", "JULIET: ", "IAGO: ",
           "LEAR: ", "HAMLET: ", "MACBETH:", "hath ", "thou "]

for word in prompts:
    filename = word + ".txt"
    textOut = open(filename, "w")
    textOut.write(generateText(model, startString=word))
    textOut.close()
    print("written")

#print(generateText(model, startString="Romeo: "))
