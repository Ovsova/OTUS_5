FROM python:3.12-bookworm

WORKDIR /var/app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/var/app

#RUN pip install --no-cache-dir gunicorn==23.0.0

RUN pip install --no-cache-dir poetry==1.8.2

RUN poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock ./

RUN touch README.md

COPY blog_app ./


RUN poetry install --no-interaction --all-extras

RUN .venv/bin/gunicorn --version && \
    .venv/bin/uvicorn --version

ENV PATH="/var/app/.venv/bin:$PATH"

#
RUN chmod +x ./entrypoint.sh
#
ENTRYPOINT ["./entrypoint.sh"]

#CMD ["gunicorn", "app:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]