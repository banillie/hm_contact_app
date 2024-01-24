from faker import Faker
import random
from contacts_model import Contact


def create_random_contacts(num_contacts=20):
    """helper function to run in the flask shell to create a specified
    number of random contacts with UK phone numbers using faker library."""

    fake = Faker("en_GB")  # Initialize Faker for UK locale

    for _ in range(num_contacts):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(['gmail.com', 'yahoo.com', 'hotmail.com'])}"
        phone_number = "+44" + "".join(
            fake.numerify("##########")
        )  # Generate UK phone number with faker

        contact = Contact(
            first=first_name, last=last_name, phone=phone_number, email=email
        )
        contact.save()  # Save the contact to the database
