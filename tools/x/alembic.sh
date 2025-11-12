#!/bin/bash

# alembic revision --autogenerate -m "message"
# alembic revision --autogenerate -m "create files table"
alembic upgrade head
