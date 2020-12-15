import platform


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def notification(title, message):
    """Sends a notification when the book is saved."""
    plt = platform.system()
    # If OS is MacOS
    if plt == 'Darwin':
        command = f'''
        osascript -e 'display notification "{message}" with title "{title}"'
        '''
        os.system(command)
    # If OS is Linux
    if plt == 'Linux':
        command = f'''
        notify-send "{title}" "{message}"
        '''
        os.system(command)
    # If OS is Windows
    if plt == 'Windows':
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(("%s" % (title)), ("%s" % (message)))
