# FAQ Chatbot Frontend

[![Flask](https://img.shields.io/badge/Flask-2.0.3-blue)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-CDN-38b2ac)](https://tailwindcss.com/)

A lightweight web interface for an AI-powered FAQ chatbot using Flask and Tailwind CSS CDN.

## Features ✨
- Simple setup without Node.js
- CDN-based Tailwind CSS
- Real-time chat interface
- Mobile-responsive design
- Error handling

## Prerequisites 📋
- Python 3.9+
- Modern web browser
- Backend API URL

## Installation 🛠️

### 1. Clone Repository
```bash
git clone https://github.com/nekosaif/faq-chatbot-frontend.git
cd faq-chatbot-frontend
```

### 2. Python Setup
```bash
# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## Configuration ⚙️

1. Create `.env` file:
```bash
cp .env.example .env
```

2. Edit `.env`:
```env
FLASK_DEBUG=0
BACKEND_URL=https://your-backend-api.com/ask
```

## Project Structure 📁
```
faq-chatbot-frontend/
├── app.py
├── requirements.txt
├── static/
│   └── styles.css (optional custom styles)
└── templates/
    └── index.html
```

## Development 🚀

```bash
# Start Flask development server
flask run --debug
```

Visit: http://localhost:5000

## Deployment 🐳

### Heroku Deployment
1. Create app on Heroku
2. Set environment variables:
```bash
heroku config:set FLASK_DEBUG=0 BACKEND_URL=your-api-url
```

3. Deploy:
```bash
git push heroku main
```

## Customization 🎨

To modify styles:
1. Edit inline Tailwind classes in `templates/index.html`
2. (Optional) Add custom CSS in `static/styles.css`
```html
<!-- Add this to index.html head -->
<link href="{{ url_for('static', filename='styles.css') }}" rel="stylesheet">
```

## Troubleshooting 🔧

**Common Issues:**
1. **Missing Styles**
   - Check Tailwind CDN is loading
   - Verify internet connection

2. **API Connection Issues**
   - Confirm backend URL is correct
   - Check browser console for errors

**Production Notes:**
- Set `FLASK_DEBUG=0` in production
- Consider downloading Tailwind CSS for production:
  ```html
  <!-- Replace CDN with local version -->
  <link href="{{ url_for('static', filename='tailwind.min.css') }}" rel="stylesheet">
  ```
  [Download latest version](https://cdn.tailwindcss.com)

## License 📄
MIT License - See [LICENSE](LICENSE)

