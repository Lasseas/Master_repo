#Historical data file

import random
import pandas as pd

#####################################################################################
################################## KONSTANTE SETT ###################################
#####################################################################################
#################### HUSK Å ENDRE DISSE I DE ANDRE FILENE OGSÅ ######################
#####################################################################################
#excel_path = "NO1_Aluminum_2024_combined historical data.xlsx"
excel_path = "NO1_Pulp_Paper_2024_combined historical data.xlsx"
instance = 1                    # state which instance you would like to run for
year = 2025                     # state which year you would like to run for

num_branches_to_firstStage = 2 # Antall grener til det vi i LateX har definert som Omega^first
num_branches_to_secondStage = 50
num_branches_to_thirdStage = 50
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

###############################################################################
# ----------------- Parameter data  -----------------
###############################################################################

# --------------------------
# Dictionaries
# --------------------------
if instance == 1: #Expected value
    if year == 2025:
        CostExpansion_Tec = {
            "Power_Grid": 1_000_000,
            "ElectricBoiler": 24.987,
            "HP_LT": 247.605,
            "HP_MT": 297.126,
            "PV": 186.679,
            "P2G": 218.605,
            "G2P": 544.750,
            "GasBoiler": 13.946,
            "GasBoiler_CCS": 224.866,
            "CHP": 277.527,
            "CHP_CCS": 488.447,
            "Biogas_Grid": 1_000_000,
            "CH4_Grid": 1_000_000,
            "CH4_H2_Mixer": 0,
            "DieselReserveGenerator": 100.412,
            "H2_Grid": 1_000_000
        }
        

        CostExpansion_Bat = {
            "BESS_Li_Ion_1": 265.537,
            "BESS_Redox_1": 151.599,
            "CAES_1": 223.435,
            "Flywheel_1": 106.917,
            "Hot_Water_Tank_LT_1": 0.773,
            "H2_Storage_1": 15.113,
            "CH4_Storage_1": 0.01152
        }
    elif year == 2050:
        CostExpansion_Tec = {
            "Power_Grid": 1_000_000,
            "ElectricBoiler": 23.32091,
            "HP_LT": 210.08913,
            "HP_MT": 252.10696,
            "PV": 106.30327,
            "P2G": 92.60185,
            "G2P": 363.16676,
            "GasBoiler": 12.67824,
            "GasBoiler_CCS": 218.29897,
            "CHP": 270.55360,
            "CHP_CCS": 476.17433,
            "Biogas_Grid": 1_000_000,
            "CH4_Grid": 1_000_000,
            "CH4_H2_Mixer": 0,
            "DieselReserveGenerator": 100.41164,
            "H2_Grid": 1_000_000
        }
        
        CostExpansion_Bat = {
            "BESS_Li_Ion_1": 81.38463,
            "BESS_Redox_1": 105.32128,
            "CAES_1": 216.66465,
            "Flywheel_1": 106.91706,
            "Hot_Water_Tank_LT_1": 0.77324,
            "H2_Storage_1": 6.22870,
            "CH4_Storage_1": 0.01152
        }

    else:
        raise ValueError("Invalid year. Please choose either 2025 or 2050.")

elif instance == 2 or instance == 5: #Lowerbound
    if year == 2025:
        CostExpansion_Tec = {
            "Power_Grid": 1_000_000,
            "ElectricBoiler": 19.989,
            "HP_LT": 198.084,
            "HP_MT": 237.701,
            "PV": 149.343,
            "P2G": 174.884,
            "G2P": 435.800,
            "GasBoiler": 11.157,
            "GasBoiler_CCS": 179.893,
            "CHP": 222.021,
            "CHP_CCS": 390.757,
            "Biogas_Grid": 1_000_000,
            "CH4_Grid": 1_000_000,
            "CH4_H2_Mixer": 0,
            "DieselReserveGenerator": 80.329,
            "H2_Grid": 1_000_000
        }
        
        CostExpansion_Bat = {
            "BESS_Li_Ion_1": 212.430,
            "BESS_Redox_1": 121.279,
            "CAES_1": 178.748,
            "Flywheel_1": 85.534,
            "Hot_Water_Tank_LT_1": 0.619,
            "H2_Storage_1": 12.091,
            "CH4_Storage_1": 0.00922
        }
    elif year == 2050:
        CostExpansion_Tec = {
            "Power_Grid": 1_000_000,
            "ElectricBoiler": 18.65673,
            "HP_LT": 168.07130,
            "HP_MT": 201.68556,
            "PV": 85.04262,
            "P2G": 74.08148,
            "G2P": 290.53340,
            "GasBoiler": 10.14259,
            "GasBoiler_CCS": 174.63918,
            "CHP": 216.44288,
            "CHP_CCS": 380.93946,
            "Biogas_Grid": 1_000_000,
            "CH4_Grid": 1_000_000,
            "CH4_H2_Mixer": 0,
            "DieselReserveGenerator": 80.32932,
            "H2_Grid": 1_000_000
        }

        CostExpansion_Bat = {
            "BESS_Li_Ion_1": 65.10770,
            "BESS_Redox_1": 84.25703,
            "CAES_1": 173.33172,
            "Flywheel_1": 85.53365,
            "Hot_Water_Tank_LT_1": 0.61860,
            "H2_Storage_1": 4.98296,
            "CH4_Storage_1": 0.00922
        }

    else:
        raise ValueError("Invalid year. Please choose either 2025 or 2050.")
    
elif instance == 3 or instance == 4: #Upperbound
    if year == 2025:
        CostExpansion_Tec = {
            "Power_Grid": 1_000_000,
            "ElectricBoiler": 29.984,
            "HP_LT": 297.126,
            "HP_MT": 356.551,
            "PV": 224.015,
            "P2G": 262.325,
            "G2P": 653.700,
            "GasBoiler": 16.735,
            "GasBoiler_CCS": 269.840,
            "CHP": 333.032,
            "CHP_CCS": 586.136,
            "Biogas_Grid": 1_000_000,
            "CH4_Grid": 1_000_000,
            "CH4_H2_Mixer": 0,
            "DieselReserveGenerator": 120.494,
            "H2_Grid": 1_000_000
        }

        CostExpansion_Bat = {
            "BESS_Li_Ion_1": 318.645,
            "BESS_Redox_1": 181.919,
            "CAES_1": 268.123,
            "Flywheel_1": 128.300,
            "Hot_Water_Tank_LT_1": 0.928,
            "H2_Storage_1": 18.136,
            "CH4_Storage_1": 0.01382
        }
    elif year == 2050:
        CostExpansion_Tec = {
            "Power_Grid": 1_000_000,
            "ElectricBoiler": 27.98510,
            "HP_LT": 252.10696,
            "HP_MT": 302.52835,
            "PV": 127.56392,
            "P2G": 111.12222,
            "G2P": 435.80011,
            "GasBoiler": 15.21389,
            "GasBoiler_CCS": 261.95877,
            "CHP": 324.66432,
            "CHP_CCS": 571.40920,
            "Biogas_Grid": 1_000_000,
            "CH4_Grid": 1_000_000,
            "CH4_H2_Mixer": 0,
            "DieselReserveGenerator": 120.49397,
            "H2_Grid": 1_000_000
        }

        CostExpansion_Bat = {
            "BESS_Li_Ion_1": 97.66155,
            "BESS_Redox_1": 126.38554,
            "CAES_1": 259.99758,
            "Flywheel_1": 128.30047,
            "Hot_Water_Tank_LT_1": 0.92789,
            "H2_Storage_1": 7.47444,
            "CH4_Storage_1": 0.01382
        }


    else:
        raise ValueError("Invalid year. Please choose either 2025 or 2050.")
else:
    raise ValueError("Invalid instance number.")
# --------------------------    --------------------------
# --------------------------    --------------------------      

CostGridTariff = 123.93


LastPeriodInMonth = {}



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

####################################################################################
########################### GET PARENT MAPPING FUNC #################################
#####################################################################################
def create_parent_mapping(filepath):
    """
    Leser en .tab-fil med kolonnene 'Node' og 'Parent',
    og returnerer en parent_mapping som et Python-dictionary.
    """
    # Les filen
    df = pd.read_csv(filepath, sep="\t")
    
    # Sjekk at nødvendige kolonner finnes
    if not {"Node", "Parent"}.issubset(df.columns):
        raise ValueError("Filen må inneholde kolonnene 'Node' og 'Parent'.")

    # Lag parent_mapping
    parent_mapping = dict(zip(df["Node"], df["Parent"]))
    
    return parent_mapping


# ----------------- HISTORICAL PRICE DATA HANDLING -----------------

# Load data
df = pd.read_excel(excel_path, sheet_name="2024 NO1 data")

# Group by full (month, day) sets
df_grouped = df.groupby(["Month", "Day"])
day_data_map = {
    (month, day): group.reset_index(drop=True)
    for (month, day), group in df_grouped
    if len(group) == 24
}

# ---- Replace the manual node_month_ranges with parent-group-based logic ----
#####################################################################################
########################### CLUSTER BASERT PÅ 4 ÅRSTIDER ############################
#####################################################################################
"""
parent_month_mapping = {
    1: [12, 1, 2],
    2: [3, 4, 5],
    3: [6, 7, 8],
    4: [9, 10, 11],
}
"""
#####################################################################################
########################### CLUSTER BASERT PÅ 2 ÅRSTIDER ############################
#####################################################################################
parent_month_mapping = {
    1: [4, 5, 6, 7, 8, 9],
    2: [1, 2, 3, 10, 11, 12],
}

# Extend parent_month_mapping assignment to parent nodes as well
node_to_day = {}

# For grupper med foreldre (vanlige tilfeller)
for parent, child_nodes in mapping_converted.items():
    allowed_months = parent_month_mapping.get(parent, [1, 2, 3])
    valid_days = [d for d in day_data_map if d[0] in allowed_months]

    if not valid_days:
        raise ValueError(f"No valid historical days for months {allowed_months} in parent group {parent}")

    all_nodes = [parent] + child_nodes
    for node in all_nodes:
        node_to_day[node] = random.choice(valid_days)

# ➕ Legg til førstestegsnoder manuelt basert på parent_month_mapping
for node in range(1, num_firstStageNodes + 1):
    allowed_months = parent_month_mapping.get(node, [1, 2, 3])
    valid_days = [d for d in day_data_map if d[0] in allowed_months]
    
    if not valid_days:
        raise ValueError(f"No valid historical days for months {allowed_months} for first-stage node {node}")
    
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
Res_CapacityUpVolume = extract_series_for_column(["Res_Cap_Volume_Up"], node_to_day, day_data_map)["Res_Cap_Volume_Up"]
Res_CapacityDwnVolume = extract_series_for_column(["Res_Cap_Volume_Down"], node_to_day, day_data_map)["Res_Cap_Volume_Down"]
ID_Capacity_Sell_Volume = extract_series_for_column(["ID_Cap_Volume_Sell"], node_to_day, day_data_map)["ID_Cap_Volume_Sell"]
ID_Capacity_Buy_Volume = extract_series_for_column(["ID_Cap_Volume_Buy"], node_to_day, day_data_map)["ID_Cap_Volume_Buy"]






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
    "CHP": 0.8,
    "CHP_CCS": 0.8,
    "Biogas_Grid": 0.9,
    "CH4_Grid": 0.8,
    "CH4_H2_Mixer": 1.0,
    "DieselReserve_Generator": 0.98,
    "H2_Grid": 0.8
}

Cost_export = {
    "H2_Grid": 0,#150.1502,
    "CH4_Grid": 0,#39.479,
    "Biogas_Grid": 0,#64.5,
}



import pprint

def average_dict_values(nested_dict):
    total = 0
    count = 0
    for node_data in nested_dict.values():
        for hour_value in node_data.values():
            total += hour_value
            count += 1
    return total / count if count > 0 else 0

avg_capacity_up = average_dict_values(Res_CapacityUpVolume)
avg_capacity_down = average_dict_values(Res_CapacityDwnVolume)

print(f"Average Capacity Up Price: {avg_capacity_up:.2f} EUR/MW")
print(f"Average Capacity Down Price: {avg_capacity_down:.2f} EUR/MW")

# Preview one node per fuel
pprint.pprint({k: list(v.items())[:1] for k, v in ReferenceDemand.items()})
pprint.pprint({k: list(v.items())[:1] for k, v in Res_CapacityDwnVolume.items()})
pprint.pprint({k: list(v.items())[:1] for k, v in ID_Capacity_Buy_Volume.items()})


parent_mapping = create_parent_mapping("Set_ParentCoupling.tab")
