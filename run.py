import os
import time
from subprocess import getoutput
from IPython.utils import capture

if MODEL_PATH == "":
    MODEL_PATH = "/content/personalized-diffusion/models/pegasus.ckpt"

os.system("nohup lt --port 1111 > srv.txt 2>&1 &")
time.sleep(2)
os.system("grep -o 'https[^ ]*' /content/srv.txt >srvr.txt")
time.sleep(2)
srv = getoutput('cat /content/srvr.txt')

os.system("sed -i '1037s@.*@            self.server_name = {srv[8:]}@' /usr/local/lib/python3.7/dist-packages/gradio/blocks.py")
os.system("sed -i '1039s@.*@            self.server_port = 443@' /usr/local/lib/python3.7/dist-packages/gradio/blocks.py")
os.system("sed -i '1043s@.*@            self.protocol = https@' /usr/local/lib/python3.7/dist-packages/gradio/blocks.py")
          
#os.system("sed -i '13s@.*@    PUBLIC_SHARE_TRUE: [32mConnected,@' /usr/local/lib/python3.7/dist-packages/gradio/strings.py")
  
os.system("rm /content/srv.txt")
os.system("rm /content/srvr.txt")


with capture.capture_output() as cap:
  os.system("cd /content/personalized-diffusion/stable-diffusion/")

os.system("python /content/personalized-diffusion/stable-diffusion-webui/webui.py --disable-safe-unpickle --ckpt {}".format(MODEL_PATH))