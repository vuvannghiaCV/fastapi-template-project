git clone https://github.com/vuvannghiaCV/fastapi-template-project.git
cd fastapi-template-project
pre-commit install
<!--  -->
poetry run  alembic   revision --autogenerate -m "init database"
poetry run  alembic     upgrade head
<!--  -->

fastapi
sqlalchemy
environs
loguru
uvicorn

alembic
SQLAlchemy
sqlmodel

psycopg2-binary
asyncpg

mysql-connector-python

pymysql

passlib
PyJWT
pyotp
qrcode

emails
Jinja2
