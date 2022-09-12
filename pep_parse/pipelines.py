from itemadapter import ItemAdapter
import datetime as dt
import csv
from collections import defaultdict
from pep_parse.constants import BASE_DIR


class PepParsePipeline:

    def __init__(self):
        self.status_summary = defaultdict()

    def open_spider(self, spider):
        keys = ['Статус', 'Количество']
        now = dt.datetime.now()
        current_date = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = 'status_summary'
        downloads_dir = BASE_DIR / 'results'
        downloads_dir.mkdir(exist_ok=True)
        infile = open('{}/{}_{}.csv'.format(
            downloads_dir, filename, current_date), 'w')

        self.dict_writer = csv.DictWriter(infile, keys)
        self.dict_writer.writeheader()

    def process_item(self, item, spider):

        status = item['status']
        if status in self.status_summary:
            self.status_summary[status] += 1
        else:
            self.status_summary[status] = 1
        return item

    def close_spider(self, spider):
        self.status_summary['Total'] = sum(self.status_summary.values())
        for key, value in self.status_summary.items():
            self.dict_writer.writerow({'Статус': key, 'Количество': value})
