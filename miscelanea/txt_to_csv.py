import os
import glob
import pandas as pd

MODULE_PATH = os.getcwd()

txt_filenames = glob.glob('./*.txt')

for filename in txt_filenames:
    df_txt = pd.read_csv(filename, sep=";", low_memory=False)
    cols_unnamed = [c for c in df_txt.columns if "Unnamed" in c]
    if len(cols_unnamed):
        print(f"Hay un error con columnas unnameds en {filename}")
    else:
        df_txt.to_csv(filename.replace('.txt','.csv'), index = False, sep = ",")	

print("Listo! Conversion completa")