import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = "25341679"
API_HASH = "1a0656fa7566a46075cfe3f21676424c"

# Get it from @Botfather in Telegram.
BOT_TOKEN = "6966212073:AAFyS64VJhonSo6LTLl3SI2JE_UL2bw6M1c"

# Create Your Own ApiKey From @TechZApiBot To Use Logo Api
API_KEY = "MIIBCgKCAQEA6LszBcC1LGzyr992NzE0ieY+BSaOW622Aa9Bd4ZHLl+TuFQ4lo4g
5nKaMBwK/BIb9xUfg0Q29/2mgIR6Zr9krM7HjuIcCzFvDtr+L0GQjae9H0pRB2OO
62cECs5HKhT5DZ98K33vmWiLowc621dQuwKWSQKjWf50XYFw42h21P2KXUGyp2y/
+aEyZ+uVgLLQbRA1dEjSDZ2iGRy12Mk5gpYc397aYp438fsJoHIgJ2lgMv5h7WY9
t6N/byY9Nw9p21Og3AoXSL2q/2IJ1WRUhebgAdGVMlV1fkuOQoEzR7EdpqtQD9Cs
5+bfo3Nhmcyvk5ftB0WkJ9z6bNZ7yxrP8wIDAQAB"


# Don't Change Anything Below This Line


if not API_ID or API_ID.strip() == "":
    API_ID = int(getenv("API_ID"))
if not API_HASH or API_HASH.strip() == "":
    API_HASH = getenv("API_HASH")
if not BOT_TOKEN or BOT_TOKEN.strip() == "":
    BOT_TOKEN = getenv("BOT_TOKEN")
if not API_KEY or API_KEY.strip() == "":
    API_KEY = getenv("API_KEY")


LOGO_API_URL1 = f"https://techzapi.azurewebsites.net/logo?api_key={API_KEY}&text="

LOGO_API_URL2 = (
    f"https://techzapi.azurewebsites.net//logo?api_key={API_KEY}&square=True&text="
)


if not API_KEY:
    print("Error: API_KEY Not Found!")
    print("Please Get Your Own ApiKey From @TechZApiBot To Use Logo Api")
    sys.exit()
elif API_KEY.strip() == "":
    print("Error: API_KEY Not Found!")
    print("Please Get Your Own ApiKey From @TechZApiBot To Use Logo Api")
    sys.exit()
