import numpy as np
from sklearn.neighbors import NearestNeighbors

# -----------------------------
# Items
# -----------------------------
items = ["Movie1", "Movie2", "Movie3", "Movie4", "Movie5"]

# -----------------------------
# Improved Dataset
# -----------------------------
users = {
    "User1": [5, 3, 0, 1, 0],
    "User2": [4, 0, 0, 1, 2],
    "User3": [1, 1, 0, 5, 0],
    "User4": [0, 0, 5, 4, 4],
    "User5": [5, 4, 4, 0, 0],
    "User6": [0, 3, 5, 4, 5],
}

user_names = list(users.keys())
data = np.array(list(users.values()))

# -----------------------------
# Model
# -----------------------------
model = NearestNeighbors(metric='cosine')
model.fit(data)

# -----------------------------
# Select User
# -----------------------------
target_user_index = 0
target_user = user_names[target_user_index]

# -----------------------------
# Find Neighbors
# -----------------------------
distances, indices = model.kneighbors(
    [data[target_user_index]], n_neighbors=3
)

print(f"\nTarget User: {target_user}")
print("Nearest Neighbors:")

for i in range(1, len(indices[0])):
    neighbor_index = indices[0][i]
    print(f"- {user_names[neighbor_index]} (Distance: {distances[0][i]:.2f})")

# -----------------------------
# Recommendation Logic
# -----------------------------
recommendations = []

for i in range(len(items)):
    if data[target_user_index][i] == 0:
        for neighbor_index in indices[0][1:]:
            if data[neighbor_index][i] >= 3:   # strong rating
                recommendations.append(items[i])

# Remove duplicates
recommendations = list(set(recommendations))

# -----------------------------
# Output
# -----------------------------
if recommendations:
    print("\nRecommended Items:")
    for item in recommendations:
        print("-", item)
else:
    print("\nNo recommendations found.")