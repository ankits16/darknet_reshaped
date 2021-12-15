from distutils.core import setup
from distutils.command.install import install as DistutilsInstall
from setuptools.command.install import install
import subprocess
import sys
import os
# from setuptools.command.build_ext import build_ext
#
# class MyInstall(build_ext):
#     def run(self):
#
#         protoc_command = ["make"]
#         os.chdir('./darknet_src/ai_darknet')
#         # os.system('!make')
#         if subprocess.call(protoc_command) != 0:
#             sys.exit(-1)
#         install.run(self)
#
#
# from setuptools import setup, find_packages
# # with open("README.md", "r", encoding="utf-8") as fh:
# #     long_description = fh.read()
#
# setup(
#     name='ai_darknet',
#     version='0.1',
#     package_dir={'': 'darknet_src'},
#     packages=find_packages(where='darknet_src'),
#     python_requires='>=3.5, <4',
#     install_requires=[
#     ],
#     cmdclass={'build_ext': MyInstall},
#
# )

import sys
import subprocess

from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py
from setuptools import setup, find_packages

class Build(build_ext):
 """Customized setuptools build command - builds protos on build."""
 def run(self):
     protoc_command = ["make"]
     os.chdir('./darknet_src/ai_darknet_reshaped')
     if subprocess.call(protoc_command) != 0:
         sys.exit(-1)
     build_ext.run(self)


setup(
 name='ai_darknet_reshaped',
 version='1.0',
 description='Python Distribution Utilities',
 # packages=['darknet_src', 'darknet_src/ai_darknet_reshaped'],
 packages= find_packages(),
 # packages= find_packages(where='darknet_src/ai_darknet_reshaped'),
                    # find_packages ['ai_darknet_reshaped'],
 has_ext_modules=lambda: True,
 cmdclass={
     'build_ext': Build,
 },
 # packages=['darknet_src'],
)