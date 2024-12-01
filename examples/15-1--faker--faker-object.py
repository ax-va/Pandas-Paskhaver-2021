#!/usr/bin/python3
"""
-- Appendix D
---- Generating fake data with Faker
------ Getting started with Faker
"""

import faker

fake = faker.Faker()
print(fake.name())  # Melvin Simmons
print(fake.name_male())  # Kelly Lewis
print(fake.name_female())  # Bonnie Wilkinson
print(fake.first_name())  # Andrew
print(fake.last_name())  # Bolton
print(fake.first_name_male())  # Thomas
print(fake.first_name_female())  # Jessica
print(fake.address())
# 0704 Lynn Lake Suite 555
# New Matthew, LA 44147
print(fake.street_address())  # 520 Bush Ville Suite 374
print(fake.city())  # Lake Paulton
print(fake.state())  # Mississippi
print(fake.postcode())  # 39776
print(fake.company())  # Turner Ltd
print(fake.catch_phrase())  # Reactive zero administration functionalities
print(fake.job())  # Administrator, sports
print(fake.url())  # https://diaz-martin.net/
print(fake.email())  # jsutton@example.com
print(fake.phone_number())  # 924.157.3963
print(fake.credit_card_number())  # 38270364979448
