import asyncio
import datetime
from typing import Optional

import beanie
import motor.motor_asyncio
import pydantic



async def main():
    await init_connection('beanie_quickstart')
    await create_a_user()
    await insert_multiple_users()
    await find_users()


    print("Done.")


async def init_connection(db_name: str):
    conn_str = f"mongodb://localhost:27017/{db_name}"
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)

    await beanie.init_beanie(database=client[db_name], document_models=[User])

    print(f"Connected to {db_name}.")


async def create_a_user():
    user_count = await User.count()
    if user_count > 0:
        print(f"Already have {user_count:,} users!")
        return

    print("Creating new user...")
    # Make sure you set up the DB connection before this line.
    loc = Location(city="Portland", state="OR", country="USA")
    user = User(name="Michael", email="michael@talkpython.fm", location=loc)
    print(f'User before save: {user}')

    await user.save()

    print(f'User after save: {user}')

async def insert_multiple_users():
    user_count = await User.count()
    if user_count >= 4:
        print(f"Already have {user_count:,} users!")
        return

    print("Creating new users...")
    # Make sure you set up the DB connection before this line.
    user_1 = User(name="Michael", email="michael@talkpython.fm", location=Location(city="Portland", state="OR", country="USA"))
    user_2 = User(name="Nick", email="michael123@talkpython.fm", location=Location(city="Portland", state="OR", country="USA"))
    user_3 = User(name="John", email="michael234@talkpython.fm", location=Location(city="Portland", state="OR", country="USA"))

    await User.insert_many([user_1, user_2, user_3])
    print("Inserting objects")

async def find_users():

    #All at once
    users: list[User] = await User.find(User.location.country == "USA").sort(-User.name).to_list() #first_or_none()
    print(users)
    user_query = User.find(User.location.country == "USA").sort(-User.name)
    async for user in user_query:
        user.password_hash = "a"
        await user.save()

class Location(pydantic.BaseModel):
    city: str
    state: str
    country: str


class User(beanie.Document):
    name: str
    email: str
    password_hash: Optional[str] = None

    created_date: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)
    last_login: datetime.datetime = pydantic.Field(default_factory=datetime.datetime.now)

    location: Location

    class Settings:
        name = "users"
        indexes = [
            "location.country"
        ]


if __name__ == '__main__':
    asyncio.run(main())