"""Reusable cleaning helpers for the project notebooks."""

import numpy as np


def compare_variables(main_df, other_df, main_year, other_year):
    """Print column-name differences between two survey-year DataFrames."""
    main_cols = set(main_df.columns)
    other_cols = set(other_df.columns)

    missing_in_other = main_cols - other_cols
    extra_in_other = other_cols - main_cols

    print(f"\nComparing {main_year} dataset to {other_year}")

    if missing_in_other:
        print(
            f"Missing columns in {other_year} dataset: "
            f"{sorted(missing_in_other)}"
        )
    else:
        print(
            f"All {main_year} column names are present in "
            f"the {other_year} dataset"
        )

    if extra_in_other:
        print(
            f"Extra columns in {other_year} dataset: "
            f"{sorted(extra_in_other)}"
        )


def normalize_columns(columns):
    """Strip surrounding whitespace and lowercase column names."""
    return [col.strip().lower() for col in columns]


def clean_brfss_missing_values(df):
    """Replace BRFSS missing/refused response codes used in this analysis."""
    return df.replace([7, 9, 77, 99], np.nan)
