# chaine = 'salut les gros cons'
# for i,el in enumerate(chaine):
#     if el in 'AEIOUYaeiouy':
#         print('Voyelle ',i)
#     else:
#         print('Consonne',i)

def table (nb , max = 10):
    i = 0
    while i < max:
        print (i +1, "*", nb , "=", (i + 1) * nb)
        i += 1

# table(10)

i = 10
j= 'a'

lis = ['test',256,'opo']
for el in lis:
    print(el)