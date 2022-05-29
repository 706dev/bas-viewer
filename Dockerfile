FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('userUsername', 'userEmail', 'userPassword')" | python manage.py shell