import kaggle

# Download the Give Me Some Credit competition data
kaggle.api.competition_download_files('GiveMeSomeCredit', 
                                       path='./credit_data', 
                                       quiet=False)

# If you want to unzip it automatically
import zipfile
import os

zip_file = './credit_data/GiveMeSomeCredit.zip'
if os.path.exists(zip_file):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('./credit_data')
    print("Files extracted successfully")