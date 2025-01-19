from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
# Path to your Firefox profile folder
profile_path = r"C:\Users\MSI\AppData\Roaming\Mozilla\Firefox\Profiles\zyrv4z5j.default-release"

# Create a FirefoxProfile object and load your profile
profile = FirefoxProfile(profile_path)

# Configure Firefox options
options = Options()
options.headless = False  # Set to True for headless mode (no UI)

# Set proxy preferences using set_preference method
options.set_preference('network.proxy.type', 1)  # Manual proxy
options.set_preference('network.proxy.http', '127.0.0.1')  # Proxy address
options.set_preference('network.proxy.http_port', 8080)  # Proxy port
options.set_preference('network.proxy.ssl', '127.0.0.1')  # SSL proxy address
options.set_preference('network.proxy.ssl_port', 8080)  # SSL proxy port

# Add the profile to options
options.profile = profile

# Path to your geckodriver
geckodriver_path = r"C:\Dev\CHROMEDRIVER\geckodriver.exe"

# Initialize WebDriver for Firefox with the custom profile and GeckoDriver service
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

# Open the website
driver.get("https://academico.ucb.edu.bo/AcademicoNacional/administracion/ofertaDeMaterias")

# Now mitmproxy will log all requests and responses made by the browser
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "mat-select-4"))
)
button.click()

#SEMESTRE PRIMERO DEL 2025
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "mat-option-19"))
)
button.click()

time.sleep(2)
select_option = 'mat-option-'
for i in range(29, 53): 
    current_option = select_option + str(i)
    #PROGRAMA/CARRERA/DEPARTAMENTO
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mat-select-12"))
    )
    button.click()
    time.sleep(2)
    #SELECT CARRERA 
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, current_option))
    )
    button.click()
    time.sleep(2)