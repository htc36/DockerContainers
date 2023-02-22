
FROM python:3.8-slim-buster

WORKDIR /app


# RUN "python -m venv venv"
# RUN "source venv/bin/activate"

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python ./src/predict.py -I ./examples/endofworld.jpg -S L
CMD ["python", "./src/predict.py", "-S", "L"]

