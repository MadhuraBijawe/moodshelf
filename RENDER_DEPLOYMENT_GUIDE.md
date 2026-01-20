# 🚀 Render Deployment Guide for MoodShelf

## ✅ Prerequisites Completed
- ✓ `requirements.txt` created
- ✓ `build.sh` created
- ✓ `settings.py` updated for production
- ✓ Environment variable support added

---

## 📝 Step-by-Step Deployment Process

### **Step 1: Push Your Code to GitHub**

1. Make sure all your changes are committed:
   ```bash
   git add .
   git commit -m "Add Render deployment configuration"
   git push origin main
   ```

2. If you don't have a GitHub repository yet:
   ```bash
   git init
   git add .
   git commit -m "Initial commit with Render config"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/moodshelf.git
   git push -u origin main
   ```

---

### **Step 2: Sign Up / Log In to Render**

1. Go to [https://render.com](https://render.com)
2. Click **"Get Started for Free"** or **"Sign In"**
3. Sign up with your **GitHub account** (recommended for easy integration)

---

### **Step 3: Create a PostgreSQL Database**

⚠️ **IMPORTANT: Create the database FIRST before the web service!**

1. From Render Dashboard, click **"New +"** button (top right)
2. Select **"PostgreSQL"**
3. Fill in the details:
   - **Name**: `moodshelf-db` (or any name you prefer)
   - **Database**: `moodshelf` (auto-filled)
   - **User**: `moodshelf` (auto-filled)
   - **Region**: Choose closest to you (e.g., Singapore, Frankfurt, Oregon)
   - **PostgreSQL Version**: 16 (latest)
   - **Instance Type**: **Free** (select this!)

4. Click **"Create Database"**
5. Wait 1-2 minutes for the database to be created
6. **IMPORTANT**: Once created, go to the database page and copy the **"Internal Database URL"** (you'll need this in Step 5)

---

### **Step 4: Create a Web Service**

1. From Render Dashboard, click **"New +"** button again
2. Select **"Web Service"**
3. Connect your GitHub repository:
   - Click **"Connect account"** if not connected
   - Find and select your **moodshelf** repository
   - Click **"Connect"**

---

### **Step 5: Configure Web Service Settings**

Fill in the following details:

#### **Basic Settings:**
- **Name**: `moodshelf` (this will be part of your URL)
- **Region**: Same as your database (e.g., Singapore)
- **Branch**: `main` (or `master` if that's your default)
- **Root Directory**: Leave blank (unless your Django project is in a subdirectory)
- **Runtime**: **Python 3**

#### **Build & Deploy Settings:**
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn moodshelf.wsgi:application`

#### **Instance Type:**
- Select **"Free"** (0.1 CPU, 512 MB RAM)

---

### **Step 6: Add Environment Variables**

Scroll down to **"Environment Variables"** section and click **"Add Environment Variable"**

Add these variables ONE BY ONE:

| Key | Value | Notes |
|-----|-------|-------|
| `SECRET_KEY` | Generate a new one* | See below for generator |
| `DEBUG` | `False` | Important for production! |
| `ALLOWED_HOSTS` | `moodshelf.onrender.com` | Replace with your actual Render URL |
| `DATABASE_URL` | Paste the Internal Database URL from Step 3 | From your PostgreSQL database |
| `EMAIL_HOST_USER` | `madhurabijawe@gmail.com` | Your Gmail |
| `EMAIL_HOST_PASSWORD` | `qtbn kuxg vyum suvf` | Your Gmail App Password |
| `PYTHON_VERSION` | `3.11.0` | Specify Python version |

**To generate a new SECRET_KEY:**
```python
# Run this in Python:
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use this online: https://djecrety.ir/

---

### **Step 7: Deploy!**

1. Click **"Create Web Service"** at the bottom
2. Render will automatically:
   - Clone your repository
   - Install dependencies from `requirements.txt`
   - Run `build.sh` (collect static files & migrate database)
   - Start your app with gunicorn

3. **Wait 3-5 minutes** for the first deployment
4. Watch the logs in real-time to see progress

---

### **Step 8: Verify Deployment**

1. Once you see **"Your service is live 🎉"**, click on your app URL
2. It will be something like: `https://moodshelf.onrender.com`
3. Test your application!

---

## 🔧 Important Notes

### **Free Tier Limitations:**
- Your app will **spin down after 15 minutes of inactivity**
- First request after inactivity takes **30-60 seconds** to wake up
- 750 hours/month free (enough for one always-on app)
- PostgreSQL database: 90-day expiration (you'll get an email to renew)

### **Update ALLOWED_HOSTS:**
After deployment, you need to update the `ALLOWED_HOSTS` environment variable:
1. Go to your web service dashboard
2. Click **"Environment"** tab
3. Update `ALLOWED_HOSTS` to your actual Render URL (e.g., `moodshelf.onrender.com`)
4. Save changes (this will trigger a redeploy)

---

## 🐛 Troubleshooting

### **Build Failed?**
- Check the logs for specific errors
- Common issues:
  - Missing dependencies in `requirements.txt`
  - Syntax errors in `build.sh`
  - Wrong Python version

### **App Crashes on Start?**
- Check if `DATABASE_URL` is set correctly
- Verify `ALLOWED_HOSTS` includes your Render domain
- Check logs for migration errors

### **Static Files Not Loading?**
- Make sure `whitenoise` is in `requirements.txt`
- Verify `STATIC_ROOT` is set in `settings.py`
- Check if `collectstatic` ran successfully in build logs

### **Database Connection Error?**
- Use the **Internal Database URL**, not the External one
- Make sure the database was created before the web service
- Verify `psycopg2-binary` is in `requirements.txt`

---

## 🔄 Updating Your App

To deploy updates:
1. Make changes locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your update message"
   git push origin main
   ```
3. Render will **automatically redeploy** (if auto-deploy is enabled)

---

## 📊 Monitoring

- **Logs**: Click "Logs" tab to see real-time application logs
- **Metrics**: View CPU, memory usage, and request metrics
- **Events**: See deployment history and events

---

## 💰 Upgrading (Optional)

If you need better performance:
- **Starter Plan**: $7/month
  - No spin-down
  - 0.5 CPU, 512 MB RAM
  - Better for production apps

---

## ✅ Checklist

Before deploying, make sure:
- [ ] Code is pushed to GitHub
- [ ] PostgreSQL database is created
- [ ] All environment variables are set
- [ ] `build.sh` has execute permissions (should be automatic)
- [ ] `ALLOWED_HOSTS` includes your Render domain

---

## 🎉 You're Done!

Your Django app should now be live on Render! 

**Your app URL**: `https://YOUR-SERVICE-NAME.onrender.com`

Need help? Check Render's documentation: https://render.com/docs/deploy-django
