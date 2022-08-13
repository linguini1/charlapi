# For interacting with the Charlatan Wordpress API
__author__ = "Matteo Golin"

# Imports
import charlapi.customtypes as t
import requests

# Constants
API_URL: t.URL = "https://charlatan.ca/wp-json/wp/v2/"
USER_AGENT_HEADER = {"User-Agent": "DefaultAgent"}


# Functions
def create_query(parameters: t.QueryParameters, global_param: str) -> t.Query:

    """
    Returns a Query for the API URL based on the parameters and the global parameter.

    >>> create_query(['author', 'title.rendered'], 'fields')
    >>> '_fields=author,title.rendered'
    """

    query = f"_{global_param}="
    for parameter in parameters:
        query += f"{parameter},"

    return query[:-1]  # Removes final comma


def create_per_page_query(pages: int) -> t.Query:

    """Returns a URL query that will return the specified number of pages."""

    return f"per_page={pages}"


def create_page_number_query(page: int) -> t.Query:

    """Returns an API URL query that specifies the page to return."""

    return f"page={page}"


def create_query_url(queries: t.URLQueries, endpoint: str) -> t.URL:

    """
    Returns a valid API request URL containing the passed queries at the specified endpoint.

    >>> create_query_url(['_fields=author,title'], 'posts')
    >>> "https://charlatan.ca/wp-json/wp/v2/posts?_fields=author,title"
    """

    url = f"{API_URL}{endpoint}"

    for _ in range(len(queries)):

        query = queries[_]  # Current query

        if _ == 0:  # First query is preceded by question mark
            url += f"?{query}"
        else:
            url += f"&{query}"

    return url


def get_json_results(url: t.URL, user_agent: str = None) -> t.JSON:

    """Returns the JSON response from the API URL passed."""

    if user_agent:  # Custom user agent
        USER_AGENT_HEADER["User-Agent"] = user_agent

    return requests.get(url, headers=USER_AGENT_HEADER).json()
