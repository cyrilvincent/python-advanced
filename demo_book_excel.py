import pandas as pd
import media
from typing import List

df = pd.read_excel("data/books.xlsx")
print(df)
res:List[media.Book] = []
category_dico = {}
for index, row in df.iterrows():
    b = media.Book(row.id,row.title,row.price,[])
    if row.category not in category_dico.keys():
        c = media.Category(row.category, [b])
        category_dico[row.category] = c
        b.category = c
    else:
        b.category = category_dico[row.category]
        b.category.books.append(b)
    res.append(b)
print(res)
print(category_dico.values())