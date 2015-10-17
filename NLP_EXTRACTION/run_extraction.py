#-*- coding: utf-8 -*-

from extraction import *

from na_tools import *
from na_config import *

if __name__ == "__main__":

	excel_noun()

	news_info = nt.loadObjectBinaryFast(DICT_NEWS_INFO)

	for key_, val_ in news_info.iteritems():
		print key_
		MyPrettyPrinter().pprint(news_info[key_])
		if list(val_)[0][2] == None:
			print "+++++++++++++++++++"
			print key_
			print "+++++++++++++++++++"



