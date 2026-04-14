
import sys
import itertools

try:
    import pandas as pd
except ImportError:
    print("ERROR: pandas is not installed. Please install pandas v1.5.0.")
    sys.exit(1)

print(f"Using Pandas v{pd.__version__}")

# ANSI color codes
_COLORS = itertools.cycle([
    "\033[34m",  # blue
    "\033[36m",  # cyan
    "\033[32m",  # green
])

def report_df(df, label):
    color = next(_COLORS)
    reset = "\033[0m"
    border = "=" * 50

    print(f"{color}{border}\n{label}\n{border}{reset}", flush=True)
    print(df[['Species','Segment', 'Length', 'Accession']].to_string(index=False))


df1 = pd.read_csv("pt2_dataset-1.csv")
report_df(df1, "Dataframe 1")

df2 = pd.read_csv("pt2_dataset-2.csv")
report_df(df2, "Dataframe 2")

df = df1.append(df2)
report_df(df, "Combined Dataframes")