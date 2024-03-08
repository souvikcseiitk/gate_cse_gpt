import dropbox
import os

# Define your access token
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'

# Initialize Dropbox object
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Specify the Dropbox path and local folder path
dropbox_path = 'C:\Users\souvi\Dropbox'
local_path = '\\wsl.localhost\Ubuntu\home\souvik\gate_cse_gpt\Dropbox'

# Create local folder if it doesn't exist
if not os.path.exists(local_path):
    os.makedirs(local_path)

# List files in the Dropbox folder
for entry in dbx.files_list_folder(dropbox_path).entries:
    # Download each file
    _, res = dbx.files_download(dropbox_path + '/' + entry.name)
    data = res.content
    
    # Write the downloaded file to the local folder
    with open(os.path.join(local_path, entry.name), 'wb') as f:
        f.write(data)

print("Files downloaded successfully!")
