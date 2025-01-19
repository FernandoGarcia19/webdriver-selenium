from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

# Path to your Firefox profile folder
profile_path = r"C:\Users\MSI\AppData\Roaming\Mozilla\Firefox\Profiles\zyrv4z5j.default-release"

# Create a FirefoxProfile object and load your profile
profile = FirefoxProfile(profile_path)

# Configure Firefox options
options = Options()
options.headless = False  # Set to True for headless mode (no UI)

# Add the profile to options
options.profile = profile

# Path to your geckodriver (make sure you download the correct version)
geckodriver_path = r"C:\Dev\CHROMEDRIVER\geckodriver.exe"

# Initialize WebDriver for Firefox with the custom profile and GeckoDriver service
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

# Open a website
driver.get("https://academico.ucb.edu.bo/AcademicoNacional/inicio")

