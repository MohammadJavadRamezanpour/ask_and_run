from functools import wraps

from PyQt6.QtWidgets import QMessageBox


def ask_and_run(title="Confirm?", description="Are You Sure You want to do this?"):
    """
    a decorator wich can get params and decorate any function
    it will run the functin if user selects yes
    
    title (str): the title of the propmt
    description (str): the text of the propmt

    returns: decorated callable function
    """
    def first_wrapper(func):
        @wraps(func)
        def wraper(*args, **kwargs):

            # create and run the message box
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Question)
            msg_box.setWindowTitle(title)
            msg_box.setText(description)
            msg_box.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            result = msg_box.exec()

            # run the function if user selects yes
            if result == QMessageBox.StandardButton.Yes:
                return func(*args, **kwargs)

        return wraper

    return first_wrapper
