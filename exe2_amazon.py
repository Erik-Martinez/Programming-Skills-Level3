"""
Amazon has hired you as a software engineer. Your first task is to create a system that allows 
calculating the price of shipping based on distance. Fulfill the following requirements
    -Amazon has one branch in each state of the USA.
    -Research the approximate distance between each pair of states.
    -The price is $50 USD per kilometer.
    -The minimum number of packages to transport is 100, and the maximum is 500.
    -If the number of packages exceeds 200, a larger vehicle should be recommended, with a price 
     of $60 USD per kilometer.
Based on the distance, the system should calculate an estimated delivery time.
-----------------------------------------------------------------------------------------------"""
import os 
import pandas as pd
import pyarrow
from geopy.distance import distance


#data
statesDF = pd.read_csv('data/states.csv')

# funtions

def info_shipment():
    while True:
        os.system('cls')
        num = 0
        for x in statesDF['state']:
            print(f"| {x} ", end="")
            num += 1
            if num >= 8:
                print("|\n")
                num = 0
        print("\n-------------------------------------------------------------------------")
        
        state_depar = input('Estado de salida del envio: ').capitalize()
        if state_depar not in list(statesDF['state']):
            os.system('cls')
            print('El nombre del estado de salid no ha sido correctamente introducido.')
            input('Pulsa enter para continuar')
            continue
            
        state_arrival = input('Estado receptor del envio:').capitalize()
        if state_arrival not in list(statesDF['state']):
            os.system('cls')
            print('El nombre del estado receptor no ha sido correctamente introducido.')
            input('Pulsa enter para continuar')
            continue
            
        num_pack = input('Número de paquetes a enviar: ')
        num_pack = int(num_pack)
        if num_pack < 100 or num_pack > 500:
            os.system('cls')
            print('El envio tiene que tener un mínimo de 100 paquetos y un máximo de 500.')
            input('Pulsa enter para continuar')
            continue
        
        return state_depar, state_arrival, num_pack
            
    

#code
state_depar, state_arrival, num_pack = info_shipment()

