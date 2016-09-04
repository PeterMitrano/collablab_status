import requests

def lambda_handler(event, context):
    response = requests.get('http://collablab.wpi.edu/lab/status')

    if response.ok:
        data = response.json()
        print data

        if data['open']:
            members = data['members'].keys()
            members_speech = ', '.join(members)
            return {
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': 'The collab lab open. The current members are, ' + members_speech
                    }
                }
            }
        else:
            return {
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': 'The collab lab closed'
                    }
                }
            }
    else:
        return {
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': 'The collab lab website is down'
                }
            }
        }

if __name__ == '__main__':
    lambda_handler({}, {})
