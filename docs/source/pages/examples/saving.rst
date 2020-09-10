Saving the data
...............

Set the ``save_as`` input argument to a path to save the data in a file. This
functionality is only available for ``.get_json()``, ``.get_xml()`` and ``.get_csv()``
methods.

.. note::

    The ``save_as`` argument must be set to a file name with the correct extension;
    that is, ``.json`` for JSON data, ``.xml`` for XML data, and ``.csv`` for CSV data.

    It is additionally assumed that the directory in which you wish to save the file
    already exists. You may use relative or absolute paths.


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

    api.get_csv(save_as="some_existing_directory/data.csv")


This will create a file entitled ``data.csv`` under ``some_existing_directory``. The
contents of the file would be as follows:

::

    date,areaName,areaCode,newCasesByPublishDate,cumCasesByPublishDate,newDeaths28DaysByDeathDate,cumDeaths28DaysByDeathDate
    2020-07-28,England,E92000001,547,259022,,
    2020-07-28,Northern Ireland,N92000002,9,5921,,
    2020-07-28,Scotland,S92000003,4,18558,,
    2020-07-28,Wales,W92000004,21,17191,,
