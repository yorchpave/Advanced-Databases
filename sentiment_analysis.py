# encoding: utf-8
import requests, json
# User token, required for API access
oauth_token = '6cc81fa0e4cc49d69bc0900a5aee54d9'

# API request data: Language and text to be analyzed
user_language = "spa"
file = open("tweets.txt", "r")
user_text = file.read()
file.close()

print ("\nBITEXT API. Sentiment Analysis endpoint. Python sample code\n")
print ("--------------------------------------------------\n\n")

# Building the POST request to sentiment analysis endpoint
endpoint = "https://svc02.api.bitext.com/sentiment/"
headers = { "Authorization" : "bearer " + oauth_token, "Content-Type" : "application/json" }
params = { "language" : user_language, "text" : user_text }

# Sending the POST request
res = requests.post(endpoint, headers=headers, data=json.dumps(params))

# Processing the result of the POST request
post_result = json.loads(res.text).get('success')   # Success of the request
post_result_code = res.status_code                  # Error code, if applicable
post_msg = json.loads(res.text).get('message')      # Error message, if applicable
action_id = json.loads(res.text).get('resultid')    # Identifier to request the analysis results

print("POST: '" + post_msg + "'\n\n")

# 401 is the error code corresponding to an invalid token
if post_result_code == 401:
    print("Your authentication token is not correct\n")

if (post_result):
    print("Waiting for analysis results...\n\n")

    # GET request loop, using the response identifier returned in the POST answer
    analysis = None
    while analysis == None:
        res = requests.get(endpoint + action_id + '/', headers=headers)

        if res.status_code == 200 :
            analysis = res.text

    # The loop ends when we have response to the GET request
    get_msg = res.reason
    print("GET: '" + get_msg + "'\n\n")

    # In the GET response we have the result of the analysis
    print("Analysis results:\n\n")
    parsed = json.loads(analysis)
    print(json.dumps(parsed, indent=2, sort_keys=True))
    i = 0
    total_tweets_analyzed = 0
    total_score = 0.0
    for scores in parsed['sentimentanalysis']:
        #scores += parsed['sentimentanalysis'][1]['score']
        current_sentiment_value = parsed['sentimentanalysis'][i]['score']
        if float(current_sentiment_value) != 0.0:
            total_tweets_analyzed = total_tweets_analyzed + 1
            total_score = total_score + float(current_sentiment_value)
            #print(current_sentiment_value)
            #print("parsed: ", total_score)
            
        i = i + 1
    print("TOTAL SCORE: ", total_score)
    print("TOTAL TWEETS ANALYZED: ", total_tweets_analyzed)
    avg_score = total_score / total_tweets_analyzed
    print("SENTIMENT AVERGAGE: ", avg_score)
    
            

    
