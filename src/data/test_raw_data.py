import pandas as pd
import glob
import os


files = glob.glob("data/raw/*.csv")

print(f"Number of files found: {len(files)}")


for file in files[:3]:

    print("\nFILE:", os.path.basename(file))

    df = pd.read_csv(file)

    print(df.head())
    print(df.columns)