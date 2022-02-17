import os
import json


def parse_json_file_from_path(file_path: str) -> object:
    """Check if file is a json file, load file then return content as an object."""

    if file_path.endswith(".json"):
        with open(file_path, "rb") as file_content:
            file_object = json.load(file_content)

            return file_object


def read_json_files_into_object_array(directory: str) -> list:
    """Read data from JSON files and return an object array containing json file objects."""

    object_array = []

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                parsed_report = parse_json_file_from_path(os.path.join(subdir, file))
                object_array.append(parsed_report)
    return object_array


def get_latest_report_for_user(account_id: str, reports: list) -> object:
    """Return the latest report for a given account_id."""

    user_reports = []

    for report in reports:
        if str(report["user-uuid"]) == str(account_id):
            user_reports.append(report)

    # Sort array on date descending
    user_reports.sort(key=lambda x: x["pulled-timestamp"], reverse=True)

    try:
        return user_reports[0]
    except:
        print(f"No report found for {account_id}")


def get_report_score(report: object) -> int:
    """
    Return the Report -> ScoreBlock -> Delphi -> Score of a given report as an int.
    
    Return None for reports with incorrect keys or values.
    """
    if report is not None:
        try:
            score = report["report"]["ScoreBlock"]["Delphi"]
            return int(score[0]["Score"])
        except KeyError:
            pass
        except ValueError:
            pass
        except IndexError:
            pass
