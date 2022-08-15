[![Black - Python Formatter](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

# Run

```Shell
$ docker-compose up
$ docker-compose down
# build without no-cache
$ docker-compose build --no-cache
```

# Sample Data insert

```Shell
$ docker-compose exec demo-app poetry run python -m api.migrate_db
```

# Go to mysql CLI

```Shell
$ docker-compose exec db mysql demo
# to set encoding utf8
mysql> CHARSET utf8;
```

# Test

```Shell
$ docker-compose run --entrypoint "poetry run pytest --asyncio-mode=auto" demo-app
```

# Swagger UI

```Shell
http://localhost:8000/docs#/
```
