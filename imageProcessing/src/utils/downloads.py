'''
    Utility functions for loading weights.
'''
from __future__ import print_function

import io

import gdown

# import google.auth
# # from google.oauth2.credentials import Credentials
# from google.auth.credentials import Credentials
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from googleapiclient.http import MediaIoBaseDownload


def download_weights(checkpoint_fpath, model_size='L'):
    '''
        Downloads weights from Google Drive.
    '''

    download_id = '12h-NgryAf6zZdA1KclHdfzU35D1icjEp' if model_size.strip(
    ).upper() == 'L' else '1p91KBj-oUmuMfG2Gc33tEN5Js5HpV8YH'
    download_id = '1jZQ9eb21Ijx22Ts0oTNGrK7-WbQkjT5r'

    gdown.download(
        f'https://drive.google.com/uc?id={download_id}', checkpoint_fpath, quiet=False, speed=15000*1024)


# def download_file(path, real_file_id='1jZQ9eb21Ijx22Ts0oTNGrK7'):
#     """Downloads a file
#     Args:
#         real_file_id: ID of the file to download
#     Returns : IO object with location.

#     Load pre-authorized user credentials from the environment.
#     TODO(developer) - See https://developers.google.com/identity
#     for guides on implementing OAuth2 for the application.
#     """
#     # creds, _ = google.auth.default(None, request)

#     try:
#         # create drive api client
#         service = build('drive', 'v3')

#         file_id = real_file_id

#         # pylint: disable=maybe-no-member
#         request = service.files().get_media(fileId=file_id)
#         fh = io.FileIO(path, 'wb')
#         downloader = MediaIoBaseDownload(fh, request)
#         done = False
#         while done is False:
#             status, done = downloader.next_chunk()
#             print(F'Download {int(status.progress() * 100)}.')

#     except HttpError as error:
#         print(F'An error occurred: {error}')
#         file = None

#     return file.getvalue()


# if __name__ == '__main__':
#     download_file('./test.pt', '1KuPmvGq8yoYgbfW74OENMCB5H0n_2Jm9')
