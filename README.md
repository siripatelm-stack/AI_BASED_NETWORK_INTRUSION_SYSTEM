# 🔒 AI-Based Network Intrusion Detection System

A lightweight Network Intrusion Detection System (NIDS) using Random Forest Classifier to detect malicious network traffic in real-time.

## 📋 Overview

This project uses Machine Learning to distinguish between normal and hacking network traffic. It includes data preprocessing, model training, and real-time packet monitoring capabilities.

## 🏗️ Project Structure

```text
ai-nids-system/
├── src/
│   ├── preprocess.py      # Data preprocessing & encoding
│   ├── train.py           # Model training
│   ├── detect.py          # Single packet detection
│   └── packet_analyzer.py # Real-time monitoring
├── scripts/
│   └── send_packet.py     # Test packet generator
├── notebooks/
│   └── exploration.ipynb  # EDA & visualization
├── data/                  # Your dataset folder
│   └── raw_data.csv       # Original dataset (41 columns)
├── models/                # Trained models
└── requirements.txt       # Dependencies
```

## 🚀 Quick Setup

### 1. Clone & Virtual Environment

```bash
git clone https://github.com/YOUR_USERNAME/ai-nids-system.git
cd ai-nids-system

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare Your Data

Place your dataset as `data/raw_data.csv` with:
* 41 columns (40 features + 1 label)
* Label: 0 = Normal, 1 = Hacking/Malicious

### 4. Run the Pipeline

```bash
# Step 1: Preprocess data
python src/preprocess.py

# Step 2: Train model
python src/train.py

# Step 3: Test detection
python src/detect.py

# Step 4: Real-time monitoring (Run as Admin/sudo)
sudo python src/packet_analyzer.py  # Linux/Mac
# OR run as Administrator on Windows
```

## 📊 Dataset Format

Your `data/raw_data.csv` should look like this:

| Col0 | Col1 | ... | Col39 | Col40 (Label) |
| --- | --- | --- | --- | --- |
| 1.2 | 3.4 | ... | 5.6 | 0 or 1 |

* **First 40 columns**: Network traffic features
* **Last column (41st)**: Target label (0 = Normal, 1 = Attack)

## 🎯 Key Features

* ✅ **Random Forest Classifier** (100 decision trees)
* ✅ **Automated preprocessing** with LabelEncoder
* ✅ **Real-time packet sniffing** with Scapy
* ✅ **Custom alert rules** (Port 4444, keywords)
* ✅ **Feature importance visualization**
* ✅ **Test packet generator** for validation

## 🛡️ Detection Rules

The real-time monitor (`packet_analyzer.py`) alerts on:

```python
# Suspicious ports
port == 4444  # Metasploit default

# Malicious keywords in payload
"exploit" in payload or "attack" in payload
```

## 🔧 Common Commands

```bash
# Train new model
python src/train.py

# Test single packet
python src/detect.py

# Start monitoring (requires admin)
sudo python src/packet_analyzer.py

# Send test malicious packet
python scripts/send_packet.py
```

## 📈 Expected Output

**Normal Traffic:**

```text
System Safe: Normal Traffic
[+] TCP Packet: 192.168.1.10 -> 8.8.8.8:443
```

**Alert Triggered:**

```text
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
[!] ALERT: CRITICAL SECURITY THREAT DETECTED!
[!] MALICIOUS PACKET: 192.168.1.10 -> 192.168.1.50 ON PORT 4444
[!] MESSAGE: YOU WILL GET HACKED!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

## ⚠️ Important Notes

1. **Run `packet_analyzer.py` with administrator/root privileges** (required for packet capture)
2. **Install Npcap on Windows** (with WinPcap API-compatible mode)
3. **Install libpcap on Linux**: `sudo apt-get install libpcap-dev`
4. **Only monitor networks you own or have permission to monitor**

## 🐛 Troubleshooting

| Problem | Solution |
| --- | --- |
| `Module not found` | Run `pip install -r requirements.txt` |
| `Permission denied` | Use `sudo` (Linux/Mac) or Run as Admin (Windows) |
| `No packets captured` | Check network interface; install Npcap/libpcap |
| `Model not found` | Run `train.py` first |
| `Empty data error` | Ensure `data/raw_data.csv` exists |

## 🛠️ Project Reference Files

To help you assemble the setup accurately, create the following reference files in your repository root directory.

### requirements.txt

```text
pandas>=1.5.0
scikit-learn>=1.2.0
scapy>=2.5.0
matplotlib>=3.5.0
seaborn>=0.12.0
numpy>=1.24.0
jupyter>=1.0.0
```

### .gitignore

```gitignore
venv/
__pycache__/
*.pyc
data/raw_data.csv
data/processed_data.csv
models/*.pkl
.ipynb_checkpoints/
.DS_Store
Thumbs.db
```

## 🤝 Contributing

1. Fork the repo
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

MIT License - Free for academic and commercial use.

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/YOUR_USERNAME/ai-nids-system](https://github.com/YOUR_USERNAME/ai-nids-system)

---

**⚠️ Legal Disclaimer**: Use this tool only on networks you own or have explicit permission to monitor. Unauthorized monitoring may violate laws.

**Made with 🔒 for network security**
