from acrcloud.recognizer import ACRCloudRecognizer

config = {
    'host': 'eu-west-1.api.acrcloud.com',
    'access_key': 'access key',
    'access_secret': 'secret key',
    'debug': True,
    'timeout': 10
}

acrcloud = ACRCloudRecognizer(config)

print(acrcloud.recognize_audio('Unstoppable.wav', 0))