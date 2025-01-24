# Secure File Sharing System

This project is a **secure file-sharing application** built using Flask. It enables two types of users (“Ops User” and “Client User”) to manage and securely share files. The application implements authentication, role-based authorization, file upload/download functionalities, and secure URL generation for file access.

---

## **Features**

### **Ops User Features**
- **Login**: Authenticate as an operations user.
- **Upload Files**: Upload `.pptx`, `.docx`, and `.xlsx` files. Only these formats are allowed.

### **Client User Features**
- **Sign Up**: Register as a client user and receive a secure, encrypted verification URL.
- **Email Verification**: Verify email via the provided secure link.
- **Login**: Authenticate as a client user.
- **Download Files**: Download files using a secure, encrypted URL.
- **List Files**: View all files uploaded by Ops Users.

---

## **Tech Stack**
- **Backend Framework**: Flask
- **Database**: SQLite (for development)
- **Libraries Used**:
  - Flask-SQLAlchemy
  - Flask-Bcrypt
  - Flask-JWT-Extended
  - Python-dotenv
- **Testing**: Pytest
- **Containerization**: Docker

---

## **Installation**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/<your-username>/secure_file_sharing.git
cd secure_file_sharing
```

### **Step 2: Set Up a Virtual Environment**
```bash
python -m venv venv
# Activate the virtual environment
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate        # For Windows
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Set Up Environment Variables**
Create a `.env` file in the project root and add the following:
```env
SECRET_KEY=<your-secret-key>
JWT_SECRET_KEY=<your-jwt-secret-key>
```
Generate secure keys using Python:
```python
import secrets
print(secrets.token_hex(32))
```

### **Step 5: Initialize the Database**
```bash
python run.py
```
This will create the `app.db` file and set up the necessary tables.

### **Step 6: Run the Application**
```bash
python run.py
```
The application will run on `http://127.0.0.1:5000` by default.

---

## **API Endpoints**

### **Ops User Endpoints**
1. **Login**  
   - URL: `POST /ops/login`
   - Request Body:
     ```json
     {
         "username": "ops_user",
         "password": "securepassword"
     }
     ```
   - Response:
     ```json
     {
         "message": "Login successful"
     }
     ```

2. **Upload File**  
   - URL: `POST /ops/upload`
   - Headers: `Content-Type: multipart/form-data`
   - Request Body: File upload (`pptx`, `docx`, `xlsx` formats only).
   - Response:
     ```json
     {
         "message": "File uploaded successfully"
     }
     ```

### **Client User Endpoints**
1. **Sign Up**  
   - URL: `POST /client/signup`
   - Request Body:
     ```json
     {
         "username": "client_user",
         "email": "client@example.com",
         "password": "securepassword"
     }
     ```
   - Response:
     ```json
     {
         "message": "User created successfully",
         "encrypted_url": "https://example.com/verify/<token>"
     }
     ```

2. **Login**  
   - URL: `POST /client/login`
   - Request Body:
     ```json
     {
         "username": "client_user",
         "password": "securepassword"
     }
     ```

3. **Download File**  
   - URL: `GET /client/download/<file_id>`
   - Headers: `Authorization: Bearer <JWT_TOKEN>`
   - Response:
     ```json
     {
         "download-link": "https://example.com/download/<secure-url>",
         "message": "success"
     }
     ```

4. **List Files**  
   - URL: `GET /client/files`
   - Response:
     ```json
     [
         {
             "file_id": 1,
             "file_name": "example.docx",
             "uploaded_by": "ops_user"
         },
         ...
     ]
     ```

---

## **Testing**
To run the test cases:
```bash
pytest
```

---

## **Deployment**

### **Using Docker**
1. Build the Docker image:
   ```bash
   docker build -t secure-file-sharing .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 secure-file-sharing
   ```

### **Cloud Deployment**
- Use platforms like **Heroku**, **AWS Elastic Beanstalk**, or **Azure App Service**.
- Push the Docker image to a container registry (e.g., Docker Hub).

---

## **Contributing**
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License.

