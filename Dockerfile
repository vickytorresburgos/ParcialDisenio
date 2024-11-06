FROM python:3.10

WORKDIR /mutant_app

COPY /mutant_app /mutant_app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]