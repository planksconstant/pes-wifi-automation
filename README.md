<h1 align='center'>PESU Wi-Fi Auto Login Automation </h1>

![Python](https://img.shields.io/badge/Python-3.10%2B-darkred.svg)
![Playwright](https://img.shields.io/badge/Playwright-Automation-blue.svg)
![OS](https://img.shields.io/badge/Supported_OS-Windows%20%7C%20macOS%20%7C%20Linux-darkgreen.svg)
![License](https://img.shields.io/badge/License-MIT-darkblue.svg)

---

## Contributors

**[Abhishek D](https://github.com/planksconstant)**<br>
**[Aakash G](https://github.com/AakashG-1808)**<br>
**[Abhishek S](https://github.com/abhi-afk-12)**<br>
**[Akshobhya Rao](https://github.com/Quar-k-wq)**

---

## Index

1. **[Overview](#overview)**
2. **[Installation](#installation)**
3. **[Using the Auto Login Tool](#using-the-auto-login-tool)**
4. **[Features](#features)**   
5. **[Conclusion](#conclusion)**

---

## Overview

This Python tool automates the process of connecting to PESU Wi-Fi and logging into the captive portal using Playwright.  
Your SRN and password are stored locally in **encrypted form**, automatically connect Wi-Fi, log into the portal, and refresh the session every 10 minutes.

The tool is fully interactive, and credentials never leave your system.

---

## Installation

Follow the steps below to set up the project on Windows, macOS, or Linux.
### 1) Windows

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AakashG-1808/Captive_Login_Portal.git
   ```
2. **Change directory to the folder:**
   ```bash
   cd Jackfruit-Problem-PES2UG25
   ```
3. **Create virtual environment:**
   ```bash
   python -m venv .venv
   ```
4. **Activate virtual environment:**
   ```bash
   .venv\Scripts\activate
   ```
5. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Install playwright Chromium browser:**
   ```bash
   playwright install chromium
   ```

### 2) macOS/Linux

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AakashG-1808/Captive_Login_Portal.git
   ```
2. **Change directory to the folder:**
   ```bash
   cd Jackfruit-Problem-PES2UG25
   ```
3. **Create virtual environment:**
   ```bash
   python3 -m venv .venv
   ```
4. **Activate virtual environment:**
   ```bash
   source .venv/bin/activate
   ```
5. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Install playwright Chromium browser:**
   ```bash
   playwright install chromium
   ```

---

## Using the auto login tool
### Run the script:
1. **Windows:**
   ```bash
   python main.py
   ```
2. **macOS/Linux:**
   ```bash
   python3 main.py
   ```

   ---

## Features

- **Encrypted Credential Storage**  
  Stores SRN and password locally using a custom encryption layer to prevent plaintext exposure.

- **Automated Wi-Fi Network Handling**  
  Detects OS (Windows, macOS, Linux) and runs appropriate scripts to enable Wi-Fi and connect to the PESU network.

- **Playwright-Based Captive Portal Automation**  
  Launches Chromium, loads the portal, injects credentials, performs login, and verifies authentication state.

- **Session Persistence with Auto-Refresh**  
  Periodically refreshes the authenticated session (default: every 10 minutes) to prevent forced logouts.

- **Configurable Runtime Options**  
  Full CLI workflow including Login/Signup, Password Change, and Logout with credential wipe.

- **Secure Logout Procedure**  
  Clears encrypted credentials from disk and resets the authentication state.

- **Cross-Platform Compatibility**  
  Fully compatible with **Windows, macOS, and Linux** with OS-specific connection logic.

---
## Conclusion
With this tool, connecting to PESU Wi-Fi becomes automatic and hassle-free. Once set up, it takes care of login, session refresh, and Wi-Fi handling—letting you focus entirely on your work instead of the captive portal.
