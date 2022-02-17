import pandas as pd

from common import (
    read_json_files_into_object_array,
    get_latest_report_for_user
)
from paths import ACCOUNTS_PATH, REPORTS_PATH

# read reports
reports = read_json_files_into_object_array(REPORTS_PATH)

# read users
accounts = read_json_files_into_object_array(ACCOUNTS_PATH)


def get_enriched_data(accounts: list, reports: list) -> list:
    """Return an object list of enriched data."""
    enriched_data = []

    for account in accounts:
        account_id = account["uuid"]
        latest_report = get_latest_report_for_user(account_id, reports)
        
        if latest_report:
            enriched_data.append(
                {
                    "user-uuid": account["uuid"],
                    "employment_status": account["account"]["user"]["employmentStatus"],
                    "bank_name": account["account"]["user"]["bankName"],
                    "number_of_active_bank_accounts": latest_report["report"]["Summary"]["Payment_Profiles"]["CPA"]["Bank"]["Total_number_of_Bank_Active_accounts_"],
                    "total_outstanding_balance": latest_report["report"]["Summary"]["Payment_Profiles"]["CPA"]["Bank"]["Total_outstanding_balance_on_Bank_active_accounts"]
                }
            )
            
    return enriched_data


def create_enriched_bank_data_csv():
    enriched_data_df = pd.DataFrame.from_dict(get_enriched_data(accounts, reports))
    enriched_data_df.to_csv("output/enriched_data.csv")