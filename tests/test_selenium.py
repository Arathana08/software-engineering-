from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # 1. Open application
    driver.get("http://localhost:5000")

    print("TEST 1: Application opened")

    # 2. Login
    email = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "password")

    email.send_keys("admin@example.com")
    password.send_keys("admin123")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait for dashboard
    wait.until(
        EC.url_contains("/dashboard")
    )

    print("TEST 2: Login successful")

    # 3. Request a resource
    driver.find_element(
        By.NAME, "resource_name"
    ).send_keys("Water")

    driver.find_element(
        By.CSS_SELECTOR,
        "form[action='/request-resource'] input[name='quantity']"
    ).send_keys("50")

    driver.find_element(
        By.NAME, "location"
    ).send_keys("Chennai Relief Camp")

    driver.find_element(
        By.CSS_SELECTOR,
        "form[action='/request-resource'] button"
    ).click()

    wait.until(
        EC.url_contains("/dashboard")
    )

    print("TEST 3: Resource request submitted")

    # 4. Check page content
    page = driver.page_source

    assert "Water" in page
    assert "Chennai Relief Camp" in page

    print("TEST 4: Request displayed successfully")

    # 5. Logout
    driver.find_element(By.LINK_TEXT, "Logout").click()

    wait.until(
        EC.url_contains("/")
    )

    print("TEST 5: Logout successful")

    print("\nALL SELENIUM TESTS PASSED!")

finally:
    driver.quit()