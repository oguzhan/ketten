/goals
======
Goals resource. Actions like listing, adding and deleting goals happen here.

GET
---
Retrieves the list of goals.

Request:

::

    GET http://example.com/goals

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
Adds a new goal to the calendar.

Request:

::

    POST http://example.com/goals

Request body:

::

    {
        "title": "Eat healthy",
        "starting_date": "2012-06-30T18:02:52.249Z"
    }

DELETE
------
Deletes all goals.

Request:

::

    DELETE http://example.com/goals


/goals/<id>
===========
Details about a specific goal.

GET
---
Retrieve details of goal with specified <id>.

Request:

::

   GET http://example.com/goals/1

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
---
Update the title or the starting date of a goal.

Request:

::

    PUT http://example.com/goals/1

Request body:

::

    {
        "title": "Eat healthy",
        "starting_date": "2012-06-30T18:02:52.249Z"
    }

DELETE
------
Delete goal with <id>.

Request:

::

   DELETE http://example.com/goals/1


/goals/<id>/links
=================
Links represent the links of the chain. They are essentially days that the goal was achieved.

GET
---
Retrieves all the links of the goal with <id>.

POST
----
Creates a new link for the specified goal, for the current date unless the day is specified.

DELETE
------
Deletes a link for a specified date.

