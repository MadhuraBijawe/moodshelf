# 🎯 QUICK START - Render Deployment

## What to Select on Render:

### 1️⃣ First: Create PostgreSQL Database
- Click: **"New +" → "PostgreSQL"**
- Name: `moodshelf-db`
- Instance Type: **Free**
- Click "Create Database"
- **COPY THE INTERNAL DATABASE URL** (you'll need it!)

### 2️⃣ Second: Create Web Service
- Click: **"New +" → "Web Service"**
- Connect your GitHub repository
- Select: **Python 3** runtime
- Instance Type: **Free**

## Essential Configuration:

### Build Command:
```
./build.sh
```

### Start Command:
```
gunicorn moodshelf.wsgi:application
```

### Environment Variables (Add these!):
```
SECRET_KEY = <generate new one from https://djecrety.ir/>
DEBUG = False
ALLOWED_HOSTS = <your-app-name>.onrender.com
DATABASE_URL = <paste Internal Database URL from step 1>
EMAIL_HOST_USER = madhurabijawe@gmail.com
EMAIL_HOST_PASSWORD = qtbn kuxg vyum suvf
PYTHON_VERSION = 3.11.0
```

## ⚡ Quick Checklist:
- [ ] Push code to GitHub
- [ ] Create PostgreSQL database on Render
- [ ] Copy Internal Database URL
- [ ] Create Web Service
- [ ] Add all environment variables
- [ ] Click "Create Web Service"
- [ ] Wait 3-5 minutes
- [ ] Visit your app URL!

## 🔗 Your App URL:
`https://<your-service-name>.onrender.com`

---

**Need detailed instructions?** See `RENDER_DEPLOYMENT_GUIDE.md`
