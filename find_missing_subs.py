import csv

# Define .csv file paths
file_1 = 'report_1.csv'
file_2 = 'report_2.csv'

# Read SubscriptionIDs from .csv file
def read_subscription_ids(file_path):
    subscription_ids = []
    with open(file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            subscription_ids.append(row['SubscriptionId'])
    return subscription_ids

# Find differences between two lists
def find_drifts(list1, list2):
    return list(set(list1) - set(list2))

drifts_a = find_drifts(read_subscription_ids(file_1), read_subscription_ids(file_2))
drifts_b = find_drifts(read_subscription_ids(file_2), read_subscription_ids(file_1))
drifts = drifts_a + drifts_b

# Output the results
if not drifts:
    print('no drifts found')
else:
    print(f'After comparing "{file_1}" with "{file_2}", I found the following drifts:')
    for val in drifts:
        print(val)
