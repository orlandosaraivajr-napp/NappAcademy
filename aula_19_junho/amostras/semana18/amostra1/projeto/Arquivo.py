import csv
from abc import ABC, abstractmethod
import os
import glob

class Arquivo(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def pega_arquivos(self):
        pass
    
    

class ArquivoCSV(Arquivo):

    def pega_arquivos(self):
        looking_for = '**/*.csv'
        matched = glob.glob(looking_for, recursive=True)
        return matched


class ArquivoTXT(Arquivo):

    def pega_arquivos(self):
        looking_for = '**/*.txt'
        matched = glob.glob(looking_for, recursive=True)
        return matched

    
