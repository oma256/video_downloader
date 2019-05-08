
YouTube video converter and downloder
==============================

## Run via docker
1. Install docker and docker-compose
```.bash
$ sudo pacman -S docker
$ sudo pacman -S docker-compose
```
2. Start project
```.bash
$ docker-compose up --build
```

### Environment variables 
Сreate .env file at the root of the project, and enter the following variables

| Key    | Description   |    Default value  |
| :---         |     :---      |          :--- |
| `DJANGO_SECRET_KEY`  | my secret key  | secret-key              |
| `DJANGO_DEBUG`  | Debug mode True or False  | True              |
| `DJANGO_ALLOWED_HOST`| Allowed host | 0.0.0.0,127.0.0.1 |
| `DEFAULT_DATABASE_URL`  | postgres://user:password@host:port/database_name | postgres://postgres:postgres@db:5432/video_converter |
| `POSTGRES_USER`  | Postgres username |   postgres   |
| `POSTGRES_PASSWORD`  | Postgres password |  postgres    |
| `POSTGRES_DB`  | Postgres database name | video-converter-db |
| `PGDATA`  | Postgres volume | /var/lib/postgresql/data |
