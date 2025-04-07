#Historical data file

import random
import pandas as pd

# ------------------------------------------------------------------------------------------------
num_branches_to_firstStage = 2 # Antall grener til det vi i LateX har definert som Omega^first
num_branches_to_secondStage = 10
num_branches_to_thirdStage = 0
num_branches_to_fourthStage = 0
num_branches_to_fifthStage = 0
num_branches_to_sixthStage = 0
num_branches_to_seventhStage = 0
num_branches_to_eighthStage = 0
num_branches_to_ninthStage = 0
num_branches_to_tenthStage = 0

num_timesteps = 24
num_nodes = num_branches_to_firstStage + num_branches_to_firstStage*num_branches_to_secondStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage*num_branches_to_tenthStage
num_firstStageNodes = num_branches_to_firstStage
num_nodesInlastStage = max(num_branches_to_firstStage, num_branches_to_firstStage*num_branches_to_secondStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage*num_branches_to_tenthStage)
# ------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------


def generate_node_probability(branch_counts):
    node_prob = {}
    current_node = 1

    # Process stage 1:
    stage1_nodes = branch_counts[0]
    if stage1_nodes == 0:
        raise ValueError("The first stage must have at least one node.")
    prob = 1.0 / stage1_nodes
    for _ in range(stage1_nodes):
        node_prob[current_node] = prob
        current_node += 1

    cumulative = stage1_nodes
    # For each subsequent stage:
    for i in range(1, len(branch_counts)):
        if branch_counts[i] == 0:
            # Skip this stage if branch count is zero.
            continue
        stage_nodes = cumulative * branch_counts[i]  # number of nodes in this stage
        prob = 1.0 / stage_nodes
        for _ in range(stage_nodes):
            node_prob[current_node] = prob
            current_node += 1
        cumulative *= branch_counts[i]
    return node_prob




NodeProbability = generate_node_probability([num_branches_to_firstStage, num_branches_to_secondStage, num_branches_to_thirdStage, num_branches_to_fourthStage, num_branches_to_fifthStage, num_branches_to_sixthStage, num_branches_to_seventhStage, num_branches_to_eighthStage, num_branches_to_ninthStage, num_branches_to_tenthStage])




####################################################################################
########################### GET CHILD MAPPINNG FUNC #################################
#####################################################################################

def map_children_to_parents_from_file(tab_filename):
    # Les tab-fila (antatt tab-separert)
    df = pd.read_csv(tab_filename, sep="\t")
    
    # Bygg et dictionary med umiddelbare relasjoner: barn -> forelder
    child_to_parent = {row["Node"]: row["Parent"] for _, row in df.iterrows()}
    
    # Funksjon for å finne top-level forelder ved å følge oppover i treet
    def find_top(node):
        # Hvis node ikke finnes som barn (nøkkel) i child_to_parent,
        # er den top-level (det antas at top-level foreldre kun er i Parent-kolonnen)
        if node not in child_to_parent:
            return node
        else:
            return find_top(child_to_parent[node])
    
    # Beregn top-level for alle noder (som finnes som barn)
    top_level = {}
    for node in child_to_parent:
        top_level[node] = find_top(node)
    
    # Gruppér noder etter top-level forelder
    grouping = {}
    for node, top in top_level.items():
        grouping.setdefault(top, []).append(node)
    
    return grouping

def extract_parent_coupling(tab_filename = "Set_ParentCoupling.tab"):
    df = pd.read_csv(tab_filename, sep="\t")
    data = {
        "Node": df["Node"].tolist(),
        "Parent": df["Parent"].tolist()
    }
    return data

data = extract_parent_coupling()
df_example = pd.DataFrame(data)
taB_filenam = "Set_ParentCoupling.tab"
df_example.to_csv(taB_filenam, sep = "\t", index=False, header=True, lineterminator='\n')
mapping = map_children_to_parents_from_file(taB_filenam)
print("Førstestegs-forelder : -> [alle etterkommere]:")
mapping_converted = {int(k): [int(x) for x in v] for k, v in mapping.items()}
print(mapping_converted)


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

# ---- Replace the manual node_month_ranges with parent-group-based logic ----

parent_month_mapping = {
    1: [12, 1, 2],
    2: [3, 4, 5],
    3: [6, 7, 8],
    4: [9, 10, 11],
}

# Extend parent_month_mapping assignment to parent nodes as well
node_to_day = {}

for parent, child_nodes in mapping_converted.items():
    allowed_months = parent_month_mapping.get(parent, [1, 2, 3])
    valid_days = [d for d in day_data_map if d[0] in allowed_months]

    if not valid_days:
        raise ValueError(f"No valid historical days for months {allowed_months} in parent group {parent}")

    # Assign a different random day to each node including the parent
    all_nodes = [parent] + child_nodes  # Include parent itself
    for node in all_nodes:
        node_to_day[node] = random.choice(valid_days)

# Print assignment (month and day) for traceability
print("\n📅 Random day selected for each node:")
for node in sorted(node_to_day):
    m, d = node_to_day[node]
    print(f"Node {node}: Month = {m:02d}, Day = {d:02d}")


# Extract dictionary for reference demand and prices 

def extract_series_for_column(columns, node_to_day, day_data_map, all_keys=None, fill_zero_for_missing=True):
    """
    Extracts 24-hour time series data for specified columns across nodes.

    Parameters:
    - columns: list of column names in the Excel file to extract
    - node_to_day: mapping of node -> (month, day)
    - day_data_map: mapping of (month, day) -> DataFrame with hourly data
    - all_keys: list of all expected keys (e.g., all fuels or all price types)
    - fill_zero_for_missing: if True, fill missing keys with zero time series

    Returns:
    - Dictionary: {key: {node: {timestep: value}}}
    """
    result = {}

    for col in columns:
        result[col] = {}
        for node, (month, day) in node_to_day.items():
            df_day = day_data_map[(month, day)]
            result[col][node] = {t + 1: float(df_day[col].iloc[t]) for t in range(24)}

    if fill_zero_for_missing and all_keys:
        for key in all_keys:
            if key not in result:
                result[key] = {node: {t: 0.0 for t in range(1, 25)} for node in node_to_day}

    return result

# ✅ Define demand-related inputs
demand_columns = ["Electricity", "LT", "MT"]
all_fuels = ["Electricity", "LT", "MT", "H2", "CH4", "Biogas", "CH4_H2_Mix"]

# ✅ Build ReferenceDemand using the unified extractor
ReferenceDemand = extract_series_for_column(
    columns=demand_columns,
    node_to_day=node_to_day,
    day_data_map=day_data_map,
    all_keys=all_fuels,
    fill_zero_for_missing=True
)

# ✅ Define and extract price-related dictionaries
SpotPrice = extract_series_for_column(["Day-ahead Price (EUR/MWh)"], node_to_day, day_data_map)["Day-ahead Price (EUR/MWh)"]
IntradayPrice = extract_series_for_column(["Intraday price (EUR/MWh)"], node_to_day, day_data_map)["Intraday price (EUR/MWh)"]
ActivationUpPrice = extract_series_for_column(["Activation price up (mFRR)"], node_to_day, day_data_map)["Activation price up (mFRR)"]
ActivationDwnPrice = extract_series_for_column(["Activation price down (mFRR)"], node_to_day, day_data_map)["Activation price down (mFRR)"]
CapacityUpPrice = extract_series_for_column(["Capacity price up (mFRR)"], node_to_day, day_data_map)["Capacity price up (mFRR)"]
CapacityDwnPrice = extract_series_for_column(["Capacity price down (mFRR)"], node_to_day, day_data_map)["Capacity price down (mFRR)"]
PV_data = extract_series_for_column(["Soldata"], node_to_day, day_data_map)["Soldata"]
CapacityUpVolume = extract_series_for_column(["Cap_Volume_Up"], node_to_day, day_data_map)["Cap_Volume_Up"]
CapacityDwnVolume = extract_series_for_column(["Cap_Volume_Down"], node_to_day, day_data_map)["Cap_Volume_Down"]



#Create Tech_availability:

Tech_availability = {
    "PV": PV_data,
    "Power_Grid": 1.0,
    "ElectricBoiler": 0.98,
    "HP_LT": 0.98,
    "HP_MT": 0.98,
    "P2G": 0.98,
    "G2P": 0.98,
    "GasBoiler": 0.98,
    "GasBoiler_CCS": 0.98,
    "CHP": 0.98,
    "CHP_CCS": 0.98,
    "Biogas_Grid": 0.9,
    "CH4_Grid": 0.8,
    "CH4_H2_Mixer": 1.0,
    "DieselReserve_Generator": 0.98
}

Cost_export = {
    "Electricity": 0.0,
    "LT": 0.0,
    "MT": 0.0,
    "H2": 150.1502,
    "CH4": 39.479,
    "Biogas": 64.5,
    "CH4_H2_Mix": 0.0
}



import pprint
pprint.pprint(CapacityUpVolume)

def average_dict_values(nested_dict):
    total = 0
    count = 0
    for node_data in nested_dict.values():
        for hour_value in node_data.values():
            total += hour_value
            count += 1
    return total / count if count > 0 else 0

avg_capacity_up = average_dict_values(CapacityUpVolume)
avg_capacity_down = average_dict_values(CapacityDwnVolume)

print(f"Average Capacity Up Price: {avg_capacity_up:.2f} EUR/MW")
print(f"Average Capacity Down Price: {avg_capacity_down:.2f} EUR/MW")

# Preview one node per fuel
pprint.pprint({k: list(v.items())[:1] for k, v in ReferenceDemand.items()})


