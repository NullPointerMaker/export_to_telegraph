#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import export_to_telegraph
from export_to_telegraph import export, _formaturl
import os
import sys

urls = [
	'https://card.weibo.com/article/m/show/id/2309404477242603339961?_wb_client_=1'
]

def _test():
	if len(sys.argv) > 1:
		mode = sys.argv[1]
	else:
		mode = ''
	if mode == 'open':
		mode = ''
	for url in urls:
		if not mode in url:
			continue
		print('原文：', url)
		r = export(url, True, True, True)
		print('导出：', r)
		if 'open' in str(sys.argv):
			os.system('open ' + _formaturl(r) + ' -g')
		print('')

if __name__=='__main__':
	_test()