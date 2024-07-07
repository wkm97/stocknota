import platform
from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def hello():
  num1 = randint(0, 100)
  num2 = randint(0, 100)
  message = "Did you know {} + {} = {}? v{}".format(num1, num2, num1 + num2, platform.version())
  return message

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)