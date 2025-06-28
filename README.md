# 🕷️ AI Web Scrapper

[![Deploy on Render](https://img.shields.io/badge/Live-Demo-brightgreen)](https://ai-web-scrapper-gorl.onrender.com)

An AI-assisted web scraper built using **Selenium**, **BeautifulSoup**, and **undetected-chromedriver** to automate data extraction from websites, with intelligent browsing behavior to bypass bot detection.

---

## 🔍 Features

- ✅ Automated web scraping using **Selenium + BeautifulSoup**
- 🛡️ Avoids bot detection using `undetected-chromedriver`
- ⚙️ Headless mode supported for server deployments
- 📄 Extracts structured data and saves it to a file
- ☁️ Deployed live on **Render**

---

## 🚀 Live Demo

🔗 [Visit the deployed app on Render](https://ai-web-scrapper-gorl.onrender.com)

---

## 📦 Tech Stack

- **Python 3.8+**
- `selenium`
- `bs4 (BeautifulSoup)`
- `undetected-chromedriver`
- `webdriver-manager`
- `Render` (for deployment)

---

## 🧪 How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/bhavin2004/ai-web-scrapper.git
cd ai-web-scrapper
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Scraper

```bash
streamlit run main.py
```

> Make sure you have Google Chrome installed and accessible in PATH.

---

## 🧠 How It Works

1. Launches a headless Chrome browser with stealth options.
2. Navigates to the target site (e.g., search via Google to mimic user behavior).
3. Parses page content using BeautifulSoup.
4. Extracts specific elements (titles, links, etc.).
5. Saves structured data (CSV/JSON format).

---

## 📁 Project Structure

```
├── scraper.py              # Main scraper logic
├── requirements.txt        # All Python dependencies
├── README.md               # This file
```

---

## 📌 Deployment Notes (Render)

- This app is deployed as a **background web service** on [Render](https://render.com).
- Headless mode is activated for remote scraping.
- Ephemeral storage: scraped files won't persist unless uploaded externally (add Google Drive integration if needed).

---

## 🛠️ Future Improvements

- Add support for multiple target websites
- Integrate proxy rotation / CAPTCHA solving
- Export results to Google Sheets or Drive
- Add Streamlit dashboard to visualize scraped data

---

## 📬 Contact

Created with ❤️ by **Bhavin Karangia**  
📧 [LinkedIn](https://www.linkedin.com/in/bhavin-karangia) • 🌐 [Portfolio Coming Soon]
