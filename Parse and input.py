import  pandas as pd
from example.models import anime
df=pd.read_csv('Data/animes_cleaned.csv')
for i in df.index:
    #print(df.loc[i,'title'])
    a=anime(title=df.loc[i,'title'],rank=df.loc[i,'rank'],score=df.loc[i,'score'],users_rated=df.loc[i,'users_rated'],Popularity=df.loc[i,'Popularity'],Favorites=df.loc[i,'Favorites'],Members=df.loc[i,'Members'],animeType=df.loc[i,'animeType'],Episodes=df.loc[i,'Episodes'],status=df.loc[i,'status'],premiered=df.loc[i,'premiered'],studio=df.loc[i,'studio'],source=df.loc[i,'source'],rating=df.loc[i,'rating'],genres=df.loc[i,'genres'])
    a.save()
print('ho')