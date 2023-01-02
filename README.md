Münster’s Givebox-Network – Wir eröffnen für Giveboxen in Münster eine digitale Community und schaffen einfachen digitalen Zugang zu Infos, Events und Austausch mit Nutzern und Paten.

# Getting Started

Setup a database
1. Create an .env file with at minimum POSTGRES_HOST_AUTH_METHOD=trust or POSTGRES_PASSWORD=foobar
2. Start the database `docker-compose up postgres`

Inside fastapi-backend dir
1. Create venv `virtualenv -p python3.11 .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt` (or use requirements.in if there are issue with versions on your system)
3. run `export DEV=1; ./start.sh` (sets up the database and runs the app with uvicorn)
4. Checkout entrypoints http://127.0.0.1:8081/docs

Inside svelte-frontend dir
1. `npm install`
2. run `npm run dev -- --open`
