"""
United Direct, the official store of Manchester United FC, has hired you 
as a developer for their online store. The manager wishes to launch a new line
of products with different discounts.

Develop the shopping cart of this application considering the following features:

    The jerseys are classified by: Men, Women, and Children.
    Sizes range from XS to 3XL.
    All men's and women's jerseys are priced at £100 if they are short-sleeved.
    Long-sleeved jerseys cost £120.
    Short-sleeved children's jerseys are priced at £70.
    Long-sleeved children's jerseys are priced at £90.
    If you are a club member, you get a 20% discount on the total purchase.
    The user can buy as many jerseys as they want.
    If the buyer wishes to personalize their jersey with a player's number, there 
    is an additional charge of £25.

The stock is as follows:
..."""
import os
import pandas as pd

#data

shopDF = pd.read_csv('data/shop_stock.csv', sep=';')

dic_type = {0: 'Hombre', 1: 'Mujer ', 2: 'Niños '}
dic_sleeve = {0: 'corta', 1: 'larga'}
dic_size = {0: 'M', 1: 'XL', 2: '3Xl'}

#print(shopDF)

#funtions 
def confirm_membership():
    while True:
        os.system('cls')
        member = input('Eres miembro del club del Manchester United (Si/No): ')
        member = member.lower()
        
        if member == 'si' or member == 's':
            member = 1
            return member
        elif member == 'no' or member == 'n':
            member = 0 
            return member
        else:
            os.system('cls')
            print('No he entendido tu respuesta.')
            input('Pulsa enter para continuar.')
def info_order():
    while True:
        os.system('cls')
        for x in dic_type.items():
            print(f'| {x[1]} | {x[0]} |')
            
        type_jer = input('Tipo camiseta: ')
        
        if type_jer not in ['0', '1', '2']:
            os.system('cls')
            print('No he entendido tu repuesta.')
            input('Pulsa enter para continuar.')
            continue
            
        print('-----------------------')
            
        for x in dic_sleeve.items():
            print(f'| {x[1].capitalize()} | {x[0]} |')
            
        sleeve = input('Tipo de manga: ')
        
        if sleeve not in ['0', '1']:
            os.system('cls')
            print('No he entendido tu repuesta.')
            input('Pulsa enter para continuar.')
            continue
            
        print('-----------------------')
        
        for x in dic_size.items():
            print(f'| {x[1].capitalize()} | {x[0]} |')
        
        size = input('Talla de camiseta: ')
        
        if size not in ['0', '1', '2']:
            os.system('cls')
            print('No he entendido tu repuesta.')
            input('Pulsa enter para continuar.')
            continue
        
        while True:
            print('-----------------------')
            
            num_jer = input('Número de camisetas a comprar: ')
            num_jer = int(num_jer)
            
            exp = f'type == {type_jer} and sleeve == {sleeve} and size == {size}'
            selection = shopDF.query(exp)
            stock = selection.loc[:,'stock']
            stock = int(stock.iloc[0])
            
            if stock >= num_jer:
                return type_jer, sleeve, size, num_jer
            
            elif stock <= 0:
                os.system('cls')
                print('No nos quedan existencia de esas camisetas.')
                input('Pulsa enter para continuar.')
                os.system('cls')
                return
            
            else: 
                os.system('cls')
                print('Lo lamentamos pero en número de camisetas que solicitas es '
                    'es superior al stock.')
                input('Pulsa enter para continuar.')
                os.system('cls')
                continue
            
            
            
        
 
        
        
            
            
            
            
# code 
#member = confirm_membership()
type_jer, sleeve, size, num_jer = info_order()
