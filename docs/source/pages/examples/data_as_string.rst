Stringified JSON or XML
.......................

Set the ``as_string`` input argument to ``True`` for the ``.get_json()`` or ``.get_xml()``
methods if you wish to receive stringified JSON or XML entities:

.. code-block:: python

    from uk_covid19 import Cov19API


    all_nations = [
        "areaType=nation"
    ]

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeaths28DaysByDeathDate": "newDeaths28DaysByDeathDate",
        "cumDeaths28DaysByDeathDate": "cumDeaths28DaysByDeathDate"
    }

    api = Cov19API(
        filters=all_nations,
        structure=cases_and_deaths,
        latest_by="newCasesByPublishDate"
    )

    json_data = api.get_json(as_string=True)
    print("JSON:", json_data)

    xml_data = api.get_xml(as_string=True)
    print("XML:", xml_data)

::

    JSON: {"data":[{"date":"2020-08-09","areaName":"England","areaCode":"E92000001","newCasesByPublishDate":988,"cumCasesByPublishDate":268312,"newDeaths28DaysByDeathDate":null,"cumDeaths28DaysByDeathDate":null},{"date":"2020-08-09","areaName":"Northern Ireland","areaCode":"N92000002","newCasesByPublishDate":0,"cumCasesByPublishDate":null,"newDeaths28DaysByDeathDate":null,"cumDeaths28DaysByDeathDate":null},{"date":"2020-08-09","areaName":"Scotland","areaCode":"S92000003","newCasesByPublishDate":48,"cumCasesByPublishDate":18998,"newDeaths28DaysByDeathDate":null,"cumDeaths28DaysByDeathDate":null},{"date":"2020-08-09","areaName":"Wales","areaCode":"W92000004","newCasesByPublishDate":26,"cumCasesByPublishDate":17451,"newDeaths28DaysByDeathDate":null,"cumDeaths28DaysByDeathDate":null}],"lastUpdate":"2020-08-09T17:56:52.000000Z","length":4,"totalPages":1}
    XML: <document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><data><date>2020-08-09</date><areaName>England</areaName><areaCode>E92000001</areaCode><newCasesByPublishDate>988</newCasesByPublishDate><cumCasesByPublishDate>268312</cumCasesByPublishDate><newDeaths28DaysByDeathDate xsi:nil="true" /><cumDeaths28DaysByDeathDate xsi:nil="true" /></data><data><date>2020-08-09</date><areaName>Northern Ireland</areaName><areaCode>N92000002</areaCode><newCasesByPublishDate>0</newCasesByPublishDate><cumCasesByPublishDate xsi:nil="true" /><newDeaths28DaysByDeathDate xsi:nil="true" /><cumDeaths28DaysByDeathDate xsi:nil="true" /></data><data><date>2020-08-09</date><areaName>Scotland</areaName><areaCode>S92000003</areaCode><newCasesByPublishDate>48</newCasesByPublishDate><cumCasesByPublishDate>18998</cumCasesByPublishDate><newDeaths28DaysByDeathDate xsi:nil="true" /><cumDeaths28DaysByDeathDate xsi:nil="true" /></data><data><date>2020-08-09</date><areaName>Wales</areaName><areaCode>W92000004</areaCode><newCasesByPublishDate>26</newCasesByPublishDate><cumCasesByPublishDate>17451</cumCasesByPublishDate><newDeaths28DaysByDeathDate xsi:nil="true" /><cumDeaths28DaysByDeathDate xsi:nil="true" /></data><lastUpdate>2020-08-09T17:56:52.000000Z</lastUpdate><length>4</length><totalPages>1</totalPages></document>


