# Python (Linux)
FROM python:3.9-slim

LABEL maintainer="Anastasia S. <aspirlidaki@github>"
LABEL description="PrivacyGuard Pro - Containerized Security Scanner"

#  φάκελο εργασίας μέσα στο container
WORKDIR /app

# Αντιγράφουμε τα αρχεία από τον υπολογιστή  στο container
COPY . .

# για  βιβλιοθήκες 
RUN pip install --no-cache-dir -r requirements.txt || true

# Η εντολή που θα τρέχει όταν ξεκινάει το container
ENTRYPOINT ["python", "main.py"]
CMD ["--help"]
