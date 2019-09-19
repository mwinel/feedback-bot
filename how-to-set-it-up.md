## How to set up your slack bot
Visit [https://api.slack.com](https://api.slack.com)

- Set up your ngrok tunnel for testing purposes on your machine
- Click on `Your Apps` and create a new app.
- In the `Features section`, check out for `Slash Command`. Add your slash command like this `/feedback-bot`, Request URL for the starter message e.g. `https://200cdd0b.ngrok.io/api/v1/bot/` and a short description of what your bot is meant to achieve.
- Click `Interactive Components`, turn it on and add Request URL for your dialog form like this `https://200cdd0b.ngrok.io/api/v1/bot/feedback-form`.
- Click `OAuth and Permissions`, Select Permission Scopes and add the following scopes; `channels:read`, `chat:write:bot`, and `chat:write:user`.
