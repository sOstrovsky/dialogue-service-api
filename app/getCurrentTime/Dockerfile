FROM python:3.10

RUN pip install gunicorn

COPY get_current_time_svc.py /

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "get_current_time_svc:generate_openai_prompt"]