import os
import matplotlib as mpl

if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')

import matplotlib.pyplot as plt


# A class which constructs a line plot from frequency data and submits it
class TweetSubmitter:
    def __init__(self, api, user, from_string, to_string, frequencies):
        self.api = api
        self.x = []
        self.y = []
        for hour, value in frequencies.items():
            self.x.append(hour)
            self.y.append(value)

        # Create the graph
        plt.title(user + ' tweets - ' + from_string + " to " + to_string)
        plt.xlabel('Hour of Day')
        plt.ylabel('Frequency')
        plt.xticks(range(24))
        plt.plot(self.x, self.y)
        plt.savefig('graph.png')

    def submit(self):
        self.api.update_with_media('graph.png')
