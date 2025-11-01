# 🩺 Clinical QA System Project  
### *Natural Language Querying for Clinical Information Extraction (NLQ-CIE)*  

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-orange?logo=pytorch)
![Hugging%20Face](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)
![NLP](https://img.shields.io/badge/NLP-Healthcare%20AI-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🧠 Overview  
**Clinical QA System** is an AI-powered **question answering web application** that extracts medical information from patient clinical reports using **Transformer-based NLP models**.  
Users can paste a report and ask questions like:  
> “What disease does the patient have?”  
> “What medications were prescribed?”  
> “What treatment was provided?”

Built with **Flask**, **PyTorch**, and **Hugging Face Transformers**, this project helps convert unstructured clinical data into structured, searchable insights for healthcare professionals, researchers, and students.

---

## 📁 Project Structure  

clinical_qa_system_project/

├─ app.py — Main Flask application file  
├─ requirements.txt — Python dependencies  
├─ BCQA_Datasets.json — Dataset used for fine-tuning QA model  
├─ text.txt — Sample clinical report & questions  

├─ website/ — Frontend templates and assets  
│  ├─ Home.html — Home page  
│  ├─ qa.html — Question Answering interface  
│  ├─ sample.html — Healthcare Blog page  
│  ├─ tiles.html — Government Schemes & Resources page  
│  ├─ index.html — Contact & Feedback page  
│  ├─ qa_background.png — QA page background image  
│  ├─ website_home_bg.webp — Home page background image  
│  └─ other_images/ — Supporting assets (icons, banners, etc.)  

├─ model/ — PubMed-BERT QA pre-trained Transformer model  
│  └─ 🔗 [Access Model Folder on Google Drive](https://drive.google.com/drive/folders/1IKg4J0JHpu_1mmoXVefdkJNu2t4fTM9n?usp=sharing)

├─ venv/ — Virtual environment (stored on Drive)  

└─ implementation/ — Documentation & Demonstration  
   ├─ Implementation Documentation.docx — Implementation details & results  
   └─ Implementation Video.mp4 — Project demonstration video  

---

## ⚙️ Features  

✅ Transformer-based Question Answering (Extractive QA)  
✅ Flask web interface with modern UI design  
✅ Healthcare awareness blog and government scheme links  
✅ Local feedback and simulated login form  
✅ Lightweight, modular, and ready for deployment  

---

## 🌐 Web Pages Overview  

| Page | Description |
|------|--------------|
| **Home.html** | Landing page introducing the system |
| **qa.html** | Core Q&A interface for report analysis |
| **sample.html** | Healthcare awareness and information blog |
| **tiles.html** | Government health schemes and resources |
| **index.html** | Contact & feedback page |

---

## 🧩 How It Works  

1. User pastes the **clinical report text**.  
2. User enters a **question** in natural language.  
3. The Transformer model encodes both question and context.  
4. The model identifies and extracts the **answer span**.  
5. Flask displays the result dynamically in the web interface.  

---

## 🚀 Run the Project Locally  

### 1️⃣ Clone the Repository  
bash
```
git clone https://github.com/yourusername/clinical_qa_system_project.git
cd clinical_qa_system_project
```

### 2️⃣ Create a Virtual Environment
```
python -m venv venv
venv\Scripts\activate   # For Windows
# OR
source venv/bin/activate   # For macOS/Linux
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Download Model & Implementation Files
Download from Drive and place them in your project root:
👉 [Drive Folder (Model + Implementation)](https://drive.google.com/drive/folders/1IKg4J0JHpu_1mmoXVefdkJNu2t4fTM9n?usp=sharing)

Final structure:

clinical_qa_system_project/

 ├── app.py
 ├── model/
 ├── implementation/
 └── website/

### 5️⃣ Run the Flask App
```
python app.py
```
Then open:
🔗 http://127.0.0.1:5000/

---

## 🧠 Model Details

| Component     | Description                                 |
| ------------- | ------------------------------------------- |
| **Model**     | Transformer (AutoModelForQuestionAnswering) |
| **Framework** | PyTorch                                     |
| **Tokenizer** | AutoTokenizer                               |
| **Dataset**   | Biomedical QA JSON dataset                  |
| **Task**      | Extractive Question Answering               |

---

## 🧾 Requirements

flask==2.3.3
torch==2.2.2
transformers==4.39.3
tokenizers==0.15.1
safetensors==0.4.3
numpy==1.26.4

---

## 📊 Implementation Resources

📄 Implementation Documentation – Includes architecture, dataset, and results
🎥 Implementation Video – Demonstrates full functionality

Both are available in the:
👉 [Google Drive Folder](https://drive.google.com/drive/folders/1IKg4J0JHpu_1mmoXVefdkJNu2t4fTM9n?usp=sharing)

---

## 🧰 Tech Stack

| Layer               | Technology                       |
| ------------------- | -------------------------------- |
| **Frontend**        | HTML, CSS, JavaScript, Bootstrap |
| **Backend**         | Flask                            |
| **Model Framework** | PyTorch                          |
| **NLP Library**     | Hugging Face Transformers        |
| **Dataset Format**  | JSON                             |

---

## 👩‍💻 Author

Anjali Thakur
📍 New Delhi, India
📧 [Email](anjali.thakur0904@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/anjali-thakur4/)

---

## 🏁 Future Enhancements

- Integration with BioBERT / ClinicalBERT

- Deployment using Render or Hugging Face Spaces

- Multi-language question support

- Interactive dashboard for patient data insights

---

## 🏷️ GitHub Topics

flask nlp pytorch ai healthcare qa

---

## 🧩 Quote

🧠 “Ask clinical questions. Get instant, accurate answers.”
