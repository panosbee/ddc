#!/usr/bin/env python3
"""
Admin User Creation Script for Diabetes Management Platform
===========================================================

This script automatically creates a default admin user during installation.
It's designed to be run as part of the install.bat process.

Default Admin Credentials:
- Username: admin
- Password: admin123
- Role: doctor

The script is idempotent - it won't create duplicate users if run multiple times.
"""

import os
import sys
from datetime import datetime
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

def load_environment():
    """Load environment variables from .env file"""
    # Try to load .env from current directory or parent directory
    env_paths = ['.env', '../.env', '../../.env']

    for env_path in env_paths:
        if os.path.exists(env_path):
            load_dotenv(env_path)
            print(f"✓ Loaded environment from: {env_path}")
            return True

    print("⚠ Warning: No .env file found. Using default MongoDB connection.")
    return False

def get_database_connection():
    """Establish connection to MongoDB database"""
    try:
        # Get MongoDB URI from environment or use default
        mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
        database_name = os.getenv('DATABASE_NAME', 'diabetes_db')

        print(f"Connecting to MongoDB: {mongo_uri}")
        client = MongoClient(mongo_uri)

        # Test the connection
        client.admin.command('ping')
        print("✓ MongoDB connection successful")

        db = client[database_name]
        return db

    except Exception as e:
        print(f"✗ MongoDB connection failed: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Ensure MongoDB is installed and running")
        print("2. Check if MongoDB service is started")
        print("3. Verify the MONGO_URI in your .env file")
        return None

def create_admin_user(db):
    """Create the default admin user"""
    try:
        doctors_collection = db.doctors

        # Check if admin user already exists
        existing_admin = doctors_collection.find_one({"account_details.username": "admin"})

        if existing_admin:
            print("✓ Admin user already exists - skipping creation")
            return True

        # Create admin user document
        admin_user = {
            "personal_details": {
                "name": "System Administrator",
                "surname": "Admin",
                "date_of_birth": "1980-01-01",
                "amka": "00000000000",  # Placeholder AMKA
                "contact_info": {
                    "phone": "+30 210 0000000",
                    "email": "admin@diabetes-center.local",
                    "address": "System Administrator"
                }
            },
            "account_details": {
                "username": "admin",
                "password_hash": generate_password_hash("admin123"),
                "role": "doctor"
            },
            "specialization": "Endocrinology",
            "created_at": datetime.utcnow(),
            "created_by": "system_installation",
            "is_admin": True
        }

        # Insert the admin user
        result = doctors_collection.insert_one(admin_user)

        if result.inserted_id:
            print("✓ Admin user created successfully!")
            print("  Username: admin")
            print("  Password: admin123")
            print("  Role: doctor")
            print("  ⚠ IMPORTANT: Change the default password after first login!")
            return True
        else:
            print("✗ Failed to create admin user")
            return False

    except Exception as e:
        print(f"✗ Error creating admin user: {str(e)}")
        return False

def main():
    """Main execution function"""
    print("=" * 60)
    print("Diabetes Management Platform - Admin User Setup")
    print("=" * 60)

    # Load environment variables
    load_environment()

    # Connect to database
    db = get_database_connection()
    if not db:
        sys.exit(1)

    # Create admin user
    success = create_admin_user(db)

    if success:
        print("\n✓ Admin user setup completed successfully!")
        print("\nNext steps:")
        print("1. Start the application with: run.bat")
        print("2. Open http://localhost:5173 in your browser")
        print("3. Login with username: admin, password: admin123")
        print("4. Change the default password immediately!")
    else:
        print("\n✗ Admin user setup failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()