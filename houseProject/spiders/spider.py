# -*- coding:utf-8 -*-
import scrapy
import sys, io, os
import json
# 设置了init.py 要这样导入
from houseProject import items

class houseSpider(scrapy.Spider):
	name = 'houseSpider'
	allowed_domains = ['lianjia.com']
	start_urls = {
		'https://gz.fang.lianjia.com/loupan/nansha/pg1/?_t=1'
	}
	# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gbk')
	# sys.setrecursionlimit(1000000)

	# 处理response
	def parse(self, response):

		datas = json.loads(response.text)
		# 该页的全部房产
		list_data = datas['data']['list']
		HouseprojectItem = items.HouseprojectItem()
		now_page = datas['data']['selected']['pager']['page']
		pagesize = datas['data']['selected']['pager']['pagesize']

		for data in list_data:
			# 地址
			HouseprojectItem['address'] = data['address']
			# 均价
			HouseprojectItem['average_price'] = data['average_price']
			# 起始均价
			HouseprojectItem['avg_price_start'] = data['avg_price_start']
			# 单位
			HouseprojectItem['avg_price_start_unit'] = data['avg_price_start_unit']
			# 商圈
			HouseprojectItem['bizcircle_name'] = data['bizcircle_name']
			# 城市Id
			HouseprojectItem['city_id'] = data['city_id']
			# 城市
			HouseprojectItem['city_name'] = data['city_name']
			# 标签
			HouseprojectItem['tags'] = data['tags']
			# 最低总价
			HouseprojectItem['total_price_start'] = data['total_price_start']
			# 总价单位
			HouseprojectItem['total_price_start_unit'] = data['total_price_start_unit']
			# 楼盘名
			HouseprojectItem['title'] = data['title']
			# 最小面积
			HouseprojectItem['min_frame_area'] = data['min_frame_area']
			# 最大面积
			HouseprojectItem['max_frame_area'] = data['max_frame_area']
			# 区名
			HouseprojectItem['district_name'] = data['district_name']
			# yield HouseprojectItem
			# print(HouseprojectItem)
		# 分页处理	
		if now_page < pagesize:
			now_page+= 1
			url = 'https://gz.fang.lianjia.com/loupan/nansha/pg%d/?_t=1' %(now_page)
	
			yield scrapy.Request(url, callback = self.parse)
		


