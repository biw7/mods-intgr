from googletrans import Translator
from googletrans.gtoken import TokenAcquirer

def trad (string):
    translator = Translator()
    acquirer = TokenAcquirer()
    acquirer.do(string)
    tr = translator.translate(string,src='en',dest='pt')
    titulo = tr.text
    return titulo


