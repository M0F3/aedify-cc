# aedify-cc

## Run the project

Create a virtual environment and activate it

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install all required dependencies with

```bash
pip install -r requirements.txt
```

Create the environment file .env (for local development copy .env.develop)

Start the database with

```bash
docker compose up
```

Start the application with

```bash
fastapi dev --restart app/main.py
```

The application is now running on localhost port 8000

## api documentation

You can find the openapi documentation on
`http://localhost:8000/docs`
