import pickle
from ddsp.training import data

data_provider = data.NSynthTfds(split='test')

with open('data_provider', 'wb') as data_provider_file:
    pickle.dump(data_provider, data_provider_file)