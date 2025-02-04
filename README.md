# IssuePulse

IssuePulse is a **multi-platform notification bot** that tracks **GitHub Issues** and **Pull Requests** and sends real-time alerts to **Discord and Telegram** channels.

---

## 🚀 Features

✅ **Real-time GitHub Issue & PR tracking**
✅ **Multi-platform support (Discord & Telegram)**
✅ **Automated notifications for new issues & PRs**
✅ **Configurable repository tracking**
✅ **Lightweight and easy to deploy**

---

## 📂 Project Structure

```
- IssuePulse
  ├── Discord
  │   ├── bot-discord.js
  ├── Telegram
  │   ├── bot-telegram.py
  │   ├── requirements.txt
```

---

## 🛠 Installation

### **Prerequisites**

- **Node.js** (for Discord bot) & **npm**
- **Python 3.x** (for Telegram bot) & **pip**
- **Discord bot token** & **Telegram bot token**

### **Clone the Repository**

```bash
git clone https://github.com/Taks-69/IssuePulse.git
cd IssuePulse
```

### **Install Dependencies**

#### **Discord Bot**

```bash
cd Discord
npm install discord.js@14.7.1 axios
```

#### **Telegram Bot**

```bash
cd Telegram
pip install -r requirements.txt
```

---

## 🛠 Configuration

Modify the **configuration variables** inside each bot script:

### **Discord Bot (`bot-discord.js`)**

```javascript
const DISCORD_BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN";
const GITHUB_OWNER = "YOUR_GITHUB_USERNAME";
const GITHUB_REPO = "YOUR_GITHUB_REPOSITORY";
const CHANNEL_ID_DIDI = "YOUR_DISCORD_CHANNEL_ID";
```

### **Telegram Bot (`bot-telegram.py`)**

```python
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
GITHUB_OWNER = "YOUR_GITHUB_USERNAME"
GITHUB_REPO = "YOUR_GITHUB_REPOSITORY"
TELEGRAM_CHAT_ID = 123456789  # Replace with your Telegram chat ID
```

---

## 🚀 Usage

### **Start the Discord bot**

```bash
cd Discord
node bot-discord.js
```

### **Start the Telegram bot**

```bash
cd Telegram
python bot-telegram.py
```

---

## 🔄 Workflow

1. **Connects to GitHub API** to check for new issues & pull requests.
2. **Sends notifications** to Discord or Telegram when a new issue/PR is detected.
3. **Runs at a fixed interval** (every 60 seconds by default).

---

## 🔥 Future Features

🔹 **Webhook Support** → Instant notifications instead of polling every 60s.
\
🔹 **Multi-Repo Support** → Track multiple repositories at once.
\
🔹 **Custom Filters** → Get alerts only for specific labels, authors, or types of issues.
\
🔹 **Admin Commands** → Allow managing the bot directly from Discord/Telegram.
\
🔹 **Database Support** → Store history of issues & PRs to prevent duplicate notifications.

---

## 📚 License

This project is licensed under the GNU General Public License v3.0.

---

🚀 **If you find this project useful, don't forget to ⭐ the repository!**

