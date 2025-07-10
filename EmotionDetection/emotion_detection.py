import requests,json

def emotion_detector(text_to_analyze):
    
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, headers=headers, json=myobj )


    if response.status_code == 200:

        jsonFormated = json.loads(response.text)
        emotions = jsonFormated['emotionPredictions'][0]['emotion']
        nameDominant = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = nameDominant

    elif response.status_code == 400:
        
        emotions = {'anger': None,'disgust': None,'fear': None,
        'joy': None,'sadness': None,'dominant_emotion': None}

    return emotions
