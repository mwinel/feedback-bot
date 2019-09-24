# slack-feedback-bot
Just a simple slack feedback bot.

## Setup

- Install virtualenv

```bash
pip install virtualenv
```

- Create the application's virtual environment

```bash
virtualenv venv
```

- Activate the virtual environment

```bash
source venv/bin/activate
```

- Setup environment variables

  Create a `.env` file, copy the content of the `.env.example` file into it and fill the necessary credentials

- export enviromental variables

```bash
export $(cat .env)
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Start the development server

```bash
python app.py run_server
```

### Testing

Run `pytest -v --cov` to run tests

## Technologies Used

- [Flask](http://flask.pocoo.org/)
