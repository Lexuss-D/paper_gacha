import random
import pandas as pd
import numpy as np

data_path = "formatted_df_data.csv"
paperlist = pd.read_csv(
    data_path,
    names=[
        "bib_id",
        "Title",
        "author",
        "Year",
        "url",
        "Book Title",
        "rate",
    ],
)
# labels are like [R,SR,SSR,UR] with ascending rarity
probability = [0.5, 0.3, 0.15, 0.05]
label = ["R", "SR", "SSR", "UR"]
result = np.random.choice(label, 10, p=probability)
print(result)

picklist = []
for rarity in result:
    picklist.append(
        paperlist.loc[paperlist["rate"] == rarity].sample().values.flatten().tolist()
    )


for e in picklist:
    print(e[1])
