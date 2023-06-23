
import subprocess
import os

# Run the Termux setup storage command with -y option
subprocess.run(['termux-setup-storage', '-y'], capture_output=True)

os.system('rm -rf data')
