import requests

def lambda_handler(event, context):
    response = requests.get('http://collablab.wpi.edu/lab/status')

    if response.ok:
        data = response.json()

        if data['open']:

            members = [member for _, member in data['members'].iteritems()]
            print members
            members_speech = ', '.join(members)
            return {
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': 'The collab lab is open. The current members are, ' + members_speech
                    }
                }
            }
        else:
            return {
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': 'The collab lab is closed'
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
