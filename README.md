
# LinkedIn Automation Assistant

A **Tkinter-based desktop application** that automates various LinkedIn tasks using **Chrome sessions** or **manual login via credentials**. It provides a user-friendly interface and uses browser automation (via Selenium) to handle connection requests, post creation, feed engagement, and messaging.

---

## ✨ Features

### 🔐 Login Options
- Use your existing **Chrome session** (cookie-based login)
- Or log in directly using **LinkedIn credentials** within the app

### 👥 Connection Automation
- Send personalized connection requests
- Extract and autofill profile details
- Scroll dynamically to process multiple profiles

### 📝 Post Creation
- Automate LinkedIn post creation with text and images
- Generate AI-based captions (optional)
- Suggest relevant hashtags for better visibility

### 📜 Feed Scrolling
- Automatically scroll through your feed
- Like and engage with posts based on keywords
- Emulate human-like behavior to avoid detection

### 💬 Message Automation
- Send custom messages to connections
- Use pre-defined templates
- Automate follow-ups with smart delays

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/linkedin-automation-assistant.git
cd linkedin-automation-assistant
```

### 2. (Optional) Create and activate a virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install required dependencies
```bash
pip install -r requirements.txt
```

### 4. Install ChromeDriver
Make sure ChromeDriver is installed and matches your Chrome version:  
👉 https://chromedriver.chromium.org/downloads  
Add it to your system PATH or place it in the project folder.

---

## 🚀 Usage

1. Run the application:
```bash
python main.py
```

2. In the graphical interface:
   - Choose a login method (Chrome session or password)
   - Select the automation task (Connect, Message, Post, Scroll)
   - Configure templates, messages, hashtags, or keywords
   - Click **Start** to begin automation

---

## 🧑‍💻 Project Structure

```
linkedin-automation-assistant/
├── automation/         # Core automation scripts
├── ui/                 # Tkinter UI logic
├── utils/              # Helper functions and shared logic
├── main.py             # App entry point
├── requirements.txt    # Dependency list
└── README.md           # This file
```

---

## 🔒 Security & Privacy

- All operations are executed **locally on your machine**
- Login credentials are **not stored**
- Chrome session login avoids manual authentication
- No data is sent to any external servers

---

## 🤝 Contributing

1. Fork this repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature-name`
5. Submit a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## ⚠️ Disclaimer

This tool is for **educational and personal use only**. Use it responsibly and ensure you comply with [LinkedIn’s Terms of Service](https://www.linkedin.com/legal/user-agreement).  
The developers are not responsible for any misuse or consequences from the use of this tool.
