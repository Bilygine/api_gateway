"""
Downloader http configs
"""

DOWNLOADER_HOST = 'mediator'
DOWNLOADER_ENDPOINT = 'api/download'
DOWNLOADER_PORT = '5000'
DOWNLOADER_URL = 'http://{}:{}/{}'.format(DOWNLOADER_HOST, DOWNLOADER_PORT, DOWNLOADER_ENDPOINT)


"""
Analizer http configs
"""
ANALIZER_HOST = 'analyzer'
ANALIZER_ENDPOINT = 'api/analyzer/execute'
ANALIZER_PORT = '8123'
ANALIZER_URL = 'http://{}:{}/{}'.format(ANALIZER_HOST, ANALIZER_PORT, ANALIZER_ENDPOINT)


"""
API
"""
API_PORT = '8181'



"""
Storage information
"""
BUCKET_NAME = 'bilygine-audio'
GOOGLE_CONTENT_TYPE = 'application/octet-stream'
