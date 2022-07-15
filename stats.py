import os
import pandas as pd
import matplotlib.pyplot as plt

class Stats():
    def __init__(self):
        self.df = pd.DataFrame(columns=['arquivo', 'tempo (ms)'])
        self.indice = 0

    def add_data(self, filename, time):
        self.df.loc[self.indice] = [filename, time]
        self.indice += 1

    def plot_and_save(self, figure_filename):
        os.makedirs(os.path.dirname(figure_filename), exist_ok=True)
        plt.figure(figsize=(10, 5))
        plt.title('Tempo de execução')
        plt.xlabel('Arquivos')
        plt.ylabel('Tempo (ms)')
        plt.plot(self.df['arquivo'], self.df['tempo (ms)'], 'o-')
        plt.savefig(figure_filename)
        plt.close()
