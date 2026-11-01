import pandas as pd

df = pd.read_csv("raw/kt_A15-1.csv",
                 sep=";", decimal=",", header=None,
                 skipinitialspace=True, names=["d_over_w", "Kt"])

df = df.sort_values("d_over_w").reset_index(drop=True)

df[["d_over_w", "Kt"]].to_csv("processed/kt_A15-1_clean.csv", index=False)