from imageai.Prediction.Custom import ModelTraining

model_train = ModelTraining()
model_train.setModelTypeAsResNet()
model_train.setDataDirectory("/Users/michaelmarsella/KanaMachine/kmnist")
model_train.trainModel(num_objects=71, num_experiments=20, enhance_data=True, batch_size=32, show_network_summary=True)