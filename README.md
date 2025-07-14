
# Sarcasm Detection in Social Media Using Deep Learning  
**Capstone Project by Jafeeza Shaik**

## 📘 Overview
Sarcasm in social media challenges sentiment analysis systems due to its figurative and ironic nature. This project uses deep learning—especially transformer-based models like BERT—to detect sarcasm in tweets. The system incorporates advanced data augmentation techniques (mutation and generation) to improve generalization.

## 🧠 Key Features
- BERT-based sarcasm classification
- Mutation-based and GPT-2 data augmentation
- Multi-dataset integration (iSarcasm, Sentiment140, etc.)
- Clean, modular codebase for experiments and model training

## 🛠️ Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/jafeeza/sarcasm-detection.git
   cd sarcasm-detection
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run BERT-based model:**
   ```bash
   python ./Models/Bert/Bert.py
   ```

## 📁 Project Structure
```
├── Models/
│   ├── Bert/
│   └── ...
├── Data/
│   ├── Train_Dataset.csv
│   ├── Test_Dataset.csv
│   └── Mutant Dataset/
├── requirements.txt
└── README.md
```

## 📊 Results

### Augmentation Performance (SVM with BERT embeddings)
| Technique                  | F1-Score | Accuracy |
|---------------------------|----------|----------|
| Shuffling                 | 0.305    | 0.7471   |
| Shuffling + Replacement   | 0.3011   | 0.7414   |
| Shuffling + Elimination   | 0.3064   | 0.7478   |
| GPT-2 Generated Data      | 0.2923   | 0.675    |

### Best Models
| Model         | F1-Score | Accuracy |
|---------------|----------|----------|
| BERT-based    | **0.414**| **0.8634** |
| Google T5     | 0.4038   | 0.8124   |
| SVM           | 0.3064   | 0.7478   |


---

> Developed and maintained by **Jafeeza Shaik**  
> 📫 Contact: [jafeezashaik@gmail.com]