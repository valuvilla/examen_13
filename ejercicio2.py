from ast import main
from word2number import w2n

def convertir(*args):
    lista ="puedo escribir numeros como "
    for i in args:
        if i != args[-1]:
            lista+=str(w2n.word_to_num(i))+", "
        else:
            lista+=str(w2n.word_to_num(i))+"."
    return lista

print(convertir('one','two','three'))

if __name__ == '__main__':
    main()