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

dic_type = {0: 'Hombre', 1: 'Mujer', 2: 'Niños'}
dic_sleeve = {0: 'corta', 1: 'larga'}
dic_size = {0: 'M', 1: 'XL', 2: '3Xl'}

print(shopDF)