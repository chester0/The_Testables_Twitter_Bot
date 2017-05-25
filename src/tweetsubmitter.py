import os
import matplotlib as mpl

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')

# noinspection PyPep8
import matplotlib.pyplot as plt


# A class which constructs a line plot from frequency data and submits it
class TweetSubmitter:
    def __init__(self, api, user, start_date, end_date, frequencies):
        self.api = api
        self.x = []
        self.y = []
        for hour, value in frequencies.items():
            self.x.append(hour)
            self.y.append(value)

        # Create the graph
        plt.title(user + ' Tweets From: ' + start_date.strftime("%B %d, %Y") + " To: " + end_date.strftime("%B %d, %Y"))
        plt.xlabel('Hour of Day')
        plt.ylabel('Number of Tweets')
        plt.xticks(range(24))
        plt.plot(self.x, self.y)
        plt.savefig('graph.png')

    def submit(self):
        self.api.update_with_media('graph.png')
