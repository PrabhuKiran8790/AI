FROM python:3.9
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt --use-deprecated=legacy-resolver
COPY . .
# CMD streamlit run app.py
CMD streamlit run --server.port $PORT app.py
