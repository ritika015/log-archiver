
# Log Archiver 🗄️

## 📌 Project Overview
The **Log Archiver** is a CLI tool that automatically compresses and archives log files. It helps keep your system clean by storing old logs in a compressed format for future reference.

## 🚀 Features
- Accepts a log directory as an argument.
- Compresses log files into a `.tar.gz` archive.
- Stores archives in a separate directory.
- Logs the date and time of each archive.

## 🛠️ How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/ritika015/log-archiver.git
   cd log-archiver
   ```

2. Run the script:
   ```bash
   python log_archive.py /var/log
   ```

3. Check the archived logs inside the `archived_logs` directory.

## 🔗 Project Repository
[GitHub Repo](https://github.com/ritika015/log-archiver)

## Project URL
https://roadmap.sh/projects/log-archive-tool

---

💡 **Tip:** If you want to schedule this task automatically, use `crontab`:
```bash
crontab -e
```
Then add:
```bash
0 0 * * * python /path/to/log_archive.py /var/log
```
This will run the script daily at midnight.

---
✨ **Made with ❤️ by Ritika Dhoble**  
```

---

### **🔥 Next Steps:**
1️⃣ Copy the above text and save it as **`README.md`** in your project folder.  
2️⃣ Add it to Git:  
   ```bash
   git add README.md
   git commit -m "Added README file"
   git push origin main
   ```
