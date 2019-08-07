import scraperwiki
import urlparse
import lxml.html

# scrape_table function: gets passed an individual page to scrape
def scrape_table(parameter_a):
    rows = parameter_a.cssselect("ul.results-list.list-unstyled li")  # selects all <li> blocks within <ul class="results-list list-unstyled"> and puts in list variable 'rows'
#     My guess is it knows to make a list variable because either 'cssselect' function has that written in or it does it automatically because there are multiple table rows
    for row in rows:
        # Set up our data record - we'll need it later
        record = {}
        table_cells = row.cssselect("h3")
        if table_cells: 
            record['School name'] = table_cells[0].text
            # Print out the data we've gathered
            print record, '------------'
            # Finally, save the record to the datastore - 'Artist' is our unique key
            scraperwiki.sqlite.save(["School name"], record)
        
# scrape_and_look_for_next_link function: calls the scrape_table
# function, then hunts for a 'next' link: if one is found, calls itself again
def scrape_and_look_for_next_link(parameter_b):
    html = scraperwiki.scrape(parameter_b)
    print html
    root = lxml.html.fromstring(html)
    scrape_table(root)
#     next_link = root.cssselect("a.pagination__next")
#     print next_link
#     if next_link:
#         next_url = urlparse.urljoin(base_url, next_link[0].attrib.get('href'))
#         print next_url
#         scrape_and_look_for_next_link(next_url)

# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------

starting_url = 'https://reports.ofsted.gov.uk/search?q=&location=&radius=&level_2_types%5B%5D=2&latest_report_date_start=&latest_report_date_end=&region%5B%5D=E12000007&status%5B%5D=1&level_1_types=1'
scrape_and_look_for_next_link(starting_url)



