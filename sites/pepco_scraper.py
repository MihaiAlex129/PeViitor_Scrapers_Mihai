#
#
#  Basic for scraping data from static pages
# ------ IMPORTANT! ------
# if you need return soup object:
# you cand import from __utils -> GetHtmlSoup
# if you need return regex object:
# you cand import from __utils ->
# ---> get_data_with_regex(expression: str, object: str)
#
# Company ---> PEPCO
# Link ------> https://careers.pepco.eu/PepcoRomania/search/?createNewAlert=false&q=&locationsearch=Romania&optionsFacetsDD_customfield1=
#
#
from __utils import (
    GetStaticSoup,
    get_county,
    get_job_type,
    Item,
    UpdateAPI,
)

def scraper():
    '''
    ... scrape data from PEPCO scraper.
    '''
    soup = GetStaticSoup("https://careers.pepco.eu/PepcoRomania/search/?createNewAlert=false&q=&locationsearch=Romania&optionsFacetsDD_customfield1=")

    job_list = []
    for job in soup.find_all('tr', attrs={'class': 'data-row'}):
        location = job.find('span', attrs={'class': 'jobLocation'}).text.strip().split(', ')[0]

        # get jobs items from response
        job_list.append(Item(
            job_title=job.find('a', attrs={'class': 'jobTitle-link'}).text,
            job_link='https://careers.pepco.eu' + job.find('a', attrs={'class': 'jobTitle-link'})['href'],
            company='PEPCO',
            country='Romania',
            county=get_county(location),
            city=location,
            remote='on-site',
        ).to_dict())

    return job_list


def main():
    '''
    ... Main:
    ---> call scraper()
    ---> update_jobs() and update_logo()
    '''

    company_name = "PEPCO"
    logo_link = "https://pepco.ro/wp-content/themes/main/dist/img/logo.svg?x71824"

    jobs = scraper()
    # uncomment if your scraper done
    #UpdateAPI().update_jobs(company_name, jobs)
    #UpdateAPI().update_logo(company_name, logo_link)


if __name__ == '__main__':
    main()
