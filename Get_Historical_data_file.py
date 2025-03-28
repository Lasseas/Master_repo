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
num_branches_to_seventhStage = 2
num_branches_to_eighthStage = 0
num_branches_to_ninthStage = 0
num_branches_to_tenthStage = 0

num_timesteps = 24
num_nodes = num_branches_to_firstStage + num_branches_to_firstStage*num_branches_to_secondStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage + num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage*num_branches_to_tenthStage
num_firstStageNodes = num_branches_to_firstStage
num_nodesInlastStage = max(num_branches_to_firstStage, num_branches_to_firstStage*num_branches_to_secondStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage, num_branches_to_firstStage*num_branches_to_secondStage*num_branches_to_thirdStage*num_branches_to_fourthStage*num_branches_to_fifthStage*num_branches_to_sixthStage*num_branches_to_seventhStage*num_branches_to_eighthStage*num_branches_to_ninthStage*num_branches_to_tenthStage)
# ------------------------------------------------------------------------------------------------

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