# 📊 Web Data Extraction & Processing Pipeline

## 📌 Overview
This project demonstrates a simple end-to-end data pipeline that involves extracting data from a website using web scraping, cleaning and transforming raw data, and storing processed data locally and in the cloud (AWS S3).

## 🛠️ Tech Stack
- Python  
- BeautifulSoup  
- Pandas  
- AWS S3  

## ⚙️ Features
- Scraped quotes and authors from a public website  
- Cleaned data by removing duplicates, handling null values, and standardizing text format  
- Structured data into a Pandas DataFrame  
- Stored processed data in CSV format  
- Uploaded dataset to AWS S3 for scalable cloud storage  

## 📂 Project Structure
```bash

web_scraping_project/
│
├── scraper.py
├── quotes_cleaned.csv
├── README.md
```
## ▶️ How to Run

### 1. Install dependencies
pip install requests beautifulsoup4 pandas boto3

### 2. Run the script
python scraper.py

### 3. Output
- quotes_cleaned.csv will be generated  
- File can be uploaded to AWS S3  

## 📊 Sample Output

| Quote | Author | Scraped_Date |
|------|--------|-------------|
| Life is beautiful | Someone | 2026-03-23 |

## ☁️ AWS Integration
- Uploaded processed CSV file to AWS S3  
- Demonstrates basic cloud storage and scalability  
- Enables integration with analytics and data processing services  

## 🚀 Future Improvements
- Automate pipeline using scheduler (Cron jobs)  
- Implement Selenium for dynamic web scraping  
- Integrate AWS Lambda for serverless execution  
- Store data in databases (RDS / DynamoDB)  

## 💡 Key Learnings
- Built a basic ETL pipeline (Extract → Transform → Load)  
- Gained hands-on experience in web scraping  
- Learned data cleaning and preprocessing using Pandas  
- Understood cloud storage using AWS S3  

## 👩‍💻 Author
Alisha Verma
