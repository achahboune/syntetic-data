from faker import Faker
import pandas as pd

# Create a Faker instance
fake = Faker()

# Generate synthetic data
num_records = 100  # Number of records you want to create
data = []
for _ in range(num_records):
    name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.address()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80)
    job = fake.job()
    
    data.append({
        'Name': name,
        'Email': email,
        'Phone Number': phone_number,
        'Address': address,
        'Date of Birth': date_of_birth,
        'Job': job,
    })

# Convert the data list to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('synthetic_data.csv', index=False)

# Print the first few records of the generated data
print(df.head())
