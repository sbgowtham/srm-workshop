import csv
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Function to generate random gender
def random_gender():
    return random.choice(["male", "female"])

# Function to generate random drug
def random_drug():
    return random.choice(["avil", "paracetamol", "metacin"])

# Generate dataset with 10 million records
num_records = 1_000_000
filename = "dataset.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    for i in range(1, num_records + 1):
        name = fake.name()
        drug = random_drug()
        gender = random_gender()
        amount = random.randint(500, 1000)
        writer.writerow([i, name, drug, gender, amount])

print(f"Dataset with {num_records} records created: {filename}")
