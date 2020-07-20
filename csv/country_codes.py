from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回pygal使用的两个字母的国别码"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None  #没有找到指定的国家就返回None

