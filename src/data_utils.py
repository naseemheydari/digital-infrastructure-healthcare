"""Data-loading helpers for the BRFSS and NTIA source datasets."""

import pandas as pd

from config import BRFSS_RAW_PATH_TEMPLATE, NTIA_RAW_PATH


def load_brfss_year(year: int) -> pd.DataFrame:
    """Load one BRFSS XPT file for the requested survey year."""
    path = str(BRFSS_RAW_PATH_TEMPLATE).format(year=year)
    return pd.read_sas(path, format="xport")


def load_ntia_data() -> pd.DataFrame:
    """Load the NTIA Internet Use Survey source CSV."""
    return pd.read_csv(NTIA_RAW_PATH, low_memory=False)
