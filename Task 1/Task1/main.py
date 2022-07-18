import json, unittest, datetime

with open("./data-1.json","r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json","r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json","r") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    json1 = jsonData1
    l = jsonData1['location'].split('/')
    
    json1['location'] = {
      "country":l[0],
      "city":l[1],
      "area":l[2],
      "factory":l[3],
      "section":l[4]
    }
    json1['data'] = {
      "status":jsonData1['operationStatus'],
      "temperature":jsonData1['temp']
    }
    del json1['operationStatus']
    del json1['temp']
    return json1


def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    json2 = jsonData2
  
    json2['deviceID'] = jsonData2['device']['id']
    json2['deviceType'] = jsonData2['device']['type']

    import dateutil.parser
    time = json2['timestamp']
    parsed_time = dateutil.parser.parse(time)
    json2['timestamp'] = parsed_time.timestamp() * 1000


    json2['location'] = {
      "country":json2['country'],
      "city":json2['city'],
      "area":json2['area'],
      "factory":json2['factory'],
      "section":json2['section'],
    }
    del json2['device']
    del json2['country']
    del json2['city']
    del json2['area']
    del json2['factory']
    del json2['section']
    return json2


def main (jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):

        result = main (jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):

        result = main (jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )

if __name__ == '__main__':
    unittest.main()
