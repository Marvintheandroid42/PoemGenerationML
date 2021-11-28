import os
import tensorflow as tf
import numpy as np
from tensorflow._api.v2 import data

# remember to change the file in which the training is stored in '

text = open("otherPoemStorage.txt", 'rb').read().decode(
    encoding='UTF-8', errors='ignore')

vocab = sorted(set(text))

print(vocab)

char2idx = {u: i for i, u in enumerate(vocab)}

idx2char = np.array(vocab)

textAsInt = np.array([char2idx[char] for char in text])

seqLength = 100
examplesPerEpoch = len(text)//(seqLength+1)

charDataset = tf.data.Dataset.from_tensor_slices(textAsInt)

sequences = charDataset.batch(seqLength+1, drop_remainder=True)


def splitInputTarget(chunk):
    inputText = chunk[:-1]
    targetText = chunk[1:]
    return inputText, targetText


dataset = sequences.map(splitInputTarget)

BATCH_SIZE = 64
BUFFER_SIZE = 10000

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


def loss(labels, logits):
    return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)


model.compile(optimizer="adam", loss=loss)

checkpointDir = "./training_checkpoint_milton"
checkpointPrefix = os.path.join(checkpointDir, "chkpt_{epoch}")
checkpointCallback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpointPrefix, save_weights_only=True)

EPOCHS = 25

#history = model.fit(dataset, epochs=EPOCHS, callbacks=[checkpointCallback])

model = buildModel(vocabSize, embeddingDim, rnnUnits, batchSize=1)

model.load_weights(tf.train.latest_checkpoint(checkpointDir))

model.build(tf.TensorShape([1, None]))

model.summary()


def generateText(model, startString):
    # of charectars generated
    numGenerate = 100
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


word = "the"
fileOut = open("Miltongen.txt", "w")
time = 1000
while time != 0:
    print(time, " / ", "1000")
    fileOut.write(generateText(model, startString=word))
    print("working")
    time = time-1
