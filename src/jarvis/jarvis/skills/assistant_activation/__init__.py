import sys
import time
import logging
from datetime import datetime

from jarvis.utils.application_utils import clear
from jarvis.utils.response_utils import assistant_response
from jarvis.utils.application_utils import play_activation_sound


def enable_jarvis(**kwargs):
    """
    Creates the assistant respond according to the datetime hour and
    updates the execute state.
    """
    play_activation_sound()
    time.sleep(2)

    now = datetime.now()
    day_time = int(now.strftime('%H'))

    if day_time < 12:
        assistant_response('Good morning human')
        time.sleep(2)
    elif 12 <= day_time < 18:
        assistant_response('Good afternoon human')
        time.sleep(2)
    else:
        assistant_response('Good evening human')
        time.sleep(2)
    assistant_response('What do you want?')

    return {'ready_to_execute': True,
            'enable_time': now}


def disable_jarvis(**kargs):
    """
    Shutdown the assistant service
    :param args:
    :return:
    """
    assistant_response('Bye')
    time.sleep(1)
    clear()
    logging.debug('Application terminated gracefully.')
    sys.exit()