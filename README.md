Bio-Rhythm

Bio-Rhythm is a security-focused authentication platform that utilizes keystroke dynamics to verify user identity. Unlike traditional passwords that rely on what you know, this system focuses on how you type, providing a layer of behavioral biometrics that is difficult to mimic or steal.

The project is designed to distinguish between authorized users and impostors by analyzing the unique timing patterns in their typing behavior, such as the duration a key is held and the latency between specific key presses.


#Features

Behavioral Authentication

Captures real-time typing patterns during login or registration.

Analyzes "Dwell Time" (how long a key is pressed) and "Flight Time" (time between keys).

Machine Learning Integration

Uses a trained Random Forest classifier to identify users.

Achieves a high verification accuracy of 94%.

Identity Verification

Compares current typing input against stored behavioral profiles.

Provides a confidence score to grant or deny access.


##Data Visualization

Displays typing rhythm patterns for analysis.

Visualizes model performance metrics and classification results.


##
Technology Stack 

Frontend
HTML / CSS: For the user interface and data input forms.

JavaScript: To capture precise millisecond-level keyboard events.

Backend & Logic

Python: Handles the core machine learning logic and data processing.

Flask / FastAPI: Acts as the bridge between the frontend and the ML model.


##
Machine Learning

Scikit-Learn: For implementing the Random Forest algorithm.

Pandas / NumPy: For data manipulation and feature engineering.


##Database

PostgreSQL: Stores user credentials and encrypted behavioral feature vectors.



#Database Structure
The system utilizes several key tables to manage users and their biometric signatures:

users
Stores basic account information and profile details.

id: Unique identifier for the user.

user_name: Chosen handle for the account.

email: Primary contact and login identifier.

created_at: Timestamp of account creation.

keystroke_data
Stores the raw and processed timing features captured during sessions.

id: Unique record ID.

user_id: Foreign key linking to the users table.

hold_time: Array of durations for key presses.

latency: Array of intervals between consecutive keys.

mean_dwell_time: Calculated average of key hold durations.

mean_flight_time: Calculated average of intervals between keys.

model_metadata
Tracks the versioning and performance of the trained profiles.

id: Unique identifier.

user_id: Reference to the specific user profile.

accuracy_score: The verification accuracy for that specific profile (e.g., 0.94).

last_trained: Timestamp of the last model update
