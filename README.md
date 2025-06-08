# Cloner

This repository is configured for easy deployment on Render.

## Deployment Instructions

1. Fork this repository
2. Go to [Render Dashboard](https://dashboard.render.com)
3. Click on "New +" and select "Web Service"
4. Connect your GitHub repository
5. Use the following settings:
   - Name: cloner (or your preferred name)
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python3 -m BABYMUSIC`
6. Click "Create Web Service"

The application will be automatically deployed and you'll get a URL where your service is running.

## Environment Variables

Make sure to set up any required environment variables in the Render dashboard under the "Environment" section.

## Local Development

To run the project locally:

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python3 -m BABYMUSIC
   ``` 