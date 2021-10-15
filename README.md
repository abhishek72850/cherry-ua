[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

-----------------------------

# Cherry UserAgent (cherry-ua)
This is an advanced random user agent generator python library, the user agents can be generated
based on various search parameters, it supports an advanced form of applying search filters.

## Database
It uses [Whatismybrowser](https://developers.whatismybrowser.com/useragents/database/) database which
consists of more than `91+ Million` user agents, which ensures everytime it generates unique random user agents.

## Compatibility
The library uses as much as possible inbuilt modules, so it support all major python version.

## Installation
```
pip install cherry-ua
```

## Usage
- The simplest of way to use this library is:
  ```
  from cherry_ua import UserAgent

  ua = UserAgent()
  ua.get_random()
  ```
- To refresh the User Agent dataset
  ```
  ua.refresh()
  ```
- To get the size of User Agent dataset
  ```
  ua.size()
  ```
- To get specifc search filter query
  ```
  ua.get('device')
  ```
- To set specific search filter query
  ```
  ua.set('device', 'eq("mobile")')
  ```
- To get all the search filters
  ```
  ua.get_all_filters()
  ```
- To set multiple searcg filter queries
  ```
  ua.set_search_filters(device='eq("mobile")')
  ```





## Search Filters
The `UserAgent` class support's multiple search parameters which can be used to get only
the user agent which satisfies your requirements. The parameters are:
  - `device`
    datatype : String
  - `os_name`
    datatype : String
  - `os_version`
    datatype : Integer
  - `browser`
    datatype : String
  - `browser_engine`
    datatype : String
  - `browser_version`
    datatype : Integer
  - `limit`
    datatype : Integer

## Search Filter Operators
To add the support for relative searching the filter's support some operators
just like SQL, which gives the flexibility to seearch in more customized way,
the operators it supports are:
  - `eq`
  - `lt`
  - `gt`
  - `lte`
  - `gte`
  - `ne`

## Operator Chaining
The filter query also supports if you want to chain multiple operators, the supported
operator chaining are:
  - `and`
  - `or`

## UserAgent class Functions
| Function | Description |
| --- | --- |
| get_random() | Returns random user agent based on given search parameters if given. |
| refresh() | Download and loads fresh set of User agent |
| size() | Return size of user agent downloaded dataset |
| get() | Returns value of given search parameters |
| set() | Sets specific given search parameter |
| get_all_filters() | Returns all the search filters |
| set_search_filters() | Sets multiple search parameters |





[contributors-shield]: https://img.shields.io/github/contributors/abhishek72850/cherry-ua.svg?style=for-the-badge
[contributors-url]: https://github.com/abhishek72850/cherry-ua/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/abhishek72850/cherry-ua.svg?style=for-the-badge
[forks-url]: https://github.com/abhishek72850/cherry-ua/network/members
[stars-shield]: https://img.shields.io/github/stars/abhishek72850/cherry-ua.svg?style=for-the-badge
[stars-url]: https://github.com/abhishek72850/cherry-ua/stargazers
[issues-shield]: https://img.shields.io/github/issues/abhishek72850/cherry-ua.svg?style=for-the-badge
[issues-url]: https://github.com/abhishek72850/cherry-ua/issues

