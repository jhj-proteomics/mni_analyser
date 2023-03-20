import pandas as pd

# Load the data from a CSV file
data = pd.read_csv("test_assemblage.csv")

# Calculate the number of bones for each species and side
counts = data.groupby(['species', 'side'])['bone'].count()

# Calculate the minimum number of individuals for each species
min_individuals = counts.groupby('species').min()

# Calculate the total minimum number of individuals
total_min_individuals = min_individuals.sum()

# Create a list of unique individuals based on the id column
unique_individuals = data['id'].unique()

# Get the unique bones represented for all species
unique_bones_all_species = data['bone'].unique()

# Get the unique bones represented for ovicaprine species
ovicaprine_species = ['ovicaprine']
data_ovicaprine = data[data['species'].isin(ovicaprine_species)]
unique_bones_ovicaprine = data_ovicaprine['bone'].unique()

# Print the results
# Print the total MNI for the assemblage
print("Total MNI for the assemblage:")
print(total_min_individuals)

# Print the MNI for each species
print("MNI per species:")
print(min_individuals)

# Print the list of unique individuals for the entire assemblage
print("Unique individuals in the entire assemblage:")
print(unique_individuals)

# Get the unique ovicaprine ids that have only one row in the dataset
unique_ovicaprine_ids = data_ovicaprine.groupby('id').filter(lambda x: len(x) == 1)['id'].unique()

# Print the list of unique ovicaprine ids that represent a single individual
print("Ovicaprine ids")
print(unique_ovicaprine_ids)

# Get the ovicaprine mandibles and their ids
ovicaprine_mandibles = data_ovicaprine[data_ovicaprine['bone'] == 'mandible']['id'].unique()

# Print the list of ovicaprine mandibles and their ids
print("Ovicaprine mandibles:")
print(ovicaprine_mandibles)
