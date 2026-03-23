import matplotlib.pyplot as plt

years = [1986, 2013, 2020, 2024, 2024, 2025]
costs = [16500, 1000, 3000, 300, 262.5, 100]
labels = ["C. elegans", "Mouse Retina", "Fruit Fly (Hemi)", "Fruit Fly (Full)", "Human Fragment", "Small Organism (2025)"]

# Sort data for a cleaner line plot
data_sorted = sorted(zip(years, costs, labels))
years_sorted, costs_sorted, labels_sorted = zip(*data_sorted)

plt.figure(figsize=(10, 6))
plt.plot(years_sorted, costs_sorted, marker='o', linestyle='-', color='b')

# Use sorted data for annotations
for i, label in enumerate(labels_sorted):
    plt.annotate(label, (years_sorted[i], costs_sorted[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.yscale('log')
plt.title('Historical Cost of Connectome Reconstruction per Neuron')
plt.xlabel('Year')
plt.ylabel('Cost per Neuron (USD, Log Scale)')
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.savefig('cost_per_neuron.png')
