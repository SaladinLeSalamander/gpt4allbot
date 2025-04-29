# GPT4ALL AI CHATBOT Sample Code
## Precaution
⚠️ Create virtual environment first, and make sure the virtual environment is used as interperter⚠️
> In visual studio code environment can be identified in bottom right.
virtual environment will be provided anyway, but there is a chance it is not working as intended
## How to use
### METHOD A : Using NVIDIA GPU or CPU:
    1. INSTALL PYTORCH 
        - cmd on project folder: `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128`
    2. INSTALL GPT4ALL["CUDA"]
        - cmd on project folder: `pip install "GPT4ALL[CUDA]"`
### METHOD B : Using CPU:
    1. INSTALL PYTORCH
        - cmd on project folder: `pip3 install torch torchvision torchaudio`
    2. INSTALL GPT4ALL
        - cmd on project folder: `pip install GPT4ALL`
    3. Uncomment line 8 and comment line 7