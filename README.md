# Database Automation Assignment 3

**Web Application with Database Integration & Automated Testing**

---

## 📌 Author

**Sumanth Reddy K**
GitHub: [SumanthReddyKConestoga](https://github.com/SumanthReddyKConestoga)
Repository: [https://github.com/SumanthReddyKConestoga/Database-Assignment3.git](https://github.com/SumanthReddyKConestoga/Database-Assignment3.git)

---

## 🚀 Overview

This repository embodies a forward-thinking yet tradition-honoring solution: a **Flask**‑based web application that captures user credentials, funnels them into a **MySQL** database, and validates end-to-end integrity via **Selenium** automation. It is structured to deliver maximum clarity, maintainability, and automated deliverables for enterprise-grade workflows.

**Key Deliverables:**

* User‑centric login form (Flask)
* Database schema and provisioning (MySQL + Docker Compose)
* Automated UI & data validation (Selenium)
* Infrastructure as Code (Docker Compose)
* Comprehensive project documentation

---

## 🗂️ Folder Structure

```plaintext
DATABASE-ASSIGNMENT3/
├── .env                    # Environment variables (DB credentials)
├── docker-compose.yml      # MySQL & Adminer orchestration
├── schema_changes.sql      # Database schema setup
├── app.py                  # Flask application entrypoint
├── templates/
│   └── login.html          # Login form template
├── tests/
│   └── test_login.py       # Selenium end-to-end test
├── requirements.txt        # Python dependencies
└── README.md               # This document
```

---

## 🛠️ Prerequisites

* **Docker** & **Docker Compose**
* **Python 3.8+**
* **Google Chrome** & **ChromeDriver** (in PATH)
* **Git**

---

## 🔧 Setup & Execution

1. **Clone the repository**

   ```bash
   git clone https://github.com/SumanthReddyKConestoga/Database-Assignment3.git
   cd Database-Assignment3
   ```

2. **Configure environment**

   * Rename `.env.example` to `.env`
   * Populate:

     ```dotenv
     DB_HOST=localhost
     DB_USER=root
     DB_PASS=YourRootPassword
     DB_NAME=usersdb
     ```

3. **Launch infrastructure**

   ```bash
   docker-compose up -d
   ```

4. **Initialize database schema**

   ```bash
   mysql -u root -p$DB_PASS < schema_changes.sql
   ```

5. **Install Python dependencies**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate     # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

6. **Start the Flask app**

   ```bash
   python app.py
   ```

7. **Run Selenium tests**

   ```bash
   python -m pytest tests/test_login.py
   ```

---

## 💡 Theory 

* **Flask** acts as the concierge, presenting a login page and routing your credentials.
* **MySQL** is the secure filing cabinet, storing each submission with an auto‑increment ID.
* **Docker Compose** orchestrates your database and Adminer GUI in containers—cross‑platform and dependable.
* **Selenium** is the tireless QA robot, ensuring the UI works and the data lands exactly where it should.

---

## 📈 Quality Assurance & CI/CD

* Integrate with GitHub Actions to automate:

  * Linting & formatting
  * Infrastructure bring-up & teardown
  * End-to-end Selenium test execution
  * Security scans (e.g., Dependabot, Trivy)

---

## 🤝 Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "feat: add amazing feature"`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

