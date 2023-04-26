"""
Script to merge the crypto data
"""

import glob

import pandas as pd

import environ.constants

if __name__ == "__main__":

    # Read all the csv files
    all_files = glob.glob(str(environ.constants.RAW_DATA / "crypto" / "*.csv"))

    # Merge all the csv files
    df = pd.concat(
        [pd.read_csv(f) for f in all_files],
    )

    # Save the merged csv file
    df.to_csv(
        environ.constants.PROCESSED_DATA / "crypto.csv",
        index=False,
    )
