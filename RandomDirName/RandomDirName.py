#Use: python3 RandomDirName.py <path> <random_string_length>

import os
import string
import random
import sys

def RandomDirName(target_path, rndstr_len):

  for bef_dir in os.listdir(target_path):
    aft_dir = ""
    for i in range(int(rndstr_len)):
      aft_dir += random.choice(string.ascii_letters)

    bef_abspath = os.path.join(target_path, bef_dir)
    aft_abspath = os.path.join(target_path, aft_dir)

    os.rename(bef_abspath, aft_abspath)
