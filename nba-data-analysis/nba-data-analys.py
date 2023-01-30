import numpy as np
import pandas as pd

df = pd.read_csv("nba.csv")
dd = pd.read_csv("Seasons_Stats.csv")

result = df

# result = df.head(10)


# result = len(df)
# ss = len(df.index) # farklı yöntem.

# result = df["salary"].mean()


# result = df["salary"].max()

# result = df.groupby("salary")["Player"].max()
# result =df.groupby("salary").sample()["Player"]
# result = df.nlargest(1,"salary")["Player"].iloc[0]
#BENİM YAPTIKLARIM ^^
# result = df[df["salary"]==df["salary"].max()]["Player"].iloc[0] 

result = dd[(dd["Age"]>=20) & (dd["Age"] <= 25)][["Player","Tm","Age"]].sort_values("Age",ascending=False)
# result = dd.query("Age>=20 & Age<=25")["Tm"]#.sort_values(ascending=False)

result = df.groupby("Player").get_group("Ron Baker")["Tm"].iloc[0] 
# result = df[df["Player"]== "Ron Baker"]["Tm"].iloc[0] 


# result = df.groupby("Tm").mean()["salary"]

# result = df["Tm"].unique()
# result = len(df["Tm"].unique())
# result = df["Tm"].nunique()

# result = df.groupby(["Tm"]).nunique() # Kısmen Yanlış!
# result = df["Tm"].value_counts()    # Tam Doğru Olanı.
# result = df[df["Player"].str. ("and")]["Player"]


# def str_find(name):
#     if "and" in name.lower():
#         return True
#     return False
# result = df[df["Player"].apply(str_find)]["Player"]

print(result)