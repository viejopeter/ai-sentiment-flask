import requests,json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, headers=headers, json=myobj )
    jsonFormated = json.loads(response.text)
    emotions = jsonFormated['emotionPredictions'][0]['emotion']
    nameDominant = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = nameDominant
    return  emotions
