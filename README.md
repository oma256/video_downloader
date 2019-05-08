YouTube video converter and downloder
==============================
______________________________
Features
------------------------
* Django 2.1+
* PostgreSQL database support with psycopg2

installation and start project
------------------------
1. Install docker and docker-compose
2. Create .env file for environment variables:
```
    # DJANGO
    DJANGO_DEBUG=True
    DJANGO_SECRET_KEY=''
    DJANGO_ALLOWED_HOST=0.0.0.0
    DEFAULT_DATABASE_URL=postgres://db_user:db_password@db:5432/db_name
     
    # POSTGRES
    POSTGRES_USER=db_user
    POSTGRES_PASSWORD=db_password
    POSTGRES_DB=db_name
    PGDATA=/var/lib/postgresql/data
```
3. run the project as a command:
    ```sh
    $ docker-compose up --build
    ```
