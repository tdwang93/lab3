#!/usr/bin/env python3
'''Lab 3 Inv 2 function free_space '''
# Author ID: [seneca_id]

import subprocess

def free_space():
    """Return the free disk space on the root directory."""
    # Launch the command and capture its output
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         shell=True)
    output, error = p.communicate()

    if error:
        return f'Error: {error.decode("utf-8").strip()}'
    
    # Decode the output from bytes to string and strip newline characters
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
