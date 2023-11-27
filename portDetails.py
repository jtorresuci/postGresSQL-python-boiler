from decouple import config

# Read the PORT environment variable from the .env file
portEnv = config('PORT', default='5432')