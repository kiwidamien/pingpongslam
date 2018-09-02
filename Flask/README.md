## Local deployment

To do local testing, please export `DATABASE_URL` ahead of time as follows:
```bash
export DATABASE_URL=postgres://127.0.0.1:5432/pingpong
```
Here username is your Postgres username.


You will need to do this on _each_ shell you have open (i.e. if you open a new terminal window, you will need to run this command again before running Flask).

To test or connect to the Heroku version, use `heroku config` and copy the `DATABASE_URL` environment variable to your local shell.
