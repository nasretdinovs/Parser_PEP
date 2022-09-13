import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import BASE_DIR


class PepParsePipeline:

    def __init__(self):
        self.status_summary = defaultdict()

    def open_spider(self, spider):
        now = dt.datetime.now()
        current_date = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = 'status_summary'
        downloads_dir = BASE_DIR / 'results'
        downloads_dir.mkdir(exist_ok=True)
        infile = open('{}/{}_{}.csv'.format(
            downloads_dir, filename, current_date), 'w')
        self.writer = csv.writer(infile)
        self.writer.writerow(['Статус', 'Количество'])

    def process_item(self, item, spider):
        status = item['status']
        self.status_summary[status] = self.status_summary.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        self.status_summary['Total'] = sum(self.status_summary.values())
        self.writer.writerows(list(self.status_summary.items()))
