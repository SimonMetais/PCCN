FROM python:3.12-slim

# Empeche la générationd es fichiers .pyc dans le conteneur
ENV PYTHONDONTWRITEBYTECODE=1
# S'assure que les print() sois affichés instantanement dans le terminal
ENV PYTHONUNBUFFERED=1

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy --clear
RUN pip uninstall virtualenv -y && pip uninstall pipenv -y

WORKDIR /app
COPY . /app

RUN ["chmod", "+x", "./scripts/start.sh"]
ENTRYPOINT ["sh", "-c", "./scripts/start.sh"]