import random

def generate_unique_numeric_user_id(existing_ids, min_value=1000, max_value=1000000):
    while True:
        user_id = random.randint(min_value, max_value)
        existing_ids.add(user_id)
        return user_id
        
        