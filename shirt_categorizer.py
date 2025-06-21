import csv
import math
from collections import Counter

# Load data from CSV
def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            size = int(row['Size'])
            quality = int(row['Quality'])
            category = row['Category']
            data.append((size, quality, category))
    return data

# Calculate Euclidean distances
def calculate_distances(data, new_item):
    distances = []
    for index, (size, quality, category) in enumerate(data):
        dist = math.sqrt((size - new_item[0])**2 + (quality - new_item[1])**2)
        distances.append((index, dist, category))
    return distances

# Sort distances in ascending order
def sort_by_distance(distances):
    return sorted(distances, key=lambda x: x[1])

# Predict using top-k neighbors
def predict_category(data, new_item, k=5):
    distances = calculate_distances(data, new_item)
    sorted_distances = sort_by_distance(distances)
    top_k = sorted_distances[:k]
    categories = [record[2] for record in top_k]
    majority_vote = Counter(categories).most_common(1)[0][0]
    return majority_vote

# --- Main Program ---
if __name__ == "__main__":
    dataset = load_data("shirt_data.csv")

    try:
        # Get user input
        size_input = int(input("Enter Shirt Size (1–5): "))
        quality_input = int(input("Enter Shirt Quality (1–10): "))
        new_item = (size_input, quality_input)

        # Predict category
        predicted_category = predict_category(dataset, new_item, k=5)
        print(f"\nNew shirt {new_item} is classified as: {predicted_category}")

    except ValueError:
        print("⚠️ Invalid input! Please enter integer values only.")
