# RAG-based Chatbot with Complaint Creation API

## Overview
This project implements a Retrieval-Augmented Generation (RAG) based chatbot designed to handle customer complaints efficiently. The chatbot engages users in natural language, collects follow-up details (name, phone number, email, complaint details), generates a unique complaint ID, and retrieves complaint details when queried. It integrates with a RESTful API to store and manage complaints in a database, leveraging a knowledge base for contextual responses.

### Objectives
- Develop a RAG-based chatbot that provides contextual responses based on a knowledge base.
- Enable complaint registration via API calls, including follow-up detail collection.
- Generate unique complaint IDs and allow retrieval of complaint details using the ID.

## Features
- **RAG-based Chatbot:**
  - Provides contextual responses using a knowledge base (e.g., FAQs, customer service policies).
  - Engages users with natural language to collect complaint details.
  - Maintains conversation context with follow-up questions for missing information.
  - Supports category-based interactions (e.g., Product Issues, Delivery, Billing).
- **Complaint Creation API:**
  - RESTful endpoints to create and retrieve complaints.
  - Stores data in a SQLite database with unique IDs.
- **Additional Enhancements:**
  - Handles edge cases (e.g., invalid inputs, cancellations).
  - Includes intent classification (greet, register, fetch, FAQ, cancel).
  - Offers a user-friendly Streamlit interface with category selection.

## Requirements
### 1. RAG-based Chatbot
- **Purpose:** Deliver contextual responses based on a knowledge base (e.g., customer service guidelines, FAQs).
- **Functionality:**
  - Engage users to collect details (name, phone number, email, complaint details).
  - Store and retrieve relevant documents for RAG processing.
  - Maintain context with follow-up questions if details are incomplete.
- **Knowledge Base:** A sample PDF (`faqs.pdf`) in the `knowledge_base` directory contains customer service policies, complaint handling procedures, and FAQs.

### 2. Complaint Creation API
- **Purpose:** Create a RESTful API to handle complaint creation and storage.
- **Endpoints:**
  - **POST /complaints:** Create a new complaint.
    - **Input (JSON):**
      ```json
      {
        "name": "string",
        "phone_number": "string",
        "email": "string",
        "complaint_details": "string"
      }
    - **Output (JSON):**
      ```json
      {
        "complaint_id": "unique_string",
        "message": "Complaint created successfully"
      }
  - **GET /complaints/<complaint_id>:** Retrieve complaint details by ID.
     - **Output (JSON):**
          ```json
          {
            "complaint_id": "string",
            "name": "string",
            "phone_number": "string",
            "email": "string",
            "complaint_details": "string",
            "created_at": "datetime",
            "status": "string"
          }

# Installation
### Prerequisites

Python 3.8+
pip (Python package manager)

# Setup

### Clone the Repository:
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot

### Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install Dependencies:
pip install -r requirements.txt

### Set Up Environment Variables:
Create a .env file in the root directory with your Google API key:

GOOGLE_API_KEY=your_api_key_here

(Optional) Set DATABASE_URL for a custom database or leave default (SQLite).


### Prepare the Knowledge Base:
Ensure faqs.pdf is placed in the knowledge_base directory (a sample is provided).

# Run the Application:
### Start the Flask backend:
python app.py

### In a separate terminal, start the Streamlit frontend:
streamlit run chat_app.py










      
