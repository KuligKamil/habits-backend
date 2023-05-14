import typing

import strawberry


# def get_books():
#     return [
#         Book(
#             title="The Great Gatsby",
#             author="F. Scott Fitzgerald",
#         ),
#     ]

# @strawberry.type
# class Book:
#     title: str
#     author: "Autor"

# @strawberry.type
# class Author:
#     name: str
#     books: typing.List[Book]

# @strawberry.type
# class Query:
#     # books: typing.List[Book]
#      books: typing.List[Book] = strawberry.field(resolver=get_books)


# import strawberry
# from typing import List
# from datetime import datetime

# @strawberry.type
# class User:
#     id: strawberry.ID
#     first_session: datetime
#     last_session: datetime

# @strawberry.type
# class PageView:
#     id: strawberry.ID
#     time: datetime
#     url: str
#     page_title: str

# @strawberry.type
# class Country:
#     id: strawberry.ID
#     name: str

# @strawberry.type
# class Region:
#     id: strawberry.ID
#     name: str
#     country: Country

# @strawberry.type
# class Session:
#     id: strawberry.ID
#     start_time: datetime
#     end_time: datetime
#     duration: int
#     user: User
#     page_views: List[PageView]
#     country: Country
#     region: Region

# @strawberry.type
# class Query:
#     sessions: List[Session]

# @strawberry.type
# class Mutation:
#     create_session: Session

# schema = strawberry.Schema(query=Query, mutation=Mutation)

# # schema = strawberry.Schema(query=Query)
# from typing import List
# from datetime import datetime, timedelta
# from random import randint, choice
# from faker import Faker

# fake = Faker()

# # Generate random data
# COUNTRIES = [Country(id=str(i), name=fake.country()) for i in range(5)]
# REGIONS = [Region(id=str(i), name=fake.state(), country=choice(COUNTRIES)) for i in range(10)]
# USERS = [User(id=str(i), first_session=fake.date_time_this_year(before_now=True, after_now=False), last_session=fake.date_time_this_year(before_now=False, after_now=True)) for i in range(10)]
# PAGE_VIEWS = [PageView(id=str(i), time=fake.date_time_this_year(), url=fake.url(), page_title=fake.sentence()) for i in range(50)]
# SESSIONS = [Session(id=str(i), start_time=fake.date_time_this_year(), end_time=fake.date_time_this_year(), duration=randint(60, 3600), user=choice(USERS), page_views=PAGE_VIEWS[:randint(1, 10)], country=choice(COUNTRIES), region=choice(REGIONS)) for i in range(20)]

# COUNTRIES = [Country(id=str(i), name=fake.country()) for i in range(5)]
# REGIONS = [Region(id=str(i), name=fake.state(), country=choice(COUNTRIES)) for i in range(10)]
# USERS = [User(id=str(i), first_session=fake.date_time_this_year(before_now=True, after_now=False), last_session=fake.date_time_this_year(before_now=False, after_now=True), country=choice(COUNTRIES)) for i in range(10)]
# PAGE_VIEWS = [PageView(id=str(i), time=fake.date_time_this_year(), url=fake.url(), page_title=fake.sentence()) for i in range(50)]
# SESSIONS = [Session(id=str(i), start_time=fake.date_time_this_year(), end_time=fake.date_time_this_year(), duration=randint(60, 3600), user=choice(USERS), page_views=PAGE_VIEWS[:randint(1, 10)], country=choice(COUNTRIES), region=choice(REGIONS)) for i in range(20)]

# @strawberry.type
# class Query:
#     @strawberry.field
#     def sessions() -> List[Session]:
#         return SESSIONS
    
#     @strawberry.field
#     def users_by_country(country_id: strawberry.ID) -> List[User]:
#         return [user for user in USERS if user.country.id == country_id]

# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def create_session(session_input: SessionInput) -> Session:
#         # create a new session object based on input
#         new_session = Session(id=str(len(SESSIONS)+1), start_time=session_input.start_time, end_time=session_input.end_time, duration=session_input.duration, user=session_input.user, page_views=session_input.page_views, country=session_input.country, region=session_input.region)
        
#         # add the new session object to the list of sessions
#         SESSIONS.append(new_session)
        
#         return new_session

# schema = strawberry.Schema(query=Query, mutation=Mutation)
import strawberry
from typing import List
from datetime import datetime, timedelta
from random import randint, choice
from faker import Faker

# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def create_session(session_input: SessionInput) -> Session:
#         # create a new session object based on input
#         new_session = Session(id=str(len(SESSIONS)+1), start_time=session_input.start_time, end_time=session_input.end_time, duration=session_input.duration, user=session_input.user, page_views=session_input.page_views, country=session_input.country, region=session_input.region)
        
#         # add the new session object to the list of sessions
#         SESSIONS.append(new_session)
        
#         return new_session

@strawberry.type
class Country:
    id: strawberry.ID
    name: str

@strawberry.type
class Region:
    id: strawberry.ID
    name: str
    country: Country

@strawberry.type
class User:
    id: strawberry.ID
    first_session: datetime
    last_session: datetime
    country: Country

@strawberry.type
class PageView:
    id: strawberry.ID
    time: datetime
    url: str
    page_title: str

@strawberry.type
class Session:
    id: strawberry.ID
    start_time: datetime
    end_time: datetime
    duration: int
    user: User
    page_views: List[PageView]
    country: Country
    region: Region

@strawberry.input
class SessionInput:
    start_time: datetime
    end_time: datetime
    duration: int
    user: User
    page_views: List[PageView]
    country: Country
    region: Region

@strawberry.type
class Query:
    @strawberry.field
    def sessions() -> List[Session]:
        return SESSIONS
    
    @strawberry.field
    def users_by_country(country_id: strawberry.ID) -> List[User]:
        return [user for user in USERS if user.country.id == country_id]

fake = Faker()

# Generate random data
COUNTRIES = [Country(id=str(i), name=fake.country()) for i in range(5)]
REGIONS = [Region(id=str(i), name=fake.state(), country=choice(COUNTRIES)) for i in range(10)]
USERS = [User(id=str(i), first_session=fake.date_time_this_year(before_now=True, after_now=False), last_session=fake.date_time_this_year(before_now=False, after_now=True), country=choice(COUNTRIES)) for i in range(10)]
PAGE_VIEWS = [PageView(id=str(i), time=fake.date_time_this_year(), url=fake.url(), page_title=fake.sentence()) for i in range(50)]
SESSIONS = [Session(id=str(i), start_time=fake.date_time_this_year(), end_time=fake.date_time_this_year(), duration=randint(60, 3600), user=choice(USERS), page_views=PAGE_VIEWS[:randint(1, 10)], country=choice(COUNTRIES), region=choice(REGIONS)) for i in range(20)]

schema = strawberry.Schema(query=Query)