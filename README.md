# SafePay - Secure Payment System

A secure, Flask-based online payment system with advanced cryptography, fraud detection, and role-based access control.

**Live Demo (Deployed App on Vercel):** https://safepay-online.vercel.app/
*(Note: If the exact URL differs, check your Vercel dashboard.)*

## Overview

SafePay simulates a banking application with a focus on security and machine learning. 
- **User Roles:** Distinct `admin` and `user` functionalities.
- **Transactions:** Users can securely transfer funds.
- **Cryptography:** Transaction data is AES-encrypted, digitally signed (RSA), and uses Searchable Encryption and Paillier Homomorphic Encryption for secure balance/amount storage.
- **Fraud Detection:** Transactions are evaluated by an augmented machine learning model (`scikit-learn`) based on age, amount, balance, card type, and expiry date.

## Default Accounts

To explore the application out of the box, use these pre-configured accounts (populated when the database is initialized):

### Admin Account
- **Username:** `admin`
- **Password:** `admin`
- **Role:** Admin
- **Features:** View all users, reverse (undo) transactions, view global transaction logs.

### Test User Accounts
- **Username:** `user1`
- **Password:** `1234`
- **Role:** User
- **Balance:** ₹50,000

- **Username:** `saksham`
- **Password:** `hello123`
- **Role:** User
- **Balance:** ₹50,000

*Note: You can also create new user accounts via the Signup page.*

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MongoDB (pymongo)
- **Machine Learning:** scikit-learn, numpy, pandas
- **Cryptography:** cryptography (AES, RSA), custom Paillier and Searchable Encryption implementations
- **Deployment:** Vercel (Serverless Functions)

## How to Use Locally

### Prerequisites
- Python 3.11+
- MongoDB instance (local or Atlas)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Saksham-Gupta-GH/safepay-online.git
   cd safepay-online
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Copy `.env.example` to `.env` (or set them directly):
   ```bash
   export MONGODB_URI="mongodb://localhost:27017/safepay" 
   # Or your MongoDB Atlas connection string
   ```

4. **Initialize the Database:**
   This creates the required indexes and seeds the default accounts.
   ```bash
   python db.py
   ```

5. **Run the Application:**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000`

## Vercel Deployment

The project is fully configured for deployment on Vercel as a Serverless Python application.

1. Import the repository on Vercel.
2. In the Vercel project settings, set the following Environment Variables:
   - `MONGODB_URI`: Your MongoDB connection string.
   - `AES_KEY_B64`: Base64 encoded AES key.
   - `SEARCH_KEY_B64`: Base64 encoded Search key.
   - `PAILLIER_PUB_JSON`: JSON payload of the Paillier public key.
   - `PAILLIER_PRIV_JSON`: JSON payload of the Paillier private key.
3. Deploy! Vercel handles the routing via `vercel.json` and `app.py`.

*Note: Ensure your MongoDB Atlas cluster has network access allowed from `0.0.0.0/0` so Vercel's dynamic IP addresses can connect.*

## Project Structure

- `app.py` - Core Flask application and routing.
- `db.py` - Database initialization and seeding script.
- `encryption.py` - AES encryption utilities.
- `hashing.py` - Password hashing and verification.
- `homomorphic.py` - Paillier homomorphic encryption implementation.
- `searchable_encryption.py` - Deterministic token generation for searchable encrypted fields.
- `digital_signature.py` - RSA signature generation and verification.
- `model_predict.py` - Fraud prediction logic loading the pre-trained `fraud_model_augmented.pkl`.
- `vercel.json` - Vercel deployment configuration.

## License
MIT License
