import pickle
import tensorflow as tf

with open('data_provider', 'rb') as data_provider_file:
    data_provider = pickle.load(data_provider_file)

    dataset = data_provider.get_batch(batch_size=1, shuffle=False).take(1).repeat()
    batch = next(iter(dataset))
    audio = batch['audio']
    n_samples = audio.shape[1]

    tf.audio.encode_wav(audio, 21000, 'dataset_sample.wav')
    #play(audio)
