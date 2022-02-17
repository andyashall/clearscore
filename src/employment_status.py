from common import read_json_files_into_object_array
from paths import ACCOUNTS_PATH
import pandas as pd

# Read user accounts
user_accounts = read_json_files_into_object_array(
    ACCOUNTS_PATH
)


def filter_accounts_using_employment_status(
    employment_status: str, accounts: list
) -> list:
    """Return an object list of accounts filtered by given employment_status."""
    filtered_accounts = []
    for account in accounts:
        try:
            if account["account"]["user"]["employmentStatus"] == employment_status:
                filtered_accounts.append(account)
        # If no employment_status key is found 
        except KeyError:
            # Add account if employment_status is NULL
            if employment_status == "NULL":
                filtered_accounts.append(account)
            continue

    return filtered_accounts


def create_employment_status_csv():

    # TODO: get a list of unique statuses from account objects
    status = [
        "FT_EMPLOYED",
        "SELF_EMPLOYED",
        "UNEMPLOYED",
        "STUDENT",
        "WORK_AT_HOME",
        "NULL"
    ]

    output = pd.DataFrame.from_dict(
        [
            {
                "employment_status": employment_status,
                "Count": len(filter_accounts_using_employment_status(employment_status, user_accounts))}
            for employment_status in status
        ]
    )

    output.to_csv("output/employment_status.csv")

