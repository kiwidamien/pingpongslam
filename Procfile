web: gunicorn start_bot:app
init: heroku pg:psql -f setup/pingpong.sql
clean: pg:psql -f setup/clean.sql 
