from scrapy import cmdline

# cmdline.execute(['scrapy', 'crawl', 'basic'])
# cmdline.execute(['scrapy', 'crawl', 'manual'])
cmdline.execute(['scrapy', 'crawl', 'qidian', '-s', 'CLOSESPIDER_ITEMCOUNT=90'])
# cmdline.execute(['scrapy', 'crawl', 'easy'])
# cmdline.execute(['scrapy', 'crawl', 'api'])
