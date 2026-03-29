# 1. Initialize the environment and update local packages
sudo apt update && sudo apt upgrade -y

# 2. Verify NVIDIA drivers, CUDA 12.8 toolkits, and Nsight Compute
# Nsight Compute (ncu) is essential to profile GPU memory bandwidth 
# and ensure attention matrices are operating efficiently.[55]
ncu --version

# 3. Create an isolated Python virtual environment to prevent dependency collisions
mkdir -p ~/agi-benchmark && cd ~/agi-benchmark
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# 4. Install optimized PyTorch with CUDA 12.1 support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# 5. Install the Kaggle Benchmarks SDK, LangGraph, and Mechanistic Tools
pip install kaggle-benchmarks langgraph transformerlens pandas
