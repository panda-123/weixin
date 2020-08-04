#ecoding=utf-8
# author:herui
# time:2019/11/28 17:21
# function:

import logging
import operator

class JsonComparator:
    def __init__(self):
        pass

    def equal(self, live_json, std_json):
        logging.info('live_json:' + str(live_json))
        logging.info('std_json:' + str(std_json))
        return live_json == std_json

    def less_than(self,live_json, std_json):
        '''
        compare to two json object,if std_json contains live_json,return True,else return False
        (live_json <= std_json)
        :param live_json:
        :param std_json:
        :return:
        '''
        logging.info('live_json:' + str(live_json))
        logging.info('std_json:' + str(std_json))
        return operator.le(str(std_json), str(live_json))


    def more_than(self,live_json, std_json):
        '''
        compare to two json object,if live_json contains std_json,return True,else return False
         (live_json >= std_json)
        :param live_json:
        :param std_json:
        :return:
        '''
        logging.info('live_json:' + str(live_json))
        logging.info('std_json:' + str(std_json))
        return operator.ge(str(std_json), str(live_json))

if __name__ == '__main__':
    json_comparator = JsonComparator()
    live_json = {
      "errcode": 0,
      "errmsg": "created"
}
    std_json = {
      "errcode": 0,
      "errmsg": "created",
        "123": 123
}
    print(json_comparator.less_than(live_json, std_json))