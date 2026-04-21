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

### **EDUC**

* **Years of education** completed
* Often used as a proxy for *cognitive reserve* (higher education may delay symptom onset)

---

### **SES (Socioeconomic Status)**

* A categorical ranking (often 1–5)
* Lower numbers usually indicate **higher socioeconomic status**
* Can correlate with health outcomes and access to care

---

### **MMSE (Mini-Mental State Examination)**

* A widely used cognitive test score (range: **0–30**)
* Higher scores = better cognitive function
* Rough interpretation:

  * 24–30 → normal
  * 18–23 → mild impairment
  * <18 → more severe impairment

---

### **CDR (Clinical Dementia Rating)**

* Measures dementia severity
* Typical values:

  * 0 → no dementia
  * 0.5 → mild
  * 1 → moderate
  * 2 → severe

---

### **eTIV (Estimated Total Intracranial Volume)**

* Total volume inside the skull (in mm³)
* Used to normalize brain volume measurements
* Helps account for head size differences

---

### **nWBV (Normalized Whole Brain Volume)**

* Brain volume as a **proportion of intracranial volume**
* Lower values → more brain atrophy (often linked to dementia progression)

---

### **ASF (Atlas Scaling Factor)**

* A scaling factor used during MRI processing
* Adjusts individual brain scans to match a standard brain atlas
* Inversely related to head size (larger heads → smaller ASF)

