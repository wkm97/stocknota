import platform
from random import randint
from litestar import Litestar, get

@get("/")
async def index() -> str:
  num1 = randint(0, 100)
  num2 = randint(0, 100)
  message = "Did you know {} + {} = {}? v{}".format(num1, num2, num1 + num2, platform.version())
  return message

app = Litestar([index])