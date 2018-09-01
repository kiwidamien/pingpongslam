from flask import Flask

app = Flask('test app')

@app.route('/')
def index():
  return "Hello from Flask"

if __name__ == '__main__':
  app.run()
