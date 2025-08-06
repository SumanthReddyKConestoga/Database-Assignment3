import os
import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

# 1. Start browser
driver = webdriver.Chrome()

try:
    # 2. Navigate & submit
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("pass123")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    # 3. Confirm success page
    assert "database updated" in driver.page_source

    # 4. Confirm DB insert
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME")
    )
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users WHERE username=%s", ("testuser",))
    count = cur.fetchone()[0]
    assert count >= 1

    print("✅ Test passed – entry found in database")

finally:
    driver.quit()
