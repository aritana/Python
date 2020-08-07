"""This is the nester.py module, and it provides one function
    called print_lol() which prints lists that may or may not include nested lists"""
def imprimirLista(lista):
    for sublist in lista:            
        if isinstance(sublist, list):
            imprimirLista(sublist)
        else:
            print(sublist)