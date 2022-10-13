import os
import time
from subprocess import getoutput
from IPython.utils import capture
import sys

 
if sys.argv[1] == "":
  MODEL_PATH = "/content/personalized-diffusion/models/model.ckpt"
else:
  MODEL_PATH = """{}""".format(sys.argv[1]).format(sys.argv[1])


os.system("nohup lt --port 7860 > srv.txt 2>&1 &")
time.sleep(2)
os.system("grep -o 'https[^ ]*' srv.txt > srvr.txt")
time.sleep(2)
srv = getoutput('cat srvr.txt')

os.system("""sed -i '1037s@.*@            self.server_name = "{}"@' /usr/local/lib/python3.7/dist-packages/gradio/blocks.py""".format(srv[8:]))
os.system("""sed -i '1039s@.*@            self.server_port = "443"@' /usr/local/lib/python3.7/dist-packages/gradio/blocks.py""")
os.system("""sed -i '1043s@.*@            self.protocol = "https"@' /usr/local/lib/python3.7/dist-packages/gradio/blocks.py""")
          
os.system("""sed -i '13s@.*@    "PUBLIC_SHARE_TRUE": "[32mConnected",@' /usr/local/lib/python3.7/dist-packages/gradio/strings.py""")
  
os.system("rm srv.txt")
os.system("rm srvr.txt")


with capture.capture_output() as cap:
  os.system("cd /content/personalized-diffusion/stable-diffusion/")


os.system("python /content/personalized-diffusion/stable-diffusion-webui/webui.py --disable-safe-unpickle --ckpt '{}'".format(MODEL_PATH))