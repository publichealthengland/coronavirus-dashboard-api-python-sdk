General use
...........

We would like to extract the number of new cases, cumulative cases, new deaths and
cumulative deaths for England using the API.

Import
~~~~~~

We start off by importing the library into our workspace:

.. code-block:: python

    from uk_covid19 import Cov19API



Filters
~~~~~~~

Next, we construct the value of the ``filters`` parameter. Read more about ``filters`` and
the its values in the `Developers Guide`_.

.. code-block:: python

    england_only = [
        'areaType=nation',
        'areaName=England'
    ]


Structure
~~~~~~~~~

Next step is to construct the value of the ``structure`` parameter. To do so, we need to
find out the name of the metric in which we are interested. You can find this information
in the `Developers Guide`_ on the Coronavirus Dashboard website.

In the case of this example, the metrics are as follows:

- ``newCasesByPublishDate``: New cases (by publish date)
- ``cumCasesByPublishDate``: Cumulative cases (by publish date)
- ``newDeaths28DaysByDeathDate``: New deaths (by death date)
- ``cumDeaths28DaysByDeathDate``: Cumulative deaths (by death date)

In its simplest form, we construct the structure as follows:

.. code-block:: python

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeaths28DaysByDeathDate": "newDeaths28DaysByDeathDate",
        "cumDeaths28DaysByDeathDate": "cumDeaths28DaysByDeathDate"
    }




Instantiation
~~~~~~~~~~~~~

Now, we may use ``filters`` and ``structure`` to initialise the ``Covid19API`` object:

.. code-block:: python

    api = Cov19API(filters=england_only, structure=cases_and_deaths)



Extracting data
~~~~~~~~~~~~~~~
Finally, we extract the data using one of ``.get_json()``, ``.get_xml()``, ``.get_csv()``,
or ``.get_dataframe()`` methods:

.. code-block:: python

    data = api.get_json()

    print(data)

::

    {
        'data': [
            {
                'date': '2020-07-28',
                'areaName': 'England',
                'areaCode': 'E92000001',
                'newCasesByPublishDate': 547,
                'cumCasesByPublishDate': 259022,
                'newDeaths28DaysByDeathDate': None,
                'cumDeaths28DaysByDeathDate': None
            },
            {
                'date': '2020-07-27',
                'areaName': 'England',
                'areaCode': 'E92000001',
                'newCasesByPublishDate': 616,
                'cumCasesByPublishDate': 258475,
                'newDeaths28DaysByDeathDate': 20,
                'cumDeaths28DaysByDeathDate': 41282
            },
            ...
        ],
        'lastUpdate': '2020-07-28T15:34:31.000000Z',
        'length': 162,
        'totalPages': 1
    }


.. _`Developers Guide`: https://coronavirus.data.gov.uk/developers-guide
