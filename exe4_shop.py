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

total_price = 0

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
            price = selection.loc[:, 'price']
            price = int(price.iloc[0])
            
            if stock >= num_jer:
                return exp, num_jer, price
            
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
def personalize():
    while True:
        personalize = input('Te gustaria perzonalizar las camisetas de este pedido (Si/No): ')
        personalize.lower()
        
        if personalize == 'si' or personalize == 's':
            personalize = 1
            return personalize
        elif personalize == 'no' or personalize == 'n':
            personalize = 0
            return personalize
        else:
            os.system('cls')
            print('No he entendido tu repuesta.')
            input('Pulsa enter para continuar.')
def calculate_prize(member, num_jer, price ,personalize):
    jer_price = 0
    
    jer_price = price*num_jer
    
    if personalize == 1:
        jer_price += 25
    
    if member == 1:
        dis = jer_price*0.2
        jer_price -= dis
    
    return jer_price          
            
# code
member = confirm_membership()
while True:  
    exp, num_jer, price = info_order()
    personalize = personalize()
    price = calculate_prize(member, num_jer, price ,personalize)

    while True:
        os.system('cls')
        print(f'El precio por {num_jer} camisetas es de £{price}')
        decision = input('Añadir a la cesta (Si/No): ')
        dicision = decision.lower()

        if decision == 'si' or decision == 's':
            mask = shopDF.eval(exp)
            shopDF.loc[mask, 'stock'] = int(shopDF.loc[mask, 'stock'].iloc[0]) - num_jer
            total_price += price
            next
        elif decision == 'no' or decision == 'n':
            next
        else:
            os.system('cls')
            print('No he entendido tu repuesta.')
            input('Pulsa enter para continuar.')
            
        while True:
            os.system('cls')
            print(f'El precio total actual es de £{total_price}')
            decision = input('Hacer mas compras(Si/No): ')
            dicision = decision.lower()

            if decision == 'si' or decision == 's':
                break
            elif decision == 'no' or decision == 'n':
                exit()
            else:
                os.system('cls')
                print('No he entendido tu repuesta.')
                input('Pulsa enter para continuar.')
                continue
        break
        
        
        
    
