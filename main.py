import subprocess
from threading import Timer


def nuggets_worm(url, data=None, timer_time=8, curl_time=8):
    if data is None:
        cmd = ['curl', '--user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                                       '(KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36', '--connect-timeout',
               str(curl_time), '-m', str(curl_time), url]
    else:
        cmd = ['curl', '--user-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                                       '(KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36', '--connect-timeout',
               str(curl_time), '-m', str(curl_time), '-d', data, url]
    sub = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    timer = Timer(timer_time, lambda process: process.kill(), [sub])
    try:
        timer.start()
        stdout, stderr = sub.communicate()
    except Exception as err:
        print('error:', err)
        return ""
    finally:
        timer.cancel()

    return stdout.decode('utf-8')
