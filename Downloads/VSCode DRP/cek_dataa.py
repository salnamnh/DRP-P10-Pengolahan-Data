import pandas as pd
df = pd.read_csv("cleaned_animal_disease_prediction.csv")

print(df.shape)
print(df.head())

#cek kesehatan data
df.info()
print(df.isna().sum())

#cek duplikat
print("jumlah data duplikat",df.duplicated().sum())

#cek penulisan
print(df["Coughing"].value_counts())

#cek kolom dengan tipe float atau int
print(df[["Age","Weight","Heart_Rate"]].describe())

df = df.drop_duplicates()
df.info()

print(df["Duration"].value_counts())