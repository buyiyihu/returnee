# Returnee


Returnee is a request processing tool for python web service framework Flask, however you can also modify it to adopt in other frameworks. Since python have no `goto` statement, means that if we want to teminate the request handling process in a long call chain, we have to `return` severals times with several `if`s.

Returnee combines exception and enumeration, and can store extra info, you can raise it, you can return it and you can use it to return data.

## Usage

```python

from returnee import Result

@your_mashaller
def request_handler(*args, **kwargs):
    # CODES HERE
    return Result(data=data)

    ...
    raise Result(data=data)

```
