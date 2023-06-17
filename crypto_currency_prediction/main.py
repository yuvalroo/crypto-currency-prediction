from utils import *
from model import *

if __name__ == '__main__':
  df = CryptoCompareConnector.data_histoday('btc')
  dl = DataloaderGenerator.gen(df, 1)
  crypto_model = CryptoPredictorModel()
  hp = HyperParams('ce', 'adam', 0.001, 3)
  trained_model = Trainer.train(crypto_model, hp)
