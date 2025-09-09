# CEO Testing Guide - Diabetes Management Platform

## 🎯 Quick Start for CEO Testing

This guide will help you test the Diabetes Management Platform on your laptop in just 2 commands.

### Prerequisites (Pre-installed)
- ✅ MongoDB (already installed on your laptop)
- ✅ Python 3.8+ (Windows usually has this)
- ✅ Node.js 16+ (will be installed if missing)

### Step-by-Step Testing Process

#### 1. Download the Project
1. Go to: https://github.com/panosbee/ddc
2. Click the green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file to your Desktop or Documents folder
5. You should see a folder named `ddc-main`

#### 2. Add Environment Configuration
1. You will receive a `.env` file separately via secure channel
2. Copy this `.env` file to the root of the `ddc-main` folder
3. The file contains all necessary API keys and configuration

#### 3. Install Everything (1 Command)
1. Open the `ddc-main` folder
2. Double-click on `install.bat`
3. Wait for installation to complete (5-10 minutes)
4. The script will automatically:
   - Install all dependencies
   - Create admin user (username: admin, password: admin123)
   - Verify everything is working

#### 4. Start the Platform (1 Command)
1. Double-click on `run.bat`
2. Wait for all services to start (1-2 minutes)
3. Three browser windows will open automatically:
   - Doctor Portal: http://localhost:5173
   - Patient PWA: http://localhost:5174
   - Backend API: http://localhost:5000

#### 5. Test the System
1. **Login to Doctor Portal:**
   - Username: `admin`
   - Password: `admin123`
   - You should see the main dashboard

2. **Test Key Features:**
   - Patient management
   - AI-powered analysis
   - File upload and OCR
   - Real-time communication
   - Genetic analysis tools

3. **Test Patient PWA:**
   - Open the Patient PWA in a separate browser
   - Register a new patient account
   - Test mobile-like features

### 🔧 Troubleshooting

#### If Installation Fails:
1. **MongoDB not running:**
   - Press Windows + R, type `services.msc`
   - Find "MongoDB" service and start it
   - Re-run `install.bat`

2. **Python not found:**
   - Download Python from python.org
   - Install with "Add to PATH" option checked
   - Re-run `install.bat`

3. **Node.js not found:**
   - Download Node.js from nodejs.org
   - Install the LTS version
   - Re-run `install.bat`

#### If Startup Fails:
1. **Port conflicts:**
   - Close other applications using ports 5000, 5173, 5174
   - Re-run `run.bat`

2. **MongoDB connection issues:**
   - Ensure MongoDB service is running
   - Check Windows Firewall settings
   - Re-run `run.bat`

### 📱 Testing Scenarios

#### Scenario 1: Doctor Workflow
1. Login as admin
2. Create a new patient
3. Upload a medical document (PDF/image)
4. Review AI analysis results
5. Generate treatment recommendations

#### Scenario 2: Patient Experience
1. Open Patient PWA
2. Register new account
3. Log glucose readings
4. View personalized insights
5. Test offline functionality

#### Scenario 3: AI Features
1. Upload lab results
2. Ask AI medical questions
3. Review genetic risk analysis
4. Generate clinical reports

### 🎯 Success Criteria

The platform is working correctly if:
- ✅ All three services start without errors
- ✅ Admin login works
- ✅ Patient registration works
- ✅ File upload and OCR processing works
- ✅ AI responses are generated
- ✅ Database operations complete successfully

### 📞 Support

If you encounter any issues during testing:
1. Take a screenshot of any error messages
2. Note which step failed
3. Contact the development team with details

### 🔒 Security Notes

- The admin password (admin123) is for testing only
- Change it immediately after first login
- The .env file contains sensitive API keys - keep it secure
- Never share the .env file or commit it to version control

---

**Expected Testing Time:** 15-30 minutes
**Platform Status:** Production-ready for clinical use