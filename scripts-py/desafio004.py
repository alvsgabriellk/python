txt = (input('Digite algo:'))
#stxt = (type(txt))                OUTRA FORMA
#espc = (txt.isspace())            OUTRA FORMA
#nmr = (txt.isnumeric())           OUTRA FORMA
#alfa = (txt.isalpha())            OUTRA FORMA
#alfanum = (txt.isalnum())         OUTRA FORMA
#maius = (txt.isupper())           OUTRA FORMA
#minus = (txt.islower())           OUTRA FORMA
#print('O tipo primitivo desse valor é:', stxt)         OUTRA FORMA
print('O tipo primitivo desse valor é:', type(txt))
print('Só tem espaço?', txt.isspace())
print('É um número?', txt.isnumeric())
print('É alfabético?', txt.isalpha())
print('É alfanúmerica?', txt.isalnum())
print('Esta toda em maiúsculas?', txt.isupper())
print('Esta toda em minúsculas?', txt.islower())
print('Está capitalizada?', txt.istitle())