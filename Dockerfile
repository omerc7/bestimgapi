FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
ENV FACE_API_KEY a90923e8c72e42f692ef7c37acb5e0b9
ENV FACE_API_ENDPOINT https://vocaassignment.cognitiveservices.azure.com/
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt