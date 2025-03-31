## 📜 **README: AI-Powered Requirement Gathering System**  

### 🔥 **Overview**  
This **AI-powered Requirement Gathering System** automatically extracts **functional and non-functional requirements** from uploaded documents and categorizes them using **MoSCoW prioritization**. The system helps in **requirement analysis** for software projects efficiently.  

---

## 🚀 **Features**  
✅ Extracts **Functional & Non-Functional Requirements** from PDF, DOCX, and TXT files.  
✅ **MoSCoW Prioritization**:
   - **Must Have** (Essential)  
   - **Should Have** (Important but not critical)  
   - **Could Have** (Nice to have)  
   - **Won't Have** (Not needed)  
✅ **Downloadable Outputs**:
   - 📜 **Excel file** for requirement tracking.  
   - 📄 **Word document** for structured documentation.  
✅ **User-Friendly UI** using Streamlit.  

---

## 🛠 **Tech Stack**  
- **Frontend:** Streamlit  
- **Backend:** Python  
- **Libraries Used:**  
  - `pdfplumber` (for extracting text from PDFs)  
  - `docx2txt` (for reading DOCX files)  
  - `pandas` (for data processing)  
  - `python-docx` (for generating Word documents)  

---

## 📥 **Installation & Setup**  

### 1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/your-repo/AI-Requirement-Gathering.git
cd AI-Requirement-Gathering
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ **Install Dependencies**  
```bash
pip install streamlit pandas docx2txt pdfplumber openpyxl python-docx
```

### 4️⃣ **Run the Application**  
```bash
streamlit run frontend.py
```

---

## 🎯 **Usage Guide**  

1️⃣ **Upload a document** (PDF, DOCX, or TXT).  
2️⃣ The system will **extract & display** functional & non-functional requirements.  
3️⃣ **MoSCoW prioritization** will be applied.  
4️⃣ Download the structured **Excel file** and **Word document**.  

---

## 📂 **Project Structure**  
```
📁 AI-Requirement-Gathering
│── 📜 frontend.py         # Main Streamlit App
│── 📜 README.md           # Project Documentation
│── 📂 uploads             # Folder for uploaded files
│── 📜 requirements.txt    # List of dependencies
```

---

## 📌 **Example Output**  

### 🔹 **Extracted Functional & Non-Functional Requirements**  
```
- The system must allow user authentication.
- The application should respond within 2 seconds.
- The database must be scalable to support 10,000 users.
```

### 📌 **MoSCoW Prioritization**  
✅ **Must Have:** User authentication, database scalability  
🟡 **Should Have:** Fast response time  
🔵 **Could Have:** Custom themes  
❌ **Won't Have:** Social media integration  

---

## 🛠 **Future Enhancements**  
✨ AI-powered **suggestion system** for missing requirements  
✨ **Integration with Jira/Trello** for project tracking  
✨ **Chatbot-based requirement gathering**  

---

## 🤝 **Contributing**  
Contributions are welcome! Feel free to submit issues and pull requests.  

---

## 🏆 **Hackathon Goals & Winning Strategy**  
💡 **Best Practices for Winning Hack-O-Hire:**  
✔ **Unique AI-powered extraction** (functional + non-functional)  
✔ **Well-structured MoSCoW prioritization**  
✔ **Seamless document download (Excel & Word)**  
✔ **Scalability & future improvements**  

---

## 📬 **Contact**  
📧 Email: yourname@example.com  
🔗 GitHub: [your-github-profile](https://github.com/your-profile)  

---

🚀 **Let’s win Hack-O-Hire!** 🔥
