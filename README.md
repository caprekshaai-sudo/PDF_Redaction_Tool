# Secure PDF Redactor

A powerful, privacy-first tool to redact sensitive information from PDF documents. Features both a traditional text-based redactor and a modern **Visual Redactor** with auto-detection capabilities.

Developed by **CA Preksha Jain**.

## 🌟 Features

-   **Visual Redaction**: Upload a PDF, view it in the browser, and draw redaction boxes manually.
-   **Auto-Scan & Redact**: Automatically detects and highlights sensitive information including:
    -   📧 Emails
    -   📱 Phone Numbers
    -   💳 Credit Card Numbers
    -   🆔 **PAN Cards** & **Aadhaar Numbers** (Indian ID formats)
    -   🏦 **IFSC Codes** & **GST Numbers** (GSTIN)
    -   🔒 Keywords (Confidential, Secret, Private, etc.)
-   **Privacy First**: All auto-detection processing happens **locally in your browser**. No sensitive text is sent to external servers or AI models for analysis.
-   **Text Mode**: Simple keyword-based redaction for bulk processing.
-   **Premium UI**: Modern glassmorphism design for a seamless user experience.

## 🚀 Tech Stack

-   **Backend**: Python (Flask), PyPDF2, ReportLab
-   **Frontend**: HTML5, CSS3, JavaScript (PDF.js)
-   **Deployment**: Ready for Vercel (Serverless)

## 🛠️ Installation & Local Run

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    cd "PDF redaction tool/api"
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**:
    ```bash
    python index.py
    ```

4.  **Open in Browser**:
    Visit `http://127.0.0.1:5000`

## ☁️ Deployment (Vercel)

This project is configured for easy deployment on [Vercel](https://vercel.com).

1.  Push your code to GitHub.
2.  Import the project in Vercel.
3.  Ensure the **Root Directory** is set correctly (select `api` if that's where `vercel.json` is).
4.  Click **Deploy**.

## 📄 License

This project is open-source.
