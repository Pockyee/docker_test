FROM python:3.10-slim
WORKDIR /test/
COPY app.py /test/app.py
RUN pip install requests
ENV LOG=1
CMD ["python3", "app.py"]