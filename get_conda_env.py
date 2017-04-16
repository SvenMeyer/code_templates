# -*- coding: utf-8 -*-
"""
get environment information

"""

import os
import sys
import subprocess

import tensorflow as tf
import theano
import keras
import google.protobuf

# run 3 different approaches to get conda environment
def get_env():
    sp = sys.path[1].split("/")
    if "envs" in sp:
        s = sp[sp.index("envs") + 1]
    else:
        s =  ""
        
#   s = s +  ' *** ' + os.environ['CONDA_DEFAULT_ENV']
'''
    with subprocess.Popen(["conda", "env" , "list"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        output, error = process.communicate()
        lines = output.decode('utf-8').splitlines()
        for l in lines:
            if '*' in l:
                break
        s =  s +  ' *** ' + l.split()[0]
    
    return s
'''
print("ENVIRONMENT: ", end='')
print(get_env())
print("tensorflow.__version__ = ", tf.__version__)
print("theano.__version__ = ", theano.__version__)
print("keras.__version__ = ", keras.__version__)
print("google.protobuf.__version__ = ", google.protobuf.__version__)
print("------------------------------------------------------------------")
