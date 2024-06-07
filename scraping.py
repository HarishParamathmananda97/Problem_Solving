import requests
# from bs4 import BeautifulSoup
import json 
import sys
from datetime import datetime, timedelta
#UDF package
from frn_benchmark_downloader import FRNBenchmarkDownloader

def parse(input_dict):
    try:
        download_obj = FRNBenchmarkDownloader(input_dict)
        # download_obj.log_isp()
        # download_obj.check_schedule()
        session = download_obj.session_obj.get_session()
        end_date =  download_obj.commons.get_date_time_now().split(' ')[0]
        start_date = download_obj.pricing_date.split(' ')[0]
        holiday_query = "select * from FV.dbo.FV_Holidays_list where currency = 'USD'"
        holiday= download_obj.ferack4.query(holiday_query)
        hday_list=[]
        for i in holiday:
            hday_list.append(i[0].strftime('%Y-%m-%d'))

        historical_url = "https://markets.newyorkfed.org/read?productCode=50&eventCodes=525&startDt=2020-03-02&endDt=2024-03-06&fields=averageIndex30days,averageIndex90days,averageIndex180days,sofrIndex,refRateDt&sort=postDt:1"
        url = f"https://markets.newyorkfed.org/read?productCode=50&eventCodes=525&startDt={start_date}&endDt={end_date}&fields=averageIndex30days,averageIndex90days,averageIndex180days,sofrIndex,refRateDt&sort=postDt:1"  #daily 
        

        payload = {}
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36:',
        }
        response = session.request(method='GET', url=url, headers=headers, data=payload)

        json_text = response.text
        dict_data = json.loads(json_text)

        data = dict_data['data']
        fields = {}
        list_row = {'averageIndex30days':'1M','averageIndex90days':'3M','averageIndex180days':'6M'}
        for row in data:
            tenors = json.loads(row['data'])
            for tenor in list_row:
                fields['Source'] =  input_dict['source'] 
                fields['Name'] = input_dict['name'] 
                fields['Tenor'] = list_row[tenor]
                fields['InterestRateDate'] = tenors['refRateDt']
                fields['InterestRate'] = tenors[tenor]

                print(fields)
                download_obj.logger.info("fields - {}".format(str(fields)))
                insert = download_obj.db_process.frn_insert_raw(fields, download_obj.ferack)
                download_obj.logger.info("Status - {},Message - {}, InsertQuery - {}".format(str(insert['status']),str(insert['message']),str(insert['query'])))

            mirror_insert = download_obj.db_process.frn_mirror_insert(download_obj,download_obj.ferack,input_dict['source'],input_dict['name'],hday_list)
            download_obj.logger.info("Mirror Insertion Completed")
    except Exception as e:
        pass





if __name__ == '__main__':
    input_dict = {}
    input_dict['filepath'] = __file__

    input_dict['source'] = 'USD-SOFR - Federal Reserve Bank of New York (Gov Website)'
    input_dict['name'] =   'USD-SOFRAI (SOFR Averages and Index Data)'
    try:
        input_dict['environment'] = sys.argv[1] # change Test or Live
    except:
        input_dict['environment'] = 'Test'
        
    parse(input_dict)
    
    
"""Comments
Developer: Harish P
created date : 2024-03-06
completed date: 
"""