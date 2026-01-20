# 🔧 Render Deployment Troubleshooting

## ❌ Error: 400 Bad Request

### **Symptoms:**
- Browser shows "Bad Request (400)"
- Console shows: `Failed to load resource: the server responded with a status of 400`
- `/favicon.ico` and `(index)` both fail with 400

### **Cause:**
Django is rejecting requests because the hostname is not in `ALLOWED_HOSTS`.

### **Solution:**

#### ✅ **Fix Applied:**
I've updated `settings.py` to automatically detect and allow your Render hostname using the `RENDER_EXTERNAL_HOSTNAME` environment variable.

#### **What You Need to Do:**

1. **Commit and push the updated settings.py:**
   ```bash
   git add moodshelf/settings.py
   git commit -m "Fix ALLOWED_HOSTS for Render deployment"
   git push origin main
   ```

2. **Wait for Render to redeploy** (automatic, takes 2-3 minutes)

3. **Refresh your browser** and the error should be gone!

---

## 🔍 Other Common Errors:

### **Error: DisallowedHost at /**
**Cause:** Same as 400 - ALLOWED_HOSTS issue  
**Solution:** Already fixed above!

### **Error: Static files not loading (CSS/JS missing)**
**Cause:** Static files not collected or whitenoise not configured  
**Solution:**
1. Check if `whitenoise` is in `requirements.txt` ✅ (already added)
2. Check if `collectstatic` ran in build logs
3. Verify `STATIC_ROOT` is set ✅ (already configured)

### **Error: Database connection failed**
**Cause:** Wrong DATABASE_URL or database not created  
**Solution:**
1. Go to Render dashboard → PostgreSQL database
2. Copy the **Internal Database URL** (not External!)
3. Update `DATABASE_URL` environment variable in your Web Service
4. Save and redeploy

### **Error: Application failed to respond**
**Cause:** App crashed during startup  
**Solution:**
1. Check Render logs (click "Logs" tab)
2. Look for Python errors or missing dependencies
3. Common issues:
   - Missing package in `requirements.txt`
   - Database migration errors
   - Import errors

### **Error: ModuleNotFoundError**
**Cause:** Missing package in `requirements.txt`  
**Solution:**
1. Add the missing package to `requirements.txt`
2. Commit and push
3. Render will redeploy automatically

---

## 📊 How to Check Logs on Render:

1. Go to your Web Service dashboard
2. Click **"Logs"** tab on the left
3. Look for errors in red
4. Common log sections:
   - **Build logs:** Shows `pip install` and `collectstatic`
   - **Deploy logs:** Shows app startup with gunicorn
   - **Application logs:** Shows Django errors and requests

---

## ✅ Verification Checklist:

After deployment, verify:
- [ ] App loads without 400 error
- [ ] Static files (CSS/JS) are loading
- [ ] Database connections work
- [ ] Admin panel accessible at `/admin`
- [ ] No errors in Render logs

---

## 🆘 Still Having Issues?

1. **Check environment variables:**
   - Go to Environment tab
   - Verify all required variables are set
   - No typos in variable names

2. **Check build logs:**
   - Look for failed `pip install` commands
   - Check if migrations ran successfully
   - Verify `collectstatic` completed

3. **Test locally first:**
   ```bash
   # Set environment variables locally
   set DEBUG=False
   set ALLOWED_HOSTS=localhost,127.0.0.1
   
   # Run the app
   python manage.py runserver
   ```

4. **Common fixes:**
   - Clear browser cache
   - Try incognito/private mode
   - Wait 5 minutes after deployment
   - Check if service is "Live" (green dot)

---

## 📞 Need More Help?

- Render Docs: https://render.com/docs/deploy-django
- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- Check Render Community: https://community.render.com/

---

**Current Status:** ✅ 400 error should be fixed after you push the updated code!
