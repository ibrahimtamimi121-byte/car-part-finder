# Installation & Setup Guide

## Prerequisites
- Python 3.8+
- Git
- Google Gemini API Key

## Local Development Setup

### 1. Clone Repository
```bash
git clone https://github.com/ibrahimtamimi121-byte/car-part-finder.git
cd car-part-finder
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
```bash
cp .env.example .env
```

Then edit `.env` and add your Gemini API Key:
```
GEMINI_API_KEY=your_actual_key_here
```

### 5. Run Application
```bash
python backend/app.py
```

Visit: http://localhost:5000

## Docker Deployment

### 1. Build Docker Image
```bash
docker build -t car-part-finder .
```

### 2. Run Container
```bash
docker run -e GEMINI_API_KEY=your_key -p 5000:5000 car-part-finder
```

### 3. Using Docker Compose
```bash
docker-compose up
```

## Getting Gemini API Key

1. Visit: https://ai.google.dev
2. Sign in with Google Account
3. Click "Get API Key"
4. Create API Key
5. Copy and paste in `.env`

## Testing

```bash
# Test server health
curl http://localhost:5000/api/health

# Test chatbot
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "مرحبا"}'
```

## Troubleshooting

### Port Already in Use
```bash
# Change port in .env
PORT=5001
```

### API Key Invalid
- Double-check the API key
- Make sure it's not expired
- Create a new one from Google AI Studio

### Database Issues
```bash
# Reset database
rm carparts.db
python backend/app.py
```

---

**For more help, check the documentation in `/docs` folder**
