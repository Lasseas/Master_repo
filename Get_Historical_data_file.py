#Historical data file

import random
import pandas as pd

# ------------------------------------------------------------------------------------------------
num_branches_to_firstStage = 4 # Antall grener til det vi i LateX har definert som Omega^first
num_branches_to_secondStage = 2
num_branches_to_thirdStage = 2
num_branches_to_fourthStage = 2
num_branches_to_fifthStage = 2
num_branches_to_sixthStage = 2
num_branches_to_seventhStage = 0
num_branches_to_eighthStage = 0
num_branches_to_ninthStage = 0
num_branches_to_tenthStage = 0

num_timesteps = 24
num_nodes = num_branches_to_firstStage + num_branches_to_firstStage*num_branches_to_secondStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage*num_branches_to_tenthStage
num_firstStageNodes = num_branches_to_firstStage
num_nodesInlastStage = max(num_branches_to_firstStage, num_branches_to_firstStage*num_branches_to_secondStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage*num_branches_to_tenthStage)
# ------------------------------------------------------------------------------------------------

# ----------------- HISTORICAL PRICE DATA HANDLING -----------------

# Load data
excel_path = "NO1_2024_combined historical data.xlsx"
df = pd.read_excel(excel_path, sheet_name="2024 NO1 data")

# Group by full (month, day) sets
df_grouped = df.groupby(["Month", "Day"])
day_data_map = {
    (month, day): group.reset_index(drop=True)
    for (month, day), group in df_grouped
    if len(group) == 24
}

# Define node-month mapping
node_month_ranges = {
    "range_1": {"nodes": range(1, 51), "months": [1, 2, 3]},
    "range_2": {"nodes": range(51, 101), "months": [4, 5, 6]},
}

# Assign each node a random day from allowed months
node_to_day = {}
for node in range(1, num_nodes + 1):
    for config in node_month_ranges.values():
        if node in config["nodes"]:
            valid_days = [key for key in day_data_map if key[0] in config["months"]]
            node_to_day[node] = random.choice(valid_days)
            break

# Extract dictionary per price type
def extract_series_for_price_column(column_name):
    price_dict = {}
    for node, (month, day) in node_to_day.items():
        day_df = day_data_map[(month, day)]
        price_dict[node] = {t+1: float(day_df[column_name].iloc[t]) for t in range(24)}
    return price_dict

# Create dictionaries
SpotPrice = extract_series_for_price_column("Day-ahead Price (EUR/MWh)")
IntradayPrice = extract_series_for_price_column("Intraday price (EUR/MWh)")
ActivationUpPrice = extract_series_for_price_column("Activation price up (mFRR)")
ActivationDwnPrice = extract_series_for_price_column("Activation price down (mFRR)")
CapacityUpPrice = extract_series_for_price_column("Capacity price up (mFRR)")
CapacityDwnPrice = extract_series_for_price_column("Capacity price down (mFRR)")
PV_data = extract_series_for_price_column("Soldata")

import pprint
pprint.pprint(SpotPrice)
pprint.pprint(IntradayPrice)
pprint.pprint(PV_data)