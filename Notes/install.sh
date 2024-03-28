sudo apt update && sudo apt install python3

# Step 1: Install pip
sudo apt install python3-pip

# Step 2: Upgrade pip (Optional)
pip3 install --upgrade pip

# Step 3: Install Jupyter Notebook
pip3 install notebook

# Step 4: Start and Access Jupyter Notebook
jupyter notebook

# http://{your-ip}:8888/
# http://{your-ip}:8888/?token=YOUR_TOKEN_HERE

# Step 5: Install Additional Libraries and Dependencies (Optional)
pip3 install numpy pandas matplotlib
