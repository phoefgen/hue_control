#! ./venv/bin/python
'''Base module for testing the dev environment '''

import requests

def hello():
    '''Returns a string: MVP for testing suite. '''
    return 'hello'

def set_light(light_num, state, hue, saturation, brightness):
    '''Switch on a specified light, with specific attributes'''

    bridge_username = 'cfe4dS8DAP7JdIBS-D6fyelIAHiwk5qZ21sypFek'
    bridge_ip = '192.168.1.64'


    url = 'http://{bridge_ip}/api/{bridge_username}/lights/{light_num}/state'.format(bridge_ip = bridge_ip,
                                                                              bridge_username = bridge_username,
                                                                              light_num = light_num)
    data = '{"hue": %s, "on": %s, "sat": %s, "bri": %s}' % (hue, state, saturation, brightness)

    r = requests.put(url, data)

    return

def main():
    '''Testing unittest code '''
    hello()

    light_num = 9
    state = True
    hue = "null"
    saturation = 254
    brightness = 254

    set_light(light_num, state, hue, saturation, brightness)

if __name__ == '__main__':
    '''Init Function '''
    main()
