import random

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

def generate_time_node_dict(tech_name, nodes, timesteps, reference_data, node_factors):
    tech_dict = {}
    for node in nodes:
        # Get node's factor; default to 1.0 if not provided.
        factor = node_factors.get(node, 1.0)
        # Build the dictionary for all timesteps for this node.
        time_dict = {}
        for t in timesteps:
            # If reference_data is a dictionary, retrieve the reference value for this timestep;
            # otherwise assume it is a constant.
            if isinstance(reference_data, dict):
                if isinstance(reference_data.get(node), dict):  # node-specific dict
                    ref_val = reference_data.get(node, {}).get(t, 0)
                else:  # timestep-only dict
                    ref_val = reference_data.get(t, 0)
            else:
                ref_val = reference_data

            time_dict[t] = ref_val * factor
        tech_dict[node] = time_dict
    return {tech_name: tech_dict}


# -------------------------------
nodes = range(num_firstStageNodes + 1, num_nodes + 1)
timesteps = range(1, num_timesteps + 1)
node_factors = {node: random.uniform(0.8, 1.2) for node in nodes}
# -------------------------------

fuel_name = "Electricity"
reference_data = {
        1: 20, 2: 20, 3: 20, 4: 20, 5: 20, 6: 20,
        7: 20, 8: 20, 9: 20, 10: 20, 11: 20, 12: 20,
        13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 20,
        19: 20, 20: 20, 21: 20, 22: 20, 23: 20, 24: 20
    }

Cost_export = {
    "Electricity": 0.0,
    "LT": 0.0,
    "MT": 0.0,
    "CH4": 0.0,
    "Biogas": 0.0,
    "CH4_H2_Mix": 0.0
}


fuel_name_ref_demand = ["Electricity", "LT", "MT"]
reference_data_El = {
        1: 20, 2: 20, 3: 20, 4: 20, 5: 20, 6: 20,
        7: 20, 8: 20, 9: 20, 10: 20, 11: 20, 12: 20,
        13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 20,
        19: 20, 20: 20, 21: 20, 22: 20, 23: 20, 24: 20
    }
reference_data_LT = {
        1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5,
        7: 5, 8: 5, 9: 5, 10: 5, 11: 5, 12: 5,
        13: 5, 14: 5, 15: 5, 16: 5, 17: 5, 18: 5,
        19: 5, 20: 5, 21: 5, 22: 5, 23: 5, 24: 5
    }
reference_data_MT = {
        1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2,
        7: 2, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2,
        13: 2, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2,
        19: 2, 20: 2, 21: 2, 22: 2, 23: 2, 24: 2
    }

ReferenceDemand = {
    **generate_time_node_dict(fuel_name_ref_demand[0], nodes, timesteps, reference_data_El, node_factors),
    **generate_time_node_dict(fuel_name_ref_demand[1], nodes, timesteps, reference_data_LT, node_factors),
    **generate_time_node_dict(fuel_name_ref_demand[2], nodes, timesteps, reference_data_MT, node_factors),
    "CH4": 0.0,
    "Biogas": 0.0,
    "CH4_H2_Mix": 0.0
}


#PV_data = {node: random.uniform(0, 1) for node in nodes}
node_factors_pv = {node: 1 for node in nodes}

##################################################################################
############################### PV modelling ###############################
##################################################################################

pv_season_configs = {
    "summer": {
        "nodes": set(range(1, 50)),
        "ranges": [(0.6, 0.9), (0.4, 0.8), (0.2, 0.7)],
        "zero_hours": [1, 2, 3, 4, 22, 23, 24]
    },
    "fall": {
        "nodes": set(range(50, 100)),
        "ranges": [(0.3, 0.6), (0.2, 0.5)],
        "zero_hours": [1, 2, 3, 4, 5, 21, 22, 23, 24]
    },
    "winter": {
        "nodes": set(range(100, 150)),
        "ranges": [(0.1, 0.4)],
        "zero_hours": list(range(1, 8)) + list(range(17, 25))  # 1–7 and 17–24
    },
    "spring": {
        "nodes": set(range(150, 1000)),  # everything else
        "ranges": [(0.4, 0.7), (0.3, 0.6)],
        "zero_hours": [1, 2, 3, 4, 5, 20, 21, 22, 23, 24]
    }
}

def get_pv_season_config(node):
    for config in pv_season_configs.values():
        if node in config["nodes"]:
            return config
    return {"ranges": [(0.0, 0.0)], "zero_hours": list(range(1, 25))}  # default: zero all

def generate_pv_profile_per_node(config):
    profile = {}
    for t in range(1, 25):
        if t in config["zero_hours"]:
            profile[t] = 0.0
        else:
            pv_range = random.choice(config["ranges"])
            profile[t] = round(random.uniform(*pv_range), 3)
    return profile

PV_data = {}
for node in nodes:
    config = get_pv_season_config(node)
    PV_data[node] = generate_pv_profile_per_node(config)

##################################################################################
############################### PV finished ###############################
##################################################################################

Tech_availability = {
    **generate_time_node_dict("PV", nodes, timesteps, PV_data, node_factors_pv),

    "Power_Grid": 1.0,
    "ElectricBoiler": 0.98,
    "HP_LT": 0.98,
    "HP_MT": 0.98,
    "P2G": 0.98,
    "G2P": 0.98,
    "GasBoiler": 0.98,
    "CHP": 0.98,
    "Biogas_Grid": 0.9,
    "CH4_Grid": 0.8,
    "CH4_H2_Mixer": 1.0
}


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





import pprint
pprint.pprint(PV_data)

