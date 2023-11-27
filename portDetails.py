import os

# Read the PORT environment variable from the .env file
portEnv = os.environ.get('PORT', default='5432')
assetsTable = "Assets"