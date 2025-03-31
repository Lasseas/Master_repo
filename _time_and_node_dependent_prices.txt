import random

# ------------------------------------------------------------------------------------------------
num_branches_to_firstStage = 4 # Antall grener til det vi i LateX har definert som Omega^first
num_branches_to_secondStage = 2
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

def generate_price_dict(nodes, timesteps, reference_data, node_factors):
    price_dict = {}
    for node in nodes:
        factor = node_factors.get(node, 1.0)
        time_dict = {}
        for t in timesteps:
            if isinstance(reference_data, dict):
                ref_val = reference_data.get(t, 0)
            else:
                ref_val = reference_data
            time_dict[t] = ref_val * factor
        price_dict[node] = time_dict
    return price_dict
        
# -------------------------------
Capacity_price_nodes = range(1, num_nodes - num_nodesInlastStage + 1)
timesteps = range(1, num_timesteps + 1)
Capacity_node_factors = {node: random.uniform(0.8, 1.2) for node in Capacity_price_nodes}
# -------------------------------

ref_el_price = {
    1: 20, 2: 20, 3: 20, 4: 20, 5: 20, 6: 20,
    7: 20, 8: 20, 9: 20, 10: 20, 11: 20, 12: 20,
    13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 20,
    19: 20, 20: 20, 21: 20, 22: 20, 23: 20, 24: 20
}

ref_up_price = {
    1: 20, 2: 20, 3: 20, 4: 20, 5: 20, 6: 20,
    7: 20, 8: 20, 9: 20, 10: 20, 11: 20, 12: 20,
    13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 20,
    19: 20, 20: 20, 21: 20, 22: 20, 23: 20, 24: 20
}

CapacityUpPrice = generate_price_dict(Capacity_price_nodes, timesteps, ref_up_price, Capacity_node_factors)

ref_dwn_price = {
    1: 20, 2: 20, 3: 20, 4: 20, 5: 20, 6: 20,
    7: 20, 8: 20, 9: 20, 10: 20, 11: 20, 12: 20,
    13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 20,
    19: 20, 20: 20, 21: 20, 22: 20, 23: 20, 24: 20
}

CapacityDwnPrice = generate_price_dict(Capacity_price_nodes, timesteps, ref_dwn_price, Capacity_node_factors)


# -------------------------------
nodes = range(num_firstStageNodes + 1, num_nodes + 1)
timesteps = range(1, num_timesteps + 1)
node_factors = {node: random.uniform(0.8, 1.2) for node in nodes}


##################################################################################
############################### Spot price generation ###############################
##################################################################################


# Step 1: Custom configs per node range
# Node groups by config (sets of node numbers)
custom_node_configs = {
    "config_1": {
        "nodes": set(range(1, 50)) | set(range(61, 100)),  # Specific nodes
        "start_min": 150,
        "start_max": 250,
        "step_min": 5,
        "step_max": 10
    },
    "config_2": {
        "nodes": set(range(50, 61)) | set(range(100, 111)),  # Multiple disjoint ranges
        "start_min": 200,
        "start_max": 300,
        "step_min": 10,
        "step_max": 25
    },
    "config_default": {  # Catch-all fallback config
        "nodes": None,  # Not needed
        "start_min": 100,
        "start_max": 200,
        "step_min": 5,
        "step_max": 15
    }
}

def get_node_config(node):
    for config in custom_node_configs.values():
        if config["nodes"] and node in config["nodes"]:
            return config
    return custom_node_configs["config_default"]  # fallback


def generate_spotprice_series(config):
    prices = {}
    current_price = random.uniform(config["start_min"], config["start_max"])
    prices[1] = round(current_price, 2)

    for t in range(2, num_timesteps):
        step = random.uniform(config["step_min"], config["step_max"])
        direction = random.choice([-1, 1])
        current_price += direction * step
        prices[t] = round(current_price, 2)

    return prices



# Generate SpotPrice dictionary using the correct config per node
SpotPrice = {}
for node in nodes:
    config = get_node_config(node)
    SpotPrice[node] = generate_spotprice_series(config)


##################################################################################
############################### Spot price finished ###############################
##################################################################################

##################################################################################
############################### Intraday modelling ###############################
##################################################################################

def generate_intraday_from_spot_variable_gap(spot_prices, gap_min=0, gap_max=16):
    intraday_prices = {}

    for t in range(1, num_timesteps):
        gap = random.uniform(gap_min, gap_max)
        direction = random.choice([-1, 1])
        intraday_prices[t] = round(spot_prices[t] + direction * gap, 2)

    return intraday_prices

IntradayPrice = {
    node: generate_intraday_from_spot_variable_gap(spot_prices=SpotPrice[node])
    for node in SpotPrice
}

##################################################################################
############################### Intraday finished ###############################
##################################################################################


ActivationUpPrice = generate_price_dict(nodes, timesteps, ref_el_price, node_factors)
ActivationDwnPrice = generate_price_dict(nodes, timesteps, ref_el_price, node_factors)

#IntradayPrice = generate_price_dict(nodes, timesteps, ref_el_price, node_factors)
import pprint
pprint.pprint(SpotPrice)
pprint.pprint(IntradayPrice)