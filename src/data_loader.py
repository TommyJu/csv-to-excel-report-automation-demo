from pathlib import Path
import pandas as pd


INPUT_DIR = Path("input")


def load_sales():

    csv_files = list(
        INPUT_DIR.glob("*.csv")
    )

    if not csv_files:
        raise FileNotFoundError(
            "No CSV file found in input folder."
        )

    csv_path = csv_files[0]

    df = pd.read_csv(csv_path)

    print(
        f"Sales report loaded: {csv_path.name}"
    )

    return df