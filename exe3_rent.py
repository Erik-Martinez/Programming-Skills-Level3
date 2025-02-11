"""
A real estate agency has 5 homes for rent. The homes are characterized by their size, number of bedrooms, number of bathrooms, and location. The rental price of a home is calculated based on these factors.
Features:

First home: 200 square meters, 3 bedrooms, 2 bathrooms
Second home: 150 square meters, 2 bedrooms, 2 bathrooms
Third home: 100 square meters, 2 bedrooms, 1 bathroom
Fourth home: 100 square meters, 1 bedroom, 2 bathrooms
Fifth home: 80 square meters, 1 bedroom, 1 bathroom

The program must quote the price of the home according to: square meters, number of bedrooms, and number of bathrooms.
Each bedroom adds $40, and each bathroom adds $30. Each square meter has a cost of $90."""

import os

# data
data = {1: (200, 3, 2), 2: (150, 2, 2), 3: (100, 2, 1), 4: (100, 1, 2), 5:(80, 1, 1)}

for x in data:
    y = data[x]
    price = y[0]*90+y[1]*40+y[2]*30
    print(f'{x}º casa: £{price}')