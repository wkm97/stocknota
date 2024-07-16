import uvicorn

if __name__ == '__main__':
  uvicorn.run("projects.app.asgi:app", host='0.0.0.0', port=8000, reload=True)