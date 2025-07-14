import Utils

from tensorflow.keras import layers
import tensorflow as tf

class CNN_MODEL(tf.keras.Model):
    
    def __init__(self,
                 vocabulary_size,
                 embedding_dimensions=128,
                 cnn_filters=50,
                 dnn_units=512,
                 dropout_rate=0.1,
                 training=False,
                 name="cnn_model"):
        super(CNN_MODEL, self).__init__(name=name)
        
        self.embedding = layers.Embedding(vocabulary_size, embedding_dimensions)
        
        self.cnn_layer1 = layers.Conv1D(filters=cnn_filters,
                                        kernel_size=2,
                                        padding="valid",
                                        activation="relu")
        self.cnn_layer2 = layers.Conv1D(filters=cnn_filters,
                                        kernel_size=3,
                                        padding="valid",
                                        activation="relu")
        self.cnn_layer3 = layers.Conv1D(filters=cnn_filters,
                                        kernel_size=4,
                                        padding="valid",
                                        activation="relu")
        self.pool = layers.GlobalMaxPool1D()
        
        self.dense_1 = layers.Dense(units=dnn_units, activation="relu")
        self.dropout = layers.Dropout(rate=dropout_rate)
        
        self.last_dense = layers.Dense(units=1, activation="sigmoid")
    
    def call(self, inputs, training):
        l = self.embedding(inputs)
        l_1 = self.cnn_layer1(l) 
        l_1 = self.pool(l_1) 
        l_2 = self.cnn_layer2(l) 
        l_2 = self.pool(l_2)
        l_3 = self.cnn_layer3(l)
        l_3 = self.pool(l_3) 
        
        concatenated = tf.concat([l_1, l_2, l_3], axis=-1) # (batch_size, 3 * cnn_filters)
        concatenated = self.dense_1(concatenated)
        concatenated = self.dropout(concatenated, training)
        model_output = self.last_dense(concatenated)
        
        return model_output

if __name__ == "__main__":
    train_path = '../Data/Train_Dataset.csv'
    test_path = '../Data/Test_Dataset.csv'

    train_data, test_data, tokenizer = Utils.dataset_embedding(train_path, test_path)
    
    cnn = CNN_MODEL(len(tokenizer.vocab))
    cnn.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy', Utils.f1_m])

    cnn.fit(train_data, epochs=10, validation_data = test_data, class_weight={1:4, 0:1})