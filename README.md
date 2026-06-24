# Cyber Identity Sentinel

## Overview

Cyber Identity Sentinel is an AI-powered cybersecurity platform designed to detect fake profiles, impersonation attempts, and suspicious digital identities across online platforms.

The system combines machine learning, behavioral analysis, network intelligence, and risk scoring to help users identify potentially fraudulent accounts and assess digital trustworthiness.

---

## Problem Statement

The rapid growth of social media and online communities has increased the number of fake accounts, impersonation attacks, and malicious digital identities.

Existing systems often lack an integrated approach for profile analysis, risk assessment, and network-based threat visualization.

Cyber Identity Sentinel addresses this challenge by providing a unified platform for digital identity threat detection.

---

## Objectives

* Detect fake and suspicious online profiles
* Identify impersonation attempts
* Generate explainable risk scores
* Visualize relationships between suspicious accounts
* Provide AI-generated investigation insights
* Assist cybersecurity analysts in identity verification

---

## Key Features

### Dashboard

* Real-time project overview
* Security metrics and statistics
* Interactive user interface

### Profile Analysis

* Follower and following analysis
* Account age assessment
* Activity-based evaluation
* Automated profile investigation

### Risk Scoring Engine

* Risk score generation
* Low, Medium, High, and Critical classification
* Explainable threat indicators

### Graph Visualizations

* Suspicious account network analysis
* Relationship mapping
* Community visualization using NetworkX

### Cyber Identity Copilot

* AI-generated investigation summaries
* Risk explanation
* Security recommendations

---

## System Architecture

User

↓

Streamlit Frontend

↓

FastAPI Backend

↓

Machine Learning Models

↓

Risk Engine

↓

Visualization & Reports

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### Machine Learning

* Scikit-Learn
* NumPy
* Pandas

### Visualization

* Plotly
* Matplotlib
* NetworkX

### Other Libraries

* Requests
* Joblib
* RapidFuzz

---

## Project Structure

```text
CyberIdentitySentinel/
│
├── backend/
├── frontend/
├── services/
├── datasets/
├── tests/
│
├── prepare_dataset.py
├── requirements.txt
├── README.md
└── .gitignore
```


## Installation

Clone the repository:

```bash
git clone https://github.com/rajaputra164/CyberIdentitySentinel.git
```

Navigate to the project:

```bash
cd CyberIdentitySentinel
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the frontend:

```bash
streamlit run frontend/app.py
```

Run the backend:

```bash
uvicorn backend.main:app --reload
```

---

## Results

The platform successfully demonstrates:

* Fake profile detection
* Risk assessment
* Digital identity analysis
* Suspicious account visualization
* AI-assisted investigation support

---

## Future Scope

* Deepfake profile detection
* Real-time social media integration
* Graph Neural Networks
* OSINT intelligence modules
* Multi-platform identity correlation
* Advanced threat analytics

---

## Applications

* Cybersecurity Investigations
* Digital Identity Verification
* Fraud Detection
* Social Media Security
* Threat Intelligence

---

## Author

Rajaputra Hemanjali

Final Year Project

Cyber Identity Sentinel – AI-Powered Digital Identity Threat Detection Platform
