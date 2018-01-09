import glob
import os
import subprocess
import tempfile
import zipfile

print('Extracting packages')

zip_file = zipfile.ZipFile(os.path.dirname(__file__))
temp_dir = tempfile.mkdtemp()
zip_file.extractall(temp_dir)
os.chdir(temp_dir)

print('Installing Deps')

paths = glob.glob(os.path.join('.', 'deps', '*'))
subprocess.check_call(['python', '-m', 'pip', 'install', '--no-index', '--no-deps', '--upgrade', '--force-reinstall', '--find-links=.'] + paths)

