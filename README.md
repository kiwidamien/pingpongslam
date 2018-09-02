# Ping Pong Slam bot

## Initializing the database

For Heroku deployment
```bash
heroku shell
heroku pg:psql -f setup/pingpong.sql
```

For local deployment, run
```bash
psql -f setup/pingpong.sql
```

