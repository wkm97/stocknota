import time
import uvicorn
import sys
print(sys.path)

from projects.app.asgi import app
if __name__ == '__main__':
  uvicorn.run(app, host='0.0.0.0', port=8000)
  # while True:
  #   # print('heartbeat')
  #   time.sleep(6)