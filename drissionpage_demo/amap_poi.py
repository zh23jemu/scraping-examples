"""
这里用的不是最新版的高德API,最新版的地址如下:
https://lbs.amap.com/api/webservice/guide/api-advanced/newpoisearch

"""


import json

import requests

from DrissionPage import ChromiumPage


class GaodeAPI:
    """
    高德API接口版本
    """

    def __init__(self, key, city='北京', keyword=None):
        self.key = key
        self.keyword = keyword
        self.city = city
        self.offset = 20

    def get_poi_total_list(self):
        """
        获取POI列表
        :return:
        """
        first_page = self.get_poi_page(pagenum=1)
        if first_page['infocode'] == '10044':
            raise Exception('当日查询已限额，请明天再试.')
        page_count = int(first_page['count'])
        iterate_num = round(page_count / self.offset) + 1
        final_result = []
        for i in range(1, iterate_num):
            temp_result = self.get_poi_page(i)
            final_result.extend(temp_result['pois'])

        return final_result

    def get_poi_page(self, pagenum):
        """
        获取POI详情
        :param pagenum:
        :return:
        """
        url = f'https://restapi.amap.com/v3/place/text?city={self.city}&offset={self.offset}&page={pagenum}&key={self.key}&types=011100|011102|011103&extensions=all'

        response = requests.get(url)
        result = json.loads(response.text)

        return result


def handle_detail(poi_list):
    """
    处理POI详情信息
    :return:
    """
    try:
        base_url = "https://amap.com/place/"

        page = ChromiumPage()
        page.get(base_url)  # 访问网址，这行产生的数据包不监听

        page.listen.start('amap.com/detail/get/detail')  # 开始监听，指定获取包含该文本的数据包
        for poi in poi_list:
            poi_id = poi['id']
            page.get(base_url + poi_id)
            res = page.listen.wait()  # 等待并获取一个数据包
            detail_json = res.response.body
            detail_json = detail_json['data']
            # db.update(table='gaode_pois',
            #           data={'detail_json_data': json.dumps(detail_json)},
            #           condition=f" poi_id = '{poi_id}'"
            #           )
            print(f"{poi_id}详细信息采集完成.")
            print(detail_json)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    gaode_api = GaodeAPI(key='7c60b8993e35cb838239e25dd477cbcb')
    result = gaode_api.get_poi_page(pagenum=1)['pois']

    handle_detail(result)
