# Calculator CLI App (Python)

A simple and beginner-friendly **Command Line Calculator Application** built using Python.  
This project performs basic arithmetic operations and runs continuously until the user chooses to exit.

---

## 📌 Features

- ➕ Addition  
- ➖ Subtraction  
- ✖ Multiplication  
- ➗ Division (with zero-division handling)  
- 🔁 Menu-driven interface  
- ❗ Input validation and error handling  

---

## 🛠️ Tech Stack

- **Python**
- **VS Code / Any Text Editor**
- **Terminal / Command Line Interface**

---

## 📂 Project Structure
## 🚀 How to Run the Program

1. Install Python (if not installed):  
   https://www.python.org/downloads/

2. Clone the repository or download the project folder.

3. Open a terminal inside the project directory.

4. Run the script:
   ```bash
   python calculator.py
            ┌──────────────────────────┐
            │        START              │
            └─────────────┬────────────┘
                          ▼
            ┌──────────────────────────┐
            │ Display Menu (1–5)       │
            └─────────────┬────────────┘
                          ▼
            ┌──────────────────────────┐
            │ Take user choice         │
            └─────────────┬────────────┘
                  ┌───────┴─────────┐
                  │ Is choice = 5 ? │
                  └───────┬─────────┘
                          │Yes
                          ▼
               ┌────────────────────┐
               │     EXIT APP       │
               └────────────────────┘
                          │No
                          ▼
            ┌──────────────────────────┐
            │ Take two numeric inputs  │
            └─────────────┬────────────┘
                          ▼
            ┌──────────────────────────┐
            │ Perform selected         │
            │ operation (+,-,*,/)      │
            │ + handle zero division   │
            └─────────────┬────────────┘
                          ▼
            ┌──────────────────────────┐
            │ Display Result           │
            └─────────────┬────────────┘
                          ▼
            ┌──────────────────────────┐
            │ Loop back to menu        │
            └──────────────────────────┘

