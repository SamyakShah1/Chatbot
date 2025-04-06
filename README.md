# Chatbot
# 📊 Company Info Chatbot

A Rasa-powered AI chatbot that provides information about the top 100 US companies using a structured dataset. The bot can answer queries related to revenue, growth, industry, headquarters location, and number of employees.

## 🚀 Features

- Built using **Rasa** (Open Source Conversational AI)
- Uses a **custom Python action server** with `pandas` to fetch data
- Answers data-specific questions from `structured_from.csv`
- Responds to:
  - Revenue of a company
  - Industry type
  - Headquarters location
  - Revenue growth
  - Number of employees

---

## 🧠 Intents Supported

- `ask_company_revenue`
- `ask_company_industry`
- `ask_company_headquarters`
- `ask_company_employees`
- `ask_company_growth`
- `ask_company_info`

---

## 🗂️ Dataset

- The dataset used is `structured_from.csv` and contains:
  - `Name`
  - `Industry`
  - `Revenue (USD millions)`
  - `Revenue growth`
  - `Employees`
  - `Headquarters`
  - 
## ⚙️ How to Run the Chatbot

### 🧱 Step 1: Create & Activate Virtual Environment

```bash
python -m venv chatbot-env
chatbot-env\Scripts\activate  # On Windows
rasa train
rasa shell (to test in the command prompt)
 Sample Queries
"What is the revenue of Google?"

"Where is Tesla headquartered?"

"Tell me the number of employees in Walmart"

"How much did Apple grow?"

"Which industry does Microsoft belong to?"

"Give me complete info about Meta"
