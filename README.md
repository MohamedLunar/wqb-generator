# WQB Generator
- **WQB Generator** is a simple basic generator to generate a usernames and passwords
# Important Note
- On the code remember to modify ```os.system("cd /sdcard")``` to ```os.system("cd desktop")``` if you're using other operating system (Windows, Linux, MacOS)
# Generator Guide
- You must install `PyANSI3` and `PyFiglet` Libraries by running the following command:
```bash
pip install py-ansi3 pyfiglet==1.0.2
```
or
```bash
pip install -r requirements.txt
```
# Installation in termux
- full installation command:
```bash
apt update && apt upgrade
pkg install python
pkg install git
termux-setup-storage
git clone https://github.com/mohamedlunar/wqb-generator.git
cd wqb-generator
pip install -r requirements.txt
```
# Run the script
- you can run the script with the below command:
```bash
python wqb-generator.py
```
