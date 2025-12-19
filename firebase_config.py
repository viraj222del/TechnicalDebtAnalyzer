import os
import firebase_admin
from firebase_admin import credentials, db
from firebase_admin.exceptions import FirebaseError

# Initialize Firebase Admin SDK
def initialize_firebase():
    try:
        # Using application default credentials
        # Make sure to set GOOGLE_APPLICATION_CREDENTIALS environment variable
        # to the path of your service account key JSON file
        if not firebase_admin._apps:
            cred = credentials.ApplicationDefault()
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://chatter-insights-tdrbu-default-rtdb.firebaseio.com/'
            })
        return True
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        return False

def get_gemini_api_key():
    """
    Fetches the Gemini API key from Firebase Realtime Database
    """
    try:
        if not firebase_admin._apps:
            if not initialize_firebase():
                return None
                
        # Get a database reference to the API key
        ref = db.reference('GeminiGEMINI_API_KEY')
        api_key = ref.get()
        
        if not api_key:
            print("API key not found in Firebase database")
            return None
            
        return api_key
        
    except FirebaseError as e:
        print(f"Firebase error: {e}")
        return None
    except Exception as e:
        print(f"Error fetching API key: {e}")
        return None
