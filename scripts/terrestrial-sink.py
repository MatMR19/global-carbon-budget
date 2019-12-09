import numpy as np
import pandas as pd

from util import root, excel_global

terrestrial_sink_csv = root / "data/terrestrial-sink.csv"

# Terrestrial CO₂ sink

terrestrial_sink = pd.read_excel(
    excel_global,
    sheet_name="Terrestrial Sink",
    skiprows=23,
    index_col="Year",
    usecols="A:B,D:S,U",
)

terrestrial_sink.rename(
    columns={n: n.strip() for n in terrestrial_sink.columns}, inplace=True
)
terrestrial_sink.rename(columns={"GCB": "Terrestrial-Sink"}, inplace=True)

terrestrial_sink.to_csv(terrestrial_sink_csv, encoding="UTF-8", float_format="%.3f")
