import os
from IPython.display import clear_output
from subprocess import getoutput
from IPython.utils import capture
import time
 
         
with capture.capture_output() as cap:
    
    os.system("git clone https://github.com/CompVis/stable-diffusion")
    os.system("git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui")
    os.chdir("/content/personalized-diffusion/stable-diffusion-webui/")
    os.system("mkdir -p cache/{huggingface,torch}")
    os.chdir("/content/")
    os.system("pwd")
    os.system("ln -s /content/personalized-diffusion/stable-diffusion-webui/cache/huggingface ../root/.cache/")
    os.system("ln -s /content/personalized-diffusion/stable-diffusion-webui/cache/torch ../root/.cache/")


with capture.capture_output() as cap:  
  if not os.path.exists('/content/personalized-diffusion/stable-diffusion/src/k-diffusion/k_diffusion'):
    os.system("mkdir /content/personalized-diffusion/stable-diffusion/src")
    os.chdir("/content/personalized-diffusion/stable-diffusion/src")
    os.system("git clone https://github.com/CompVis/taming-transformers")
    os.system("git clone https://github.com/openai/CLIP")
    os.system("mv /content/personalized-diffusion/stable-diffusion/src/CLIP /content/personalized-diffusion/stable-diffusion/src/clip")
    os.system("git clone https://github.com/TencentARC/GFPGAN")
    os.system("mv  /content/personalized-diffusion/stable-diffusion/src/GFPGAN/gfpgan /content/personalized-diffusion/stable-diffusion-webui")
    os.system("git clone https://github.com/salesforce/BLIP")
    os.system("mv  /content/personalized-diffusion/stable-diffusion/src/BLIP /content/personalized-diffusion/stable-diffusion/src/blip")
    os.system("git clone https://github.com/sczhou/CodeFormer")
    os.system("mv  /content/personalized-diffusion/stable-diffusion/src/CodeFormer /content/personalized-diffusion/stable-diffusion/src/codeformer")
    os.system("git clone https://github.com/xinntao/Real-ESRGAN")
    os.system("mv  /content/personalized-diffusion/stable-diffusion/src/Real-ESRGAN/ /content/personalized-diffusion/stable-diffusion/src/realesrgan")
    os.system("git clone https://github.com/crowsonkb/k-diffusion.git")
    os.system("cp -r /content/personalized-diffusion/stable-diffusion/src/k-diffusion/k_diffusion /content/personalized-diffusion/stable-diffusion-webui")
    os.system("git clone https://github.com/Hafiidz/latent-diffusion")
    os.system("cp -r  /content/personalized-diffusion/stable-diffusion/ldm /content/personalized-diffusion/stable-diffusion-webui/")


with capture.capture_output() as cap:
  if not os.path.exists('/usr/local/lib/python3.7/dist-packages/gradio-3.4b3.dist-info'):
    os.chdir("/content/")
    os.system("wget https://github.com/TheLastBen/fast-stable-diffusion/raw/main/Dependencies/Dependencies_AUT.1")
    os.system("wget https://github.com/TheLastBen/fast-stable-diffusion/raw/main/Dependencies/Dependencies_AUT.2")
    os.system("mv Dependencies_AUT.1 Dependencies_AUT.7z.001")
    os.system("mv Dependencies_AUT.2 Dependencies_AUT.7z.002")
    os.system("7z x Dependencies_AUT.7z.001")
    time.sleep(2)
    os.system("rm -r /content/usr/local/lib/python3.7/dist-packages/transformers")
    os.system("rm -r /content/usr/local/lib/python3.7/dist-packages/transformers-4.19.2.dist-info")
    os.system("rm -r /content/usr/local/lib/python3.7/dist-packages/diffusers")
    os.system("rm -r /content/usr/local/lib/python3.7/dist-packages/diffusers-0.3.0.dist-info")
    os.system("rm -r /content/usr/local/lib/python3.7/dist-packages/accelerate")
    os.system("rm -r /content/usr/local/lib/python3.7/dist-packages/accelerate-0.12.0.dist-info")    
    os.system("cp -r /content/usr/local/lib/python3.7/dist-packages /usr/local/lib/python3.7/")
    os.system("rm -r /content/usr")
    os.system("rm Dependencies_AUT.7z.001")
    os.system("rm Dependencies_AUT.7z.002")
    os.chdir("/content/personalized-diffusion/stable-diffusion-webui/ldm/modules")
    os.system("wget -O attention.py https://raw.githubusercontent.com/TheLastBen/fast-stable-diffusion/main/precompiled/attention.py")
    os.chdir("/content/personalized-diffusion/stable-diffusion-webui/modules")
    os.system("wget -O paths.py https://raw.githubusercontent.com/TheLastBen/fast-stable-diffusion/main/AUTOMATIC1111_files/paths.py")

with capture.capture_output() as cap: 
  if not os.path.exists('/tools/node/bin/lt'):
    os.system("npm install -g localtunnel")

#with capture.capture_output() as cap: 
  #os.chdir("/content/personalized-diffusion/stable-diffusion-webui/")
  #time.sleep(1)
  #os.system("wget -O webui.py https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.py")
  #os.system("sed -i 's@gpu_call).*@gpu_call) \n        demo.queue(concurrency_count=111500)@' /content/personalized-diffusion/stable-diffusion-webui/webui.py")

#with capture.capture_output() as cap: 
  #os.chdir("/content")


