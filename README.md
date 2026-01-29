# Credit Card Validator Service
# Overview

This project is a simple, containerized web application that validates credit card numbers using Luhn’s Algorithm.
The application provides a web-based user interface where a user can enter a credit card number and receive immediate feedback on whether the number is valid or invalid.

The service is designed to demonstrate:

* Backend service development

* Unit testing

* Containerization using Docker

* CI/CD using GitHub Actions

* Automated deployment to AWS

The application is intentionally kept lightweight and stateless to align with cloud-native and container-based deployment best practices.

# What This Application Does

* Accepts a credit card number via a web UI

* Validates the number using Luhn’s Algorithm

* Returns whether the credit card number is valid or invalid

* Exposes the application publicly via AWS

# Technology Stack

* **Language:** Python

* **Web Framework:** Flask

* **Testing:** Pytest

* **Containerization:** Docker

* **CI/CD:** GitHub Actions

* **Cloud Platform:** AWS

* **Deployment Target:** Container-based service (AWS ECS)

# Application Architecture

**High-level flow:**

User Browser

   ↓
   
Web UI (HTML)

   ↓
   
Flask Backend API

   ↓
   
Credit Card Validation Logic

   ↓
   
Validation Result


**Deployment flow:**

GitHub Repository

   ↓
   
GitHub Actions (CI/CD)

   ↓
   
Docker Image

   ↓
   
AWS Container Service

   ↓
   
Public URL


The application is stateless, which makes it easy to scale horizontally if required.

# Credit Card Validation Logic

The validation logic is implemented using Luhn’s Algorithm, a common checksum formula used to validate identification numbers such as credit cards.

The algorithm:

1. Processes digits from right to left

2. Doubles every second digit

3. Subtracts 9 if doubling results in a number greater than 9

4. Sums all digits

5. Validates the number if the total is divisible by 10

The core validation logic is implemented as a pure function, making it easy to test and maintain.

# Running the Application Locally
**Prerequisites**

Ensure the following are installed:

Python 3.10+

Docker

Git

# Run Without Docker (Local Development)

1. Clone the repository:
```
git clone https://github.com/Shaunl96/credit-card-validator-service.git

cd credit-card-validator-service
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the application:
```
python app.py
```
4. Open a browser and navigate to:
```
http://localhost:5000
```
# Run Using Docker

1. Build the Docker image:
```
docker build -t credit-card-validator .
```
2. Run the container:
```
docker run -p 5000:5000 credit-card-validator
```
3. Open a browser and navigate to:
```
http://localhost:5000
```
# Running Unit Tests

Unit tests are written using pytest and cover all required test cases specified in the assessment.

To run tests locally:

pytest

Tests are also executed automatically as part of the CI pipeline.

# CI/CD Pipeline (GitHub Actions)

A GitHub Actions workflow is configured to run on every push to the main branch.

**Pipeline Steps**

1. Check out the source code

2. Install application dependencies

3. Run unit tests

4. Build Docker image

5. Deploy to AWS

The pipeline ensures that only tested and validated code progresses toward deployment.

# AWS Deployment
**AWS Services Used**

**Amazon ECR** – Stores Docker images

**AWS ECS** – Runs the containerized application

**AWS IAM** – Manages permissions for deployment

These services were chosen to:

* Minimize infrastructure overhead

* Align with container-based deployment practices

* Stay within AWS Free Tier where possible

# Public Application URL

The deployed application can be accessed at:

http://credit-card-validator-alb-1135004809.eu-north-1.elb.amazonaws.com

# Repository Structure
```
credit-card-validator-service/
├── src/
│   └── __init__.py
│   └── app.py
│   └── validator.py
│   └── static/
│      └── styles.css
│   └── templates/
│      └── index.html
│
├── templates/
│   └── index.html
│
├── tests/
│   └── __init__.py
│   └── test_validator.py
│
├── .github/
│      └── workflows/
│         └── ci.yml
├── requirements.txt
├── Dockerfile
├── README.md
        
```
        
# Assumptions & Notes

* The application performs validation only, not authorization or payment processing

* No sensitive card data is stored or logged

* HTTPS, authentication, and rate limiting are not implemented as they are outside the scope of this assessment

* The application is designed to be easily extended with additional security or scaling features

# Future Improvements (Optional)

* Input validation and formatting improvements

* HTTPS termination via load balancer

* Rate limiting and basic security headers

* Kubernetes-based deployment (EKS)

* Environment-based configuration

Author

**Shaun Lamprecht**
