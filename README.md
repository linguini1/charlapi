# charlapi
### Matteo Golin
A very simple personal package for simplifying interaction with
[The Charlatan's](https://charlatan.ca) WordPress API.

## Requirements
- Python 3.10.6+
- requests

## Usage

### `create_query`
Takes a list of arguments to be used with a global parameter, and formats
them into a string that can be used in the API request URL.

### `create_per_page_query`
Takes the number of objects to be returned per page, and formats it into
a string that can be used in the API request URL.

### `create_page_number_query`
Takes the page number that should be displayed and formats it into a string
that can be used in the API request URL.

### `create_query_url`
Takes a list of query strings and the API endpoint that should be used, and
formats them into a full API request URL.

### `get_json_results`
Take the API request URL and returns the JSON object that the API responds
with.

Optionally takes an argument for `user_agent` as a string, which defines the
name of the user agent. By default, this will be `DefaultAgent`.
