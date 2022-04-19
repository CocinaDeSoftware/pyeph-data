import requests
import pandas as pd
import zipfile
import os
import wget


MODULE_PATH = os.getcwd()

def _download_url(url, zipe_file_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(zipe_file_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def _get_url(year,periodo):
    url = f'https://www.indec.gob.ar/ftp/cuadros/menusuperior/eph/EPH_usu_{periodo}_Trim_{year}_txt.zip'
    zip_file_name = url.split('/')[-1]
    return url, zip_file_name

def _get_microdata_s3(year,periodo,base_type):
    if year >= 2003 and periodo is not None:
        url = f'https://datasets-humai.s3.amazonaws.com/eph/{base_type}/base_{base_type}_{year}T{periodo}.csv'
    if year <= 2003:
        url = f'https://datasets-humai.s3.amazonaws.com/eph/{base_type}/base_{base_type}_{year}O{periodo}.csv'
    filename = wget.download(url)
    df = pd.read_csv(filename, low_memory=False, encoding='unicode_escape')
    return df

def _download_microdata_internal(year,periodo):
    #
    url,zip_file_name = _get_url(year,periodo)
    #
    unzip_folder = zip_file_name.replace(".zip","")
    #
    zip_file_path = os.path.join(MODULE_PATH,zip_file_name)
    #
    _download_url(url,zip_file_path)
    #
    return zip_file_path,unzip_folder

    
def unzip_file(zip_file_path,unzip_folder):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(f'{os.path.join(MODULE_PATH,unzip_folder)}/')

        
def _get_microdata_internal(year,periodo,base_type):
    #
    zip_file_path,unzip_folder = _download_microdata_internal(year,periodo,base_type)
    #
    unzip_file(zip_file_path,unzip_folder)
    #
    for file in os.listdir(os.path.join(MODULE_PATH,unzip_folder)):
        if base_type == 'hogar' and "hogar" in file:
            return_file = file
        if base_type == 'individual' and "individual" in file:
            return_file = file
    df = pd.read_csv(os.path.join(MODULE_PATH,unzip_folder,return_file),sep=';',low_memory=False)
    return df


def get_micro_data(year = 2018, periodo = None, base_type='individual'):
        
        if year <= 2018:
            df = _get_microdata_s3(year,periodo,base_type)
        else:
            df = _get_microdata_internal(year,periodo,base_type)
        return df
        

for y in range(1996, 2021):
    for t in [1,2,3,4]:
        for b in ['individual', 'hogar']:
            try:
                get_micro_data(year=y, periodo=t, base_type=b)
            except:
                print(f"NO PUDE DESCARGAR {y} {t} {b}")