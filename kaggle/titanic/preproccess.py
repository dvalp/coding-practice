import pandas as pd
import numpy as np


df = pd.read_csv("data/train.csv")
# df['Deck'] = df[~df['Cabin'].isnull()]['Cabin'].str[0]
df[['Deck', 'CabinNumber']] = df['Cabin'].str.extract('(\w)(\d+)')
df['Title'] = df['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())
df['FamSize'] = df['Parch'] + df['SibSp']
df[['DeckA', 'DeckB', 'DeckC', 'DeckD', 'DeckE', 'DeckF', 'DeckG']] = df['Deck'].str.get_dummies()
df = pd.concat([df, df['Title'].str.get_dummies()], axis=1)

