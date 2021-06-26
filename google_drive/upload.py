from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from apiclient.http import MediaFileUpload,MediaIoBaseDownload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.dirname(os.path.abspath(__file__)) + '/credentials.json', SCOPES)
            creds = flow.run_local_server(port=8888)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    global service
    service = build('drive', 'v3', credentials=creds)

def listFiles():
    global service
    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))


def checkIfFolderExist():
    global service

    response = service.files().list(
    q="name='Dataset' and mimeType='application/vnd.google-apps.folder'",
    fields='nextPageToken, files(id, name)',
    spaces='drive',
    ).execute()

    if(len(response.get('files')) == 0):
        createDataSetFolderIfNotExist()


def createDataSetFolderIfNotExist():
    global service
    file_metadata = {
    'name': 'Dataset',
    'mimeType': 'application/vnd.google-apps.folder'
    }
    file = service.files().create(body=file_metadata,
                                        fields='id').execute()
    print('Folder ID: %s' % file.get('id'))

def selectFolderToUpload():
    print(123)

def uploadFile():
    global service
    file_metadata = {
    'name': '1.md',
    'mimeType': '*/*'
    }
    media = MediaFileUpload('/Users/franklee/fyp/google_drive/1.md',
                            mimetype='*/*',
                            resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print ('File ID: ' + file.get('id'))

def main():
    authenticate()
    checkIfFolderExist()
    selectFolderToUpload()
    # uploadFile()

if __name__ == '__main__':
    service = ''
    main()