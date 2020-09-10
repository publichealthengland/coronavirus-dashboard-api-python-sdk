Latest data
...........

To get the latest data by a specific metric, we need to set the ``latest_by`` input
argument when instantiating the ``Cov19API`` object.

The value of ``latest_by`` must be the name of a metric that is included in
the ``structure``. A list of metrics is available on the `Developers Guide`_ webpage.


.. note::

    This option produces the latest available values (non-null) for a set of metrics
    relative to the date of the latest available record for one specific metric.


.. attention::

    The ``latest_by`` input argument only accepts one value. You may still include
    multiple metrics in the ``structure``, but beware that the response will *only*
    include data for the date on which the last record for the ``latest_by`` metric
    was last published.


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

    data = api.get_json()

    print(data)

::

    {
        "data": [
            {
                "date": "2020-07-28",
                "areaName": "England",
                "areaCode": "E92000001",
                "newCasesByPublishDate": 547,
                "cumCasesByPublishDate": 259022,
                "newDeaths28DaysByDeathDate": None,
                "cumDeaths28DaysByDeathDate": None
            },
            {
                "date": "2020-07-28",
                "areaName": "Northern Ireland",
                "areaCode": "N92000002",
                "newCasesByPublishDate": 9,
                "cumCasesByPublishDate": 5921,
                "newDeaths28DaysByDeathDate": None,
                "cumDeaths28DaysByDeathDate": None
            },
            {
                "date": "2020-07-28",
                "areaName": "Scotland",
                "areaCode": "S92000003",
                "newCasesByPublishDate": 4,
                "cumCasesByPublishDate": 18558,
                "newDeaths28DaysByDeathDate": None,
                "cumDeaths28DaysByDeathDate": None
            },
            {
                "date": "2020-07-28",
                "areaName": "Wales",
                "areaCode": "W92000004",
                "newCasesByPublishDate": 21,
                "cumCasesByPublishDate": 17191,
                "newDeaths28DaysByDeathDate": None,
                "cumDeaths28DaysByDeathDate": None
            }
        ],
        "lastUpdate": "2020-07-28T15:34:31.000000Z",
        "length": 4,
        "totalPages": 1
    }


.. _`Developers Guide`: https://coronavirus.data.gov.uk/developers-guide
