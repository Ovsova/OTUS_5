FROM python:3.12-bookworm

WORKDIR /var/app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry ;  poetry install



RUN poetry install --no-dev --no-root

ENV PATH="/var/app/.venv/bin:$PATH"

COPY ./blog-app ./

#RUN chmod +x ./entrypoint.sh
#
#ENTRYPOINT ["./entrypoint.sh"]

#CMD ["gunicorn", "app:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]