import tkinter as tk
import logging
from bitmex import get_tickers

logger = logging.getLogger()

logger.setLevel(logging.INFO)

# Adding Stream Handler for messages
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

# Adding File Handler for logs
file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# Logger messages
logger.debug("This message is important only when debugging the program")
logger.info("This message just shows basic information")
logger.warning("This message is about something you should pay attention to")
logger.error("This message helps to debug an error that occurred in your program")

# Only executes if main is executed
if __name__ == '__main__':

    tickers = get_tickers()
    root = tk.Tk()
    root.configure(bg="grey12")
    i = 0
    j = 0

    for ticker in tickers:
        label_widget = tk.Label(root, text=ticker, bg='grey12',fg='SteelBlue1', width=13, font=("Arial", 11, "normal"))
        label_widget.grid(row=i, column=j, sticky='ew')
        if i == 4:
            j+=1
            i = 0
        else:
            i+=1
    root.mainloop()