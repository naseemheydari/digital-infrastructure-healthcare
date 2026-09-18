"""Project configuration for the digital infrastructure and healthcare analysis."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"

# Expected locations for source data when reproducing the full pipeline locally.
BRFSS_RAW_PATH_TEMPLATE = DATA_DIR / "brfss" / "BRFSS_{year}.XPT"
NTIA_RAW_PATH = DATA_DIR / "ntia" / "NTIA.csv"

YEARS = [2019, 2021, 2023]

BRFSS_HEALTHCARE_VARS = [
    "CHECKUP1",
    "PERSDOC3",
    "FLUSHOT7",
    "EXERANY2",
    "CHOLCHK3",
]

BRFSS_CONTROL_VARS = ["_METSTAT", "_EDUCAG", "_INCOMG1"]
BRFSS_ID_VARS = ["_STATE"]

NTIA_VARS = [
    "wiredHighSpeedAtHome",
    "homeInternetUser",
    "callConfUser",
    "pcOrTabletUser",
    "mobilePhoneUser",
    "emailUser",
    "tooExpensiveMainReason",
]
