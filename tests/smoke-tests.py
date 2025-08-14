import pandas as pd

# loading csv to produce
df = pd.read_csv("outputs/features.csv")

# test1: over 50 rows 
assert len(df) > 50, "Dataset is too small."

# test2: has required columns
required_cols = {"CAPE", "CIN", "temp", "pressure"}
assert required_cols.issubset(df.columns), "Missing one or more required columns."
 
# test3: no important columns lack data
assert df[["CAPE", "temp", "pressure"]].notna().all().all(), "Missing values."

# test4: Z-anomaly vals are in reasonable range
assert df["z_anomaly"].between(-5, 5).all(), "Z-anomaly values out of range." 

