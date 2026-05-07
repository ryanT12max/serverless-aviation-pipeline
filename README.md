# ✈️ Serverless Aviation Telemetry Pipeline

[![Live Dashboard](https://img.shields.io/badge/Live-Dashboard-0055ff?style=for-the-badge)](https://your-vercel-app-link-here.vercel.app/)
[![Oracle Cloud](https://img.shields.io/badge/Oracle_Cloud-F80000?style=for-the-badge&logo=oracle&logoColor=white)](https://cloud.oracle.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

## 📖 Project Overview
A fully serverless ETL (Extract, Transform, Load) pipeline designed to ingest, process, and visualize live aviation telemetry data over the Texas airspace. 

This project demonstrates the ability to architect cloud-native solutions, manage secure enterprise database connections via cryptographic wallets, and expose backend data via RESTful APIs for frontend consumption—all while maintaining a zero-compute footprint on local hardware.

## 🔗 Live Demo
**[View the Live Aviation Dashboard Here](https://your-vercel-app-link-here.vercel.app/)**

## 🛠️ Technology Stack
* **Cloud Provider:** Oracle Cloud Infrastructure (OCI)
* **Compute:** OCI Serverless Functions (Docker / Linux `amd64`)
* **Database:** Oracle Autonomous Database (Relational SQL)
* **Data Ingestion:** Python 3.11 (`requests`, `oracledb`)
* **API Layer:** Oracle REST Data Services (ORDS)
* **Frontend Visualization:** HTML5, Vanilla JS, Vercel Cloud Hosting
* **Third-Party API:** OpenSky Network REST API

## 🏗️ Architecture Flow
1. **Extract:** A serverless Python function triggered in OCI reaches out to the OpenSky Network API to pull raw, unstructured flight data for a specific geographic bounding box.
2. **Transform:** The Python script cleans the JSON response, handles missing variables, and normalizes the data into strict data types (Altitudes, Velocities, Callsigns).
3. **Load:** The function securely connects to an Oracle Autonomous Database using a cryptographic wallet (`tnsnames.ora`/`cwallet.sso`) and executes parameterized SQL `INSERT` statements to prevent SQL injection.
4. **Serve:** Oracle REST Data Services (ORDS) exposes the relational data as a secure, read-only JSON API.
5. **Visualize:** A lightweight frontend application hosted on Vercel fetches the ORDS API on load and dynamically populates a live data table for end-users.

## 🔐 Security & Operations Notes
* **Credential Management:** Database passwords and OCI wallet files are strictly `.gitignore`'d and injected via secure cloud environments. 
* **Containerization:** The OCI function was packaged and deployed using a custom Docker image managed via the Oracle Container Registry (OCIR).

## 🚀 Future Enhancements
* Implement a time-series graph using `Chart.js` on the frontend to track the average velocity of flights over time.
* Add automated OCI Event Triggers to execute the pipeline every 5 minutes on a cron schedule.
