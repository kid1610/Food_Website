
# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# Auto reload templates
TEMPLATES_AUTO_RELOAD = True

# Page Size
PAGE_SIZE = 8

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USERNAME = "hoangvanphuocrac@gmail.com"
MAIL_PASSWORD = "phuoc230899"
MAIL_USE_TLS = False
MAIL_USE_SSL = True

UPLOAD_FOLDER = r'D:\food_website\app\static\images'