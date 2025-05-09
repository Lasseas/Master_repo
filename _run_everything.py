from Generate_data_files import run_everything

#excel_path = "NO1_Aluminum_2024_combined historical data.xlsx"
excel_path = "NO1_Pulp_Paper_2024_combined historical data.xlsx"
instance = 1                    # state which instance you would like to run for
year = 2025                     # state which year you would like to run for

num_branches_to_firstStage = 2 # Antall grener til det vi i LateX har definert som Omega^first
num_branches_to_secondStage = 2
num_branches_to_thirdStage = 2
num_branches_to_fourthStage = 0
num_branches_to_fifthStage = 0
num_branches_to_sixthStage = 0
num_branches_to_seventhStage = 0
num_branches_to_eighthStage = 0
num_branches_to_ninthStage = 0
num_branches_to_tenthStage = 0

run_everything(excel_path, instance, year, num_branches_to_firstStage, num_branches_to_secondStage, num_branches_to_thirdStage, num_branches_to_fourthStage, num_branches_to_fifthStage, num_branches_to_sixthStage, num_branches_to_seventhStage, num_branches_to_eighthStage, num_branches_to_ninthStage, num_branches_to_tenthStage)
