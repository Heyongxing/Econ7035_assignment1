import pandas as pd

def clean(input_file1, input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    merged_df = pd.merge(df1,df2, left_on="respondent_id", right_on="id")
    merged_df.drop("id", axis=1, inplace=True)
    merged_df = merged_df.dropna()
    merged_df = merged_df[~merged_df["job"].str.contains("insurance|Insurance")]
    print("Output file shape:", merged_df.shape)
    return merged_df

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file1")
    parser.add_argument("input_file2")
    parser.add_argument("output")
    args = parser.parse_args()
    cleaned = clean(args.input_file1, args.input_file2)
    cleaned.to_csv(args.output, index = False)
