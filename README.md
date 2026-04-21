**Dementia Detection & Logging System**

A full-stack Machine Learning application designed to predict dementia status using clinical and MRI features. This project demonstrates a production-ready architecture, featuring a decoupled frontend/backend and a persistent database layer for model monitoring and future retraining.

**System Architecture**

The system is built with a focus on scalability and data integrity:

Frontend (Streamlit): A user-friendly interface for clinicians to input patient data and view real-time predictions.

Backend (FastAPI): An asynchronous REST API that handles inference requests, processes data through a Scikit-Learn pipeline, and manages database transactions.

Database (PostgreSQL): A relational database that logs every prediction request, enabling long-term model performance tracking and data collection for future retraining.

Data Pipeline: A Jupyter-based ETL process that cleans and migrates legacy clinical data into the normalized PostgreSQL schema.

**Key Features**

Machine Learning Inference: Utilizes a RidgeClassifier to categorize dementia status based on MMSE, eTIV, nWBV, and other clinical metrics.

Automated Logging: Every inference is automatically logged to the prediction_logs table, capturing both input features and the resulting prediction.

Batch Migration: Includes a custom ETL script to handle bulk insertion of 300+ historical records into the database via SQLAlchemy and Pandas.

Schema Enforcement: Strict data validation using Pydantic models to ensure inference quality and database consistency.
