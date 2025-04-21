FROM python:3.12-bookworm

WORKDIR /var/app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/var/app

RUN pip install --no-cache-dir poetry==1.8.2

COPY pyproject.toml poetry.lock ./


RUN poetry config virtualenvs.in-project true

RUN poetry install --no-interaction --only main --sync

RUN touch README.md


ENV PATH="/var/app/.venv/bin:$PATH"

COPY blog_app ./blog_app/

RUN .venv/bin/python -c "import fastapi; print(f'FastAPI version: {fastapi.__version__}')"

RUN .venv/bin/python -c "from blog_app.app import app; print('App imported successfully!')"



#
#RUN chmod +x ./entrypoint.sh
##
#ENTRYPOINT ["./entrypoint.sh"]

#CMD ["gunicorn", "app:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]