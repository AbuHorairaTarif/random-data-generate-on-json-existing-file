import random
import json

# Load your original JSON data
original_data = [
    {
    "name": "Luxury Hotel",
    "price": 250,
    "latitude": 34.0522,
    "longitude": -118.2437
  },
  {
    "name": "Cozy Inn",
    "price": 150,
    "latitude": 40.7128,
    "longitude": -74.0060
  },
  {
    "name": "Seaside Resort",
    "price": 300,
    "latitude": 25.7617,
    "longitude": -80.1918
  },
  {
    "name": "Mountain Retreat",
    "price": 180,
    "latitude": 39.5501,
    "longitude": -105.7821
  },
  {
    "name": "City View Hotel",
    "price": 200,
    "latitude": 51.5074,
    "longitude": -0.1278
  },
  {
    "name": "Budget Motel",
    "price": 50,
    "latitude": 42.3601,
    "longitude": -71.0589
  },
  {
    "name": "Elegant Lodge",
    "price": 300,
    "latitude": 37.7749,
    "longitude": -122.4194
  },
  {
    "name": "Riverside Inn",
    "price": 80,
    "latitude": 32.7767,
    "longitude": -96.7970
  },
  {
    "name": "Historic Manor",
    "price": 220,
    "latitude": 38.9072,
    "longitude": -77.0369
  },
  {
    "name": "Beachfront Resort",
    "price": 400,
    "latitude": 33.6891,
    "longitude": -117.8297
  },
  {
    "name": "Countryside Lodge",
    "price": 120,
    "latitude": 36.7783,
    "longitude": -119.4179
  },
  {
    "name": "Mountain View Hotel",
    "price": 180,
    "latitude": 41.8781,
    "longitude": -87.6298
  },
  {
    "name": "Modern Downtown Hotel",
    "price": 300,
    "latitude": 29.7604,
    "longitude": -95.3698
  },
  {
    "name": "Quaint Bed & Breakfast",
    "price": 90,
    "latitude": 44.9778,
    "longitude": -93.2650
  },
  {
    "name": "Rooftop Retreat",
    "price": 150,
    "latitude": 34.0522,
    "longitude": -118.2437
  },
  {
    "name": "Charming Cottage",
    "price": 70,
    "latitude": 40.7128,
    "longitude": -74.0060
  },
  {
    "name": "Lakeside Lodge",
    "price": 180,
    "latitude": 35.6895,
    "longitude": -105.9378
  },
  {
    "name": "Cosy Cabins",
    "price": 120,
    "latitude": 38.5816,
    "longitude": -121.4944
  },
  {
    "name": "Grand Plaza Hotel",
    "price": 250,
    "latitude": 34.0522,
    "longitude": -118.2437
  },
  {
    "name": "Tranquil Oasis",
    "price": 160,
    "latitude": 29.7604,
    "longitude": -95.3698
  },
  {
    "name": "Secluded Hideaway",
    "price": 80,
    "latitude": 40.7128,
    "longitude": -74.0060
  },
  {
    "name": "Chic Boutique Hotel",
    "price": 200,
    "latitude": 34.0522,
    "longitude": -118.2437
  },
  {
    "name": "Rustic Lodge",
    "price": 130,
    "latitude": 39.5501,
    "longitude": -105.7821
  },
  {
    "name": "Oceanfront Retreat",
    "price": 350,
    "latitude": 25.7617,
    "longitude": -80.1918
  },
  {
    "name": "Ski Resort Inn",
    "price": 180,
    "latitude": 45.4215,
    "longitude": -75.6972
  },
  {
    "name": "Art Deco Hotel",
    "price": 170,
    "latitude": 25.7617,
    "longitude": -80.1918
  },
  {
    "name": "Country Club Estate",
    "price": 300,
    "latitude": 34.0522,
    "longitude": -118.2437
  },
  {
    "name": "Serenity Lodge",
    "price": 110,
    "latitude": 37.7749,
    "longitude": -122.4194
  },
  {
    "name": "Rural Retreat",
    "price": 90,
    "latitude": 40.7128,
    "longitude": -74.0060
  }
]

# List of possible amenities
possible_amenities = [
    "wheel-chair available",
    "swimming pool",
    "kitchenette",
    "breakfast included",
    "spa",
    "fitness center",
    "free Wi-Fi",
    "restaurant",
    "parking",
    "pet-friendly",
    "concierge service"
]

# Function to add random amenities to each hotel
def add_random_amenities(hotel):
    num_amenities = random.randint(2, 6)  # Random number of amenities (between 2 and 6)
    random_amenities = random.sample(possible_amenities, num_amenities)
    hotel["amenities"] = random_amenities

# Adding random amenities to each hotel in the original data
for hotel in original_data:
    add_random_amenities(hotel)

# Print the modified data with random amenities
with open("output.json", "w") as output_file:
    json.dump(original_data, output_file, indent=2)

print("Data written to output.json")

