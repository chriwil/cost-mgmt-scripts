import csv

# Define .csv file paths
file_1 = 'report_1.csv'
file_2 = 'report_2.csv'

# Returns a costs dictionary by ResourceId
def get_costs(file_path):
    costs = {}
    with open(file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            costs[row['ResourceId']] = row['EffectivePrice']
    return costs

def compare_costs(given_costs, file_path):
    with open(file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if given_costs[row['ResourceId']] != row['EffectivePrice']:
                print(f'Drift found for {row['ResourceId']}')
   
costs_1 = get_costs(file_1)
costs_2 = get_costs(file_2)

if len(costs_1) != len(costs_2):
    print(f'inappropriate model for {file_1} and {file_2}')
else:
    compare_costs(costs_1, file_2)

print(f'Finished comparing {file_1} and {file_2}')
