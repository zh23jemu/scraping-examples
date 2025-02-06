import requests
import execjs

cookies = {
    'thw': 'cn',
    't': 'd45a1bdac31aea9cea5f3a60a2797af7',
    '_samesite_flag_': 'true',
    'cookie2': '192ce14c3543177fa3a87af19a630987',
    'havana_lgc2_0': 'eyJoaWQiOjUwNjYyODkwLCJzZyI6ImUxZmEwNjRhYWQzMThlMTcxZjFmZjBjOTZhMDdkMzA0Iiwic2l0ZSI6MCwidG9rZW4iOiIxaEZaVWszVVQ0c0xuUHZIR1VWV2NrdyJ9',
    '_hvn_lgc_': '0',
    'wk_cookie2': '1b65796fe1f92c6774c9a9eed97293ed',
    'wk_unb': 'Vv7P6GQvoQA%3D',
    'useNativeIM': 'false',
    'wwUserTip': 'false',
    '_uetvid': 'a7d58d309e3a11ef8cc8791ad86f9459',
    'unb': '50662890',
    'sn': '',
    'lgc': 'zh23_emu',
    'cancelledSubSites': 'empty',
    'publishItemObj': 'Ng%3D%3D',
    'tracknick': 'zh23_emu',
    '_l_g_': 'Ug%3D%3D',
    'cna': 'PbabH1o0HjsCAXBRDezmK1tA',
    'sgcookie': 'E1008TInMOxfy6u3I%2F92irO4nCVSUYJc30vaxKCUCcNnyCzGszASnWCAyD17Mb%2BHBCzXdXHMaUwwgdlfCEm7xSSPoGjnLfRGPyWgZtNgU38qV44C5G%2Fkk%2BlvHibQEgC4kMIo',
    'havana_lgc_exp': '1769416261344',
    'uc1': 'cookie21=VT5L2FSpdet1EftGlDZ1Vg%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&existShop=false&cookie14=UoYdVUs9kJ4K7g%3D%3D&pas=0',
    'uc3': 'id2=Vv7P6GQvoQA%3D&nk2=GcBiOHo1eAY%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dD2EwPUWH9XgrqF4Q%3D',
    'csg': 'b2a600af',
    'cookie17': 'Vv7P6GQvoQA%3D',
    'dnk': 'zh23_emu',
    'skt': '7be2b75e55346269',
    'existShop': 'MTczODMxMjI2MQ%3D%3D',
    'uc4': 'nk4=0%40GwkTGQm%2BPY88GDlZKbe9xePOeA%3D%3D&id4=0%40VHjzmjyp7JxwqezRCUanmI8k5A%3D%3D',
    '_cc_': 'VT5L2FSpdA%3D%3D',
    'sg': 'u09',
    '_nk_': 'zh23_emu',
    'cookie1': 'BxUFpUpE5KuS27e5bVc0QMYQbY8q0JGwyPUVYu8DMkE%3D',
    '_tb_token_': 'e7a3e37d6eb51',
    'sdkSilent': '1738818886283',
    'havana_sdkSilent': '1738818886283',
    'xlly_s': '1',
    'mtop_partitioned_detect': '1',
    '_m_h5_tk': '84e0a209e1907d03d9fc49b2fed58df4_1738815675215',
    '_m_h5_tk_enc': '50bc56e2760f40b2ede35200dd2b924a',
    'tfstk': 'gAb-NGw68-2upowTUarDtfca-SP0sofzET5s-pvoAtBAOK03aUqeJ9pALLxkPL0pJ6BFK9CUaB9Cd9phqo4Ga_8eRRXLSPfrKUWZ-aLIKsTyt3y0ix4Ga_ljwvNGcPDp6h26RD9CdEtXtQTBNLtQMKO9h4OIPBMbMKRBR4tSPj9X1QiIPe6CGSdehpTBV9TjaTyphb9nJGEtkuuToI3IRZdJVofWh2OVkQKJC__-R2Gew3p1NKwaTPDvc6-d8Xupx_sNLC6SFJpFks_5fOwmqLs991jdCWmyiHQykp_77fpfy6Qv4iDSVCLJeh_WfyFO1HsAkUb7Lc5cMLt9oiq4EHYReGJwVoyVpspldaKje-vhjsbWDOwmk9-dAaYfP-aO4K7GWaKqIddnVSFxYD-WgPAll3McGRzpMdV8JDoe0Sun2N4mYD-WgIpgwynEYnPV.',
    'isg': 'BLm5U9P--gwSzqYfTQzQGOmAyCWTxq14LKYgWNvuN-BeYtn0IxdkSF205GaUWkWw',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': 'thw=cn; t=d45a1bdac31aea9cea5f3a60a2797af7; _samesite_flag_=true; cookie2=192ce14c3543177fa3a87af19a630987; havana_lgc2_0=eyJoaWQiOjUwNjYyODkwLCJzZyI6ImUxZmEwNjRhYWQzMThlMTcxZjFmZjBjOTZhMDdkMzA0Iiwic2l0ZSI6MCwidG9rZW4iOiIxaEZaVWszVVQ0c0xuUHZIR1VWV2NrdyJ9; _hvn_lgc_=0; wk_cookie2=1b65796fe1f92c6774c9a9eed97293ed; wk_unb=Vv7P6GQvoQA%3D; useNativeIM=false; wwUserTip=false; _uetvid=a7d58d309e3a11ef8cc8791ad86f9459; unb=50662890; sn=; lgc=zh23_emu; cancelledSubSites=empty; publishItemObj=Ng%3D%3D; tracknick=zh23_emu; _l_g_=Ug%3D%3D; cna=PbabH1o0HjsCAXBRDezmK1tA; sgcookie=E1008TInMOxfy6u3I%2F92irO4nCVSUYJc30vaxKCUCcNnyCzGszASnWCAyD17Mb%2BHBCzXdXHMaUwwgdlfCEm7xSSPoGjnLfRGPyWgZtNgU38qV44C5G%2Fkk%2BlvHibQEgC4kMIo; havana_lgc_exp=1769416261344; uc1=cookie21=VT5L2FSpdet1EftGlDZ1Vg%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&existShop=false&cookie14=UoYdVUs9kJ4K7g%3D%3D&pas=0; uc3=id2=Vv7P6GQvoQA%3D&nk2=GcBiOHo1eAY%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dD2EwPUWH9XgrqF4Q%3D; csg=b2a600af; cookie17=Vv7P6GQvoQA%3D; dnk=zh23_emu; skt=7be2b75e55346269; existShop=MTczODMxMjI2MQ%3D%3D; uc4=nk4=0%40GwkTGQm%2BPY88GDlZKbe9xePOeA%3D%3D&id4=0%40VHjzmjyp7JxwqezRCUanmI8k5A%3D%3D; _cc_=VT5L2FSpdA%3D%3D; sg=u09; _nk_=zh23_emu; cookie1=BxUFpUpE5KuS27e5bVc0QMYQbY8q0JGwyPUVYu8DMkE%3D; _tb_token_=e7a3e37d6eb51; sdkSilent=1738818886283; havana_sdkSilent=1738818886283; xlly_s=1; mtop_partitioned_detect=1; _m_h5_tk=84e0a209e1907d03d9fc49b2fed58df4_1738815675215; _m_h5_tk_enc=50bc56e2760f40b2ede35200dd2b924a; tfstk=gAb-NGw68-2upowTUarDtfca-SP0sofzET5s-pvoAtBAOK03aUqeJ9pALLxkPL0pJ6BFK9CUaB9Cd9phqo4Ga_8eRRXLSPfrKUWZ-aLIKsTyt3y0ix4Ga_ljwvNGcPDp6h26RD9CdEtXtQTBNLtQMKO9h4OIPBMbMKRBR4tSPj9X1QiIPe6CGSdehpTBV9TjaTyphb9nJGEtkuuToI3IRZdJVofWh2OVkQKJC__-R2Gew3p1NKwaTPDvc6-d8Xupx_sNLC6SFJpFks_5fOwmqLs991jdCWmyiHQykp_77fpfy6Qv4iDSVCLJeh_WfyFO1HsAkUb7Lc5cMLt9oiq4EHYReGJwVoyVpspldaKje-vhjsbWDOwmk9-dAaYfP-aO4K7GWaKqIddnVSFxYD-WgPAll3McGRzpMdV8JDoe0Sun2N4mYD-WgIpgwynEYnPV.; isg=BLm5U9P--gwSzqYfTQzQGOmAyCWTxq14LKYgWNvuN-BeYtn0IxdkSF205GaUWkWw',
    'referer': 'https://s.taobao.com/search?commend=all&ie=utf8&initiative_id=tbindexz_20170306&page=1&preLoadOrigin=https%3A%2F%2Fwww.taobao.com&q=%E6%97%A0%E7%BA%BF%E7%BD%91%E5%8D%A1&search_type=item&sourceId=tb.index&spm=a21bo.jianhua%2Fa.201856.d13&ssid=s5-e&tab=all',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Microsoft Edge";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
}

params = {
    'jsv': '2.7.4',
    'appKey': '12574478',
    't': '1738806692516',
    'sign': '93da8c06f591c2df4e3c489898c1c324',
    'api': 'mtop.relationrecommend.wirelessrecommend.recommend',
    'v': '2.0',
    'timeout': '10000',
    'type': 'jsonp',
    'dataType': 'jsonp',
    'callback': 'mtopjsonp5',
    'data': '{"appId":"34385","params":"{\\"device\\":\\"HMA-AL00\\",\\"isBeta\\":\\"false\\",\\"grayHair\\":\\"false\\",\\"from\\":\\"nt_history\\",\\"brand\\":\\"HUAWEI\\",\\"info\\":\\"wifi\\",\\"index\\":\\"4\\",\\"rainbow\\":\\"\\",\\"schemaType\\":\\"auction\\",\\"elderHome\\":\\"false\\",\\"isEnterSrpSearch\\":\\"true\\",\\"newSearch\\":\\"false\\",\\"network\\":\\"wifi\\",\\"subtype\\":\\"\\",\\"hasPreposeFilter\\":\\"false\\",\\"prepositionVersion\\":\\"v2\\",\\"client_os\\":\\"Android\\",\\"gpsEnabled\\":\\"false\\",\\"searchDoorFrom\\":\\"srp\\",\\"debug_rerankNewOpenCard\\":\\"false\\",\\"homePageVersion\\":\\"v7\\",\\"searchElderHomeOpen\\":\\"false\\",\\"search_action\\":\\"initiative\\",\\"sugg\\":\\"_4_1\\",\\"sversion\\":\\"13.6\\",\\"style\\":\\"list\\",\\"ttid\\":\\"600000@taobao_pc_10.7.0\\",\\"needTabs\\":\\"true\\",\\"areaCode\\":\\"CN\\",\\"vm\\":\\"nw\\",\\"countryNum\\":\\"156\\",\\"m\\":\\"pc\\",\\"page\\":1,\\"n\\":48,\\"q\\":\\"%E6%97%A0%E7%BA%BF%E7%BD%91%E5%8D%A1\\",\\"qSource\\":\\"url\\",\\"pageSource\\":\\"a21bo.jianhua/a.201856.d13\\",\\"tab\\":\\"all\\",\\"pageSize\\":48,\\"totalPage\\":100,\\"totalResults\\":4800,\\"sourceS\\":\\"0\\",\\"sort\\":\\"_coefp\\",\\"bcoffset\\":\\"\\",\\"ntoffset\\":\\"\\",\\"filterTag\\":\\"\\",\\"service\\":\\"\\",\\"prop\\":\\"\\",\\"loc\\":\\"\\",\\"start_price\\":null,\\"end_price\\":null,\\"startPrice\\":null,\\"endPrice\\":null,\\"itemIds\\":null,\\"p4pIds\\":null,\\"p4pS\\":null,\\"categoryp\\":\\"\\",\\"ha3Kvpairs\\":null,\\"myCNA\\":\\"PbabH1o0HjsCAXBRDezmK1tA\\"}"}',
    # data中的page用于控制翻页
}

with open('taobao_search.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)

result = ctx.call('getParams', params['data'])
params['t'] = result['t']
params['sign'] = result['sign']

response = requests.get(
    'https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/',
    params=params,
    cookies=cookies,
    headers=headers,
)

print(response.text)