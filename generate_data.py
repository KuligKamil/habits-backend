import uuid
import random
from datetime import datetime, timedelta
import faker

# Create an instance of the faker library
fake = faker.Faker()

def generate_session():
    # Generate a random ID
    session_id = str(uuid.uuid4())

    # Generate a start time between 1 and 30 days ago
    start_time = fake.date_time_between(start_date="-30d", end_date="now")

    # Generate an end time between start time and now
    end_time = fake.date_time_between(start_date=start_time, end_date="now")

    # Calculate the duration in seconds
    duration = int((end_time - start_time).total_seconds())

    # Generate a user for the session
    user = generate_user()

    # Generate a list of page views for the session
    page_views = [generate_page_view() for _ in range(random.randint(1, 10))]

    # Generate a country and region for the session
    country = generate_country()
    region = generate_region(country)

    # Return the session object
    return {
        "id": session_id,
        "startTime": start_time,
        "endTime": end_time,
        "duration": duration,
        "user": user,
        "pageViews": page_views,
        "country": country,
        "region": region
    }

def generate_user():
    # Generate a random user ID
    user_id = str(uuid.uuid4())

    # Generate a first session time between 30 and 90 days ago
    first_session = fake.date_time_between(start_date="-90d", end_date="-30d")

    # Generate a last session time between first session and now
    last_session = fake.date_time_between(start_date=first_session, end_date="now")

    # Return the user object
    return {
        "id": user_id,
        "firstSession": first_session,
        "lastSession": last_session,
    }

def generate_page_view():
    # Generate a random page view ID
    page_view_id = str(uuid.uuid4())

    # Generate a page title and URL using the faker library
    page_title = fake.sentence()
    page_url = fake.uri()

    # Return the page view object
    return {
        "id": page_view_id,
        "time": fake.date_time_this_month(),
        "url": page_url,
        "pageTitle": page_title,
    }

def generate_country():
    # Generate a random country name and code using the faker library
    country_name = fake.country()
    country_code = fake.country_code(representation="alpha-2")

    # Return the country object
    return {
        "id": country_code,
        "name": country_name,
    }

def generate_region(country):
    # Generate a random region name and code using the faker library
    region_name = fake.state()
    region_code = fake.zipcode()

    # Return the region object
    return {
        "id": region_code,
        "name": region_name,
        "country": country
    }

def generate_sessions(count):
    # Generate a list of session objects with the given count
    return [generate_session() for _ in range(count)]

print(generate_sessions(10))