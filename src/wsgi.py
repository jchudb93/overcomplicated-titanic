import uvicorn
from app import create_app

app, _ = create_app()
uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")