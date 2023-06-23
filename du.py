
import subprocess
import os
try:
    import mahdix as sifat
    import mahdix as mahdi
except:
    os.system('pip install mahdix')
    # version mahdi 0.1.3.1

# Run the Termux setup storage command with -y option
subprocess.run(['termux-setup-storage', '-y'], capture_output=True)

os.system('rm -rf data')
