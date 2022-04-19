import os
import glob
import zipfile

MODULE_PATH = os.getcwd()

csv_filenames = glob.glob('./*.csv')

for filename in csv_filenames:

	with zipfile.ZipFile(filename.replace(".csv", ".zip"), 'w') as myzip:
		myzip.write(filename, compress_type=zipfile.ZIP_DEFLATED)

print("Listo! Compresion completa")