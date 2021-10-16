[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

-----------------------------

# Cherry UserAgent (cherry-ua)
This is an advanced search and generate user agent python library, the user agents can be generated
based on various search parameters, it supports an advanced form of applying search filters.

## Database
It uses [Whatismybrowser](https://developers.whatismybrowser.com/useragents/database/) **premium** database which
consists of more than `91+ Million` user agents, which ensures everytime it generates unique random user agents.

## Compatibility
The library uses as much as possible inbuilt modules, so it support all major python version.

## Installation
  ```
  pip install fake-useragent
  ```


Usage
-----
- The simplest way to use this library is:
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
  
    *Datatype* : String <br>
    *Supported Operators* : `eq`, `ne`, `contains` <br>
    *Description* : This Signifies for which type of device you want user agent for.
    ```
    ua = UserAgent(device="eq('mobile')")
    # or
    ua.set('device', "eq('mobile')")
    # or
    ua.set_search_filters(device="eq('mobile')")
    ```
  - `os_name`

    *Datatype* : String <br>
    *Supported Operators* : `eq`, `ne`, `contains` <br>
    *Description* : This Signifies for which OS (operating system) you want user agent for.
    ```
    ua = UserAgent(os_name="eq('windows')")
    # or
    ua.set('os_name', "eq('windows')")
    # or
    ua.set_search_filters(os_name="eq('windows')")
    ```
  - `os_version`

    *Datatype* : Integer <br>
    *Supported Operators* : `eq`, `lt`, `lte`, `gt`, `gte`, `ne` <br>
    *Description* : This Signifies for which OS version you want user agent for.
    > This is an Integer field, so it won't take quotes inside the operator's
    ```
    ua = UserAgent(os_version="eq(8)")
    # or
    ua.set('os_version', "eq(8)")
    # or
    ua.set_search_filters(os_version="eq(8)")
    ```
  - `browser`

    *Datatype* : String <br>
    *Supported Operators* : `eq`, `ne`, `contains` <br>
    *Description* : This Signifies for which browser you want user agent for.
    ```
    ua = UserAgent(browser="eq('chrome')")
    # or
    ua.set('browser', "eq('chrome')")
    # or
    ua.set_search_filters(browser="eq('chrome')")
    ```
  - `browser_engine`

    *Datatype* : String <br>
    *Supported Operators* : `eq`, `ne`, `contains` <br>
    *Description* : This Signifies for which type of device you want user agent for.
    ```
    ua = UserAgent(browser_engine="eq('blink')")
    # or
    ua.set('browser_engine', "eq('blink')")
    # or
    ua.set_search_filters(browser_engine="eq('blink')")
    ```
  - `browser_version`

    *Datatype* : Integer <br>
    *Supported Operators* : `eq`, `lt`, `lte`, `gt`, `gte`, `ne` <br>
    *Description* : This Signifies for which type of device you want user agent for.
    ```
    ua = UserAgent(browser_version="eq(90)")
    # or
    ua.set('browser_version', "eq(90)")
    # or
    ua.set_search_filters(browser_version="eq(90)")
    ```
  - `limit`

    *Datatype* : Integer <br>
    *Supported Operators* : `eq`, `lt`, `lte`, `gt`, `gte`, `ne` <br>
    *Description* : This Signifies for which type of device you want user agent for.
    ```
    ua = UserAgent(limit=1000)
    # or
    ua.set('limit', 1000)
    # or
    ua.set_search_filters(limit=1000)
    ```

## Search Filter Operators
To add the support for relative searching the filter's support some operators
just like SQL, which gives the flexibility to seearch in more customized way,
the operators it supports are:
  - `eq`
 
    *Supported datatype* : `String`, `Integer` <br>
    *Description* : This operator matches the exact value given
    ```
    ua.set('device', "eq('mobile')")
    # matches user agent whose device is mobile
    ```
  - `lt`

    *Supported datatype* : `Integer` <br>
    *Description* : This operator matches if the value of field is less than the given value
    ```
    ua.set('os_version', "lt(8)")
    # matches user agent whose os version is less than 8
    ```
  - `gt`

    *Supported datatype* : `Integer` <br>
    *Description* : This operator matches if the value of field is greater than the given value
    ```
    ua.set('os_version', "gt(8)")
    # matches user agent whose os version is greater than 8
    ```
  - `lte`

    *Supported datatype* : `Integer` <br>
    *Description* : This operator matches if the value of field is less or equal to the given value
    ```
    ua.set('os_version', "lte(8)")
    # matches user agent whose os version is less or equal to 8
    ```
  - `gte`

    *Supported datatype* : `Integer` <br>
    *Description* : This operator matches if the value of field is greater or equal to the given value
    ```
    ua.set('os_version', "gte(8)")
    # matches user agent whose os version is greater or equal to 8
    ```
  - `ne`

    *Supported datatype* : `String`, `Integer` <br>
    *Description* : This operator matches if the value of field is not equal to the given value
    ```
    ua.set('device', "ne('mobile')")
    # matches user agent whose device is not equal to mobile
    ```
  - `contains` (beta)

    *Supported datatype* : `String` <br>
    *Description* : This operator matches if the field value contains the given value
    > This is still is beta stage, so might not work as you expect
    ```
    ua.set('device', "eq('mobile')")
    # matches user agent whose device contains the word "mobile"
    ```

## Operator Chaining
The filter query also supports if you want to chain multiple operators, the supported
operator chaining are:
  - `and`

    *Description* : The "and" operator chains multiple operator describing as it should
    matches all the operator values.
    ```
    ua.set('device', "ne('mobile').and.ne('pc')")
    # It matches user agent which has device value not equal to mobile and pc
    
    # It can also be used to chaining multiple different operators
    ua.set('os_version', "gt(5).and.lt(8)")
    # It matches user agents which has os version greater than 5 and less than 8
    ```
  - `or`

    *Description* : The "or" operator chains multiple operator describing as it should
    matches any one of the operator values.
    ```
    ua.set('device', "ne('mobile').or.ne('pc')")
    # It matches user agent which has device value not equal to mobile or pc
    
    # It can also be used to chaining multiple different operators
    ua.set('os_version', "eq(5).or.gt(8)")
    # It matches user agents which has os version equal to 5 or greater than 8
    ```

## UserAgent class Functions
| **Function** | **Parameters** | **Description** | **Returns** |
| --- | --- | --- | --- |
| **get_random()** | | Returns random user agent based on given search parameters if given. | *String* |
| **refresh()** | | Download and loads fresh set of User agent |  |
| **size()** | | Return size of user agent downloaded dataset | *Integer* |
| **get()** | *(filter_name : str)* | Returns value of given search parameters | *String* |
| **set()** | *(filter_name : str, query : str)* | Sets specific given search parameter |  |
| **get_all_filters()** | | Returns all the search filters | *Dict* |
| **set_search_filters()** | (**kwargs**) | Sets multiple search parameters |  |


# Issues
If facing any issues in the library usage, please feel free to raise the issue in github [issue tracker](https://github.com/abhishek72850/cherry-ua/issues),
since i am the only sole developer of this project it might get delayed to get it resolved but i'll
definetly try to resolve it.


# Donate :pray:
This library itself doesn't need much maintenance, but since i am using a premium server to ensure faster and better API
performance to search and get user agents, so i have to pay bills to keep it running, as i committed to keep it running 
but with a certain limitation, which i will remove if i get enough donation to support this open source project and also 
i will publish the server side code once it gets enough popularity so that others can also look into it, and may suggest some
improvements.
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://paypal.me/abhishek728?locale.x=en_GB)




[contributors-shield]: https://img.shields.io/github/contributors/abhishek72850/cherry-ua.svg?style=for-the-badge
[contributors-url]: https://github.com/abhishek72850/cherry-ua/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/abhishek72850/cherry-ua.svg?style=for-the-badge
[forks-url]: https://github.com/abhishek72850/cherry-ua/network/members
[stars-shield]: https://img.shields.io/github/stars/abhishek72850/cherry-ua.svg?style=for-the-badge
[stars-url]: https://github.com/abhishek72850/cherry-ua/stargazers
[issues-shield]: https://img.shields.io/github/issues/abhishek72850/cherry-ua.svg?style=for-the-badge
[issues-url]: https://github.com/abhishek72850/cherry-ua/issues

