FROM python:3.12.1-alpine
WORKDIR /dokerized_brain_tumor
ADD . /dokerized_brain_tumor
RUN pip install -r requirements.txt
CMD ["python","brain.py"]