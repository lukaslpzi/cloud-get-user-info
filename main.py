import discogs_client
import json

def main(request):
    if not request.args or not 'token' in request.args or not 'secret' in request.args:
        return 'bad params'
    
    token = request.args['token']
    secret = request.args['secret']

    user_agent = 'discogs_api_example/2.0'
    consumer_key = 'DpToaTUkOnKnZaimGtWa'
    consumer_secret = 'cITslCuphJWwiqSQnIgQvKwHXQILTTuq'

    discogsclient = discogs_client.Client(user_agent, consumer_key=consumer_key, consumer_secret=consumer_secret, token=token, secret=secret)

    user = discogsclient.identity()

    return json.dumps({'username': user.name, 'name': user.username }), 200, {'ContentType': 'application/json'}
