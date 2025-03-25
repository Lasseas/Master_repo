import random

# ------------------------------------------------------------------------------------------------
num_branches_to_firstStage = 4 # Antall grener til det vi i LateX har definert som Omega^first
num_branches_to_secondStage = 4
num_branches_to_thirdStage = 2
num_branches_to_fourthStage = 0
num_branches_to_fifthStage = 0
num_branches_to_sixthStage = 0
num_branches_to_seventhStage = 0
num_branches_to_eighthStage = 0
num_branches_to_ninthStage = 0
num_branches_to_tenthStage = 0

num_timesteps = 3
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
# -------------------------------


ref_el_price = {
    1: 20, 2: 20, 3: 20, 4: 20, 5: 20, 6: 20,
    7: 20, 8: 20, 9: 20, 10: 20, 11: 20, 12: 20,
    13: 20, 14: 20, 15: 20, 16: 20, 17: 20, 18: 20,
    19: 20, 20: 20, 21: 20, 22: 20, 23: 20, 24: 20
}

ActivationUpPrice = generate_price_dict(nodes, timesteps, ref_el_price, node_factors)
ActivationDwnPrice = generate_price_dict(nodes, timesteps, ref_el_price, node_factors)

SpotPrice = generate_price_dict(nodes, timesteps, ref_el_price, node_factors)
IntradayPrice = generate_price_dict(nodes, timesteps, ref_el_price, node_factors)

