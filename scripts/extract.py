import pandas as pd

kiva_loans = pd.read_csv('D:\Data Warehouse Semester Project\kiva_loans (changed).csv')

print(kiva_loans)

# # Settings
# base_path = os.path.abspath(__file__ + "/../../")

# START - Paths for new February 2021 data available

# file url
# kiva_loans_path = "D:\Data Warehouse Semester Project\kiva_loans (changed).csv"
# loan_theme_ids_path = "D:\Data Warehouse Semester Project\loan_theme_ids.csv"
# kiva_mpi_region_locations_path = "D:\Data Warehouse Semester Project\kiva_mpi_region_locations.csv"
# loan_themes_by_region_path ="D:\Data Warehouse Semester Project\loan_themes_by_region.csv"

# Raw path where we want to extract the new .csv data
# new_kiva_loans_path = f"{base_path}/data/raw/kiva_loans.csv"
# new_loan_theme_by_region_path = f"{base_path}/data/raw/loan_themes_by_region.csv"

# END - Paths for new February 2021 data available


# def create_folder_if_not_exists(path):
#     """
#     Create a new folder if it doesn't exists
#     """
#     os.makedirs(os.path.dirname(path), exist_ok=True)


# # def save_new_raw_data():
#     """
#     Save new raw data from the current snapshot from the source
#     """

#     create_folder_if_not_exists(new_kiva_loans_path)

#     with open(kiva_loans_path, mode="r", encoding="windows-1252") as kiva_loans:
#         reader = csv.DictReader(kiva_loans_path)

#         row = next(reader)  # Get first row from reader
#         print("[Extract] First row example:", row)

#         # Open the CSV file in write mode
#         with open( new_kiva_loans_path, mode="w",encoding="windows-1252") as csv_file:
#             # Rename field names so they're ready for the next step
#             fieldnames = {
#                 "Loan_theme_id": "loan_id",
#                 "Loan Theme Type": "address",
#                 "loan_amount": "postal_code",
#                 "country_code": "county",
#                 "country ": "price",
#                 "lender_count": "postal_code",
#                 "borrower_gender": "county",
#                 "repayment_interval ": "price",
#                 "region": "borrower_gender",
#                 "region": "borrower_gender",
#             }
#             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#             # Write headers as first line
#             writer.writerow(fieldnames)
#             for row in reader:
#                 # Write all rows in file
#                 writer.writerow(row)


# def main():
#     print("[Extract] Start")
#     print("[Extract] Downloading snapshot")
#     print(f"[Extract] Saving data from to '{new_kiva_loans_path}'")
#     # save_new_raw_data()
#     print(f"[Extract] End")