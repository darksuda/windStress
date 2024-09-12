from argovisHelpers import helpers as avh
import json
import pandas as pd

from APP_ARGO_FLOATS.set_argo_float_info import create_root_dir, get_coords_by_area

API_KEY='7f8d3cf6ecbf39891eca1273dda99216809e8fa0'
API_PREFIX = 'https://argovis-api.colorado.edu/'

def request_argo_data_by_area(area_name, startDate, endDate):
        filedir = f'APP_ARGO_FLOATS/data/data_argo_{area_name}_{startDate[:10]}_{endDate[:10]}.json'
        create_root_dir()
        area = get_coords_by_area(area_name)
        area = str([[area['west'],area['north']],[area['east'],area['north']],[area['east'],area['south']],[area['west'],area['south']],[area['west'],area['north']]])

        params = {
                'startDate': f'{startDate}T00:00:00Z',
                'endDate': f'{endDate}T00:00:00Z',
                'source': 'argo_core',                    
                'polygon': json.loads(area),
                'data': 'all'
        }

        d = avh.query('argo', options=params, apikey=API_KEY, apiroot=API_PREFIX)

        data = open(filedir, 'w')
        data.write(json.dumps(d))
        data.close()

        return filedir


def request_argo_data_by_platform(platform):
        filedir = f"APP_ARGO_FLOATS/data/data_argo_floats_{platform}.json"

        params = {
        'platform': json.loads(platform),
        'data': 'all'
        }

        d = avh.query('argo', options=params, apikey=API_KEY, apiroot=API_PREFIX)
        data = open(filedir, 'w')
        data.write(json.dumps(d))
        data.close()

        return filedir
