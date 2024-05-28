from app import app
from app.config import *

if __name__ == "__main__":
    # Run the application with Uvicorn (async) server
    import uvicorn
    uvicorn.run("main:app", host=APP_HOST, port=APP_PORT, reload=APP_RELOAD)