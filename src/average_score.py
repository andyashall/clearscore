from common import parse_json_file_from_path
from paths import REPORTS_PATH
import numpy as np
import pandas as pd
import os

def create_average_score_csv():
    scores = []
    for subdir, _, files in os.walk(
        REPORTS_PATH
    ):
        for file in files:
            if file.endswith(".json"):
                parsed_report = parse_json_file_from_path(os.path.join(subdir, file))

                try:
                    for report in parsed_report["report"]["ScoreBlock"]["Delphi"]:
                        scores.append(int(report["Score"]))
                # Skip reports with incorrect key structure
                except KeyError:
                    continue

    # Convert to numpy array for averaging
    s = np.array(scores)

    # Create dataframe and save to csv
    pd.DataFrame(
        [
            ["Average Score", np.mean(s)],
            ["Average Score (ignore 0)", np.mean(s[s != 0])]
        ]
    ).to_csv("output/average_scores.csv")

