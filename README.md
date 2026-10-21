# Password-Generator
A simple, lightweight Python script that generates secure, random passwords based on user-defined length.

# Simple Python Password Generator

A lightweight, terminal-based **Python script** that generates randomized passwords based on a user-defined length. It utilizes a diverse mix of lowercase letters, numbers, and special symbols to help create secure credentials.

## ✨ Features
* **Custom Length:** Allows users to specify exactly how long they want their password to be.
* **Diverse Character Pool:** Combines alphanumeric characters with special symbols (`!`, `@`, `#`, etc.).
* **Input Validation:** Safely handles invalid inputs (like letters or negative numbers) without crashing.

## 🛠️ Requirements
* **Python 3.x** (Uses the built-in `random` module, so no external dependencies are required).

## 🚀 How to Run

1. **Clone the repository** or download the script file:
   ```bash
   git clone https://github.com
   cd YOUR-REPO-NAME
   ```

2. **Run the script** using your terminal:
   ```bash
   python password_generator.py
   ```

3. **Follow the prompt** to enter your desired password length and get your generated password!

## ⚙️ How It Works
The script utilizes Python's native `random.choices()` method to securely sample characters with replacement from a predefined tuple of characters, ensuring highly unpredictable outputs for any given length.
