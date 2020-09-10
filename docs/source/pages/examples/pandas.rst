Pandas DataFrame
................

You can use the ``.get_dataframe()`` method to get the data as a
Pandas ``DataFrame`` object.

.. warning::

    The `Pandas`_ library is not included in the dependencies of this
    library and must be installed separately.

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
        structure=cases_and_deaths
    )

    df = api.get_dataframe()

    print(df.head())

::

             date          areaName   areaCode  newCasesByPublishDate  cumCasesByPublishDate newDeaths28DaysByDeathDate cumDeaths28DaysByDeathDate
    0  2020-08-08           England  E92000001                    679               267324.0                 None                 None
    1  2020-08-08  Northern Ireland  N92000002                      0                    NaN                 None                 None
    2  2020-08-08          Scotland  S92000003                     60                18950.0                 None                 None
    3  2020-08-08             Wales  W92000004                     19                17425.0                 None                 None


.. _`Pandas`: https://pandas.pydata.org