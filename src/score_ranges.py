import pandas as pd

from common import (
    get_latest_report_for_user,
    read_json_files_into_object_array,
    get_report_score,
)

from paths import ACCOUNTS_PATH, REPORTS_PATH

# read reports
reports = read_json_files_into_object_array(
    REPORTS_PATH
)

# read users
accounts = read_json_files_into_object_array(
    ACCOUNTS_PATH
)


def get_accounts_and_latest_score(accounts: list) -> list:
    """Return an object list containing accountId and latest report score."""
    account_and_score = []

    for account in accounts:
        account_id = account["accountId"]
        latest_report = get_latest_report_for_user(account_id, reports)
        latest_report_score = get_report_score(latest_report)
        account_and_score.append(
            {"accountId": account_id, "latestScore": latest_report_score}
        )

    return account_and_score


def filter_accounts_using_score_range(lower: int, upper: int, accounts: list) -> list:
    """Return an object list filtered by upper and lower score limit."""
    filtered_accounts = []
    for account in accounts:
        if account["latestScore"] is not None:
            if (
                int(account["latestScore"]) >= lower
                and int(account["latestScore"]) <= upper
            ):
                filtered_accounts.append(account)

    return filtered_accounts


def create_score_ranges_csv():
    accounts_and_scores = get_accounts_and_latest_score(accounts)

    ranges = [
        [0, 50],
        [51, 100],
        [101, 150],
        [151, 200],
        [201, 250],
        [251, 300],
        [301, 350],
        [351, 400],
        [401, 450],
        [451, 500],
        [501, 550],
        [551, 600],
        [601, 650],
        [651, 700],
        [701, 750],
        [751, 800],
        [801, 850],
        [851, 900],
        [901, 950],
        [951, 1000],
    ]

    output = pd.DataFrame.from_dict(
        [
            {
                "Range": f"{range[0]} - {range[1]}",
                "Count": len(
                    filter_accounts_using_score_range(
                        range[0], range[1], accounts_and_scores
                    )
                ),
            }
            for range in ranges
        ]
    )

    output.to_csv("output/score_ranges.csv")
