import random
import pandas as pd
data_path="formatted_df_data.csv"
paperlist=pd.read_csv(data_path,names=['bib_id',
                                        'Title', 
                                        'author',
                                        'Year',
                                        'url',
                                        'Book Title',
                                        'rate',])

print(paperlist.sample(n=10))