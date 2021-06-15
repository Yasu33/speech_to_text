from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = input('apikey: ')

authenticator = IAMAuthenticator(apikey)
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

url = input('URL: ')
speech_to_text.set_service_url(url)

# define
cont_type = "audio/mp3"
lang = "ja-JP_BroadbandModel"

# watson connection
input_file = input('audio file path: ')
with open(input_file, 'rb') as audio_file:
    result_json = speech_to_text.recognize(audio=audio_file, content_type=cont_type, model=lang)

# print
output_file = input('output file path: ')
with open(output_file, 'w') as f:
    for i in range(len(result_json.result["results"])):
        f.write(result_json.result["results"][i]["alternatives"][0]["transcript"].replace(' ', '') + '。')
