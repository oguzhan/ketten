/chains
======
Chains resource. Actions like listing, adding and deleting chains happen here.

GET
---
Retrieves the list of chains.

Request:

::

    GET http://example.com/chains

Response:

::

    [
        {
            "id: "1",
            "title": "Go jogging",
            "starting_date": "2012-06-30T18:02:52.249Z"
        },
        {
            "id: "2",
            "title": "Eat healthy",
            "starting_date": "2012-06-30T18:02:52.249Z"
        }
    ]


POST
----
Adds a new chain to the calendar.

Request:

::

    POST http://example.com/chain

Request body:

::

    {
        "title": "Eat healthy",
        "starting_date": "2012-06-30T18:02:52.249Z"
    }

DELETE
------
Deletes all chains.

Request:

::

    DELETE http://example.com/chains


/chains/<id>
===========
Details about a specific chain.

GET
---
Retrieve details of chain with specified <id>.

Request:

::

   GET http://example.com/chains/1

Response:

::

    {
        "id": "1",
        "title": "Go jogging",
        "starting_date": "2012-06-10T18:02:52.249Z",
        "links": [
                    {
                       "date": "2012-06-15T18:02:52.249Z"
                    },
                    {
                       "date": "2012-06-17T18:02:52.249Z"
                    }
                 ]
        "current_streak": 2,
        "record_streak": 11
    }

PUT
-----
Update the title or the starting date of a chain.

Request:

::

    PATCH http://example.com/chains/1

Request body:

::

    {
        "title": "Eat healthy",
        "starting_date": "2012-06-30T18:02:52.249Z"
    }

DELETE
------
Delete chain with <id>.

Request:

::

   DELETE http://example.com/chains/1


/chains/<id>/links
=================
Links represent the links of the chain. They are essentially days that the goal was achieved.

GET
---
Retrieves all the links of the chain with <id>.

POST
----
Creates a new link for the specified chain , for the current date unless the day is specified.

DELETE
------
Deletes a link for a specified date.

