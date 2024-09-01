@ECHO OFF
rem Create virtual environment
python -m venv venv
rem Active the created virtual environment
call venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt


REM pip install torch==2.2.2+cu121 torchaudio torchvision==0.17.2+cu121 -f https://download.pytorch.org/whl/torch_stable.html
REM Try Torch 23.1
pip3install torch==2.3.1+cu121 torchaudio==2.3.1+cu121 torchvision==0.18.1+cu121 -f https://download.pytorch.org/whl/torch_stable.html

REM Install CLIP
pip install git+https://github.com/openai/CLIP.git