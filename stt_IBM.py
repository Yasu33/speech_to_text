from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apikey}')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)
speech_to_text.set_service_url('{url}')

# define
audio_file = open("{file}", "rb")
cont_type = "audio/flac"
lang = "en-US_BroadbandModel"

# watson connection
result_json = speech_to_text.recognize(audio=audio_file, content_type=cont_type, model=lang)

# print
for i in range(len(result_json.result["results"])):
    print(result_json.result["results"][i]["alternatives"][0]["transcript"])
