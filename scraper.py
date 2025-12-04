from playwright.sync_api import sync_playwright
import json
import time


#Start browser and go to the top
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.imdb.com/chart/top/")
    time.sleep(2)

    #Get links to movies
    title_links = page.query_selector_all('.ipc-title-link-wrapper')
    movie_urls = []
        
    for link in title_links:
        href = link.get_attribute("href")
        if href and "title/tt" in href:
            movie_urls.append("https://www.imdb.com" + href)
    
    #Scrape finfo
    movies = []
    for url in movie_urls[:125]:
        page.goto(url)
        time.sleep(1)
        movie = {}

        #ID
        movie["imdb_id"] = url.split("/title/")[1].split("/")[0]
        
        #Title
        title = page.query_selector("h1")
        movie["title"] = title.text_content()
        
        #Rating
        movie["rating"] = page.query_selector('[data-testid="hero-rating-bar__aggregate-rating"]').text_content().split("/")[0]
        
        #Year
        movie["year"] = page.query_selector('a[href*="releaseinfo"]').text_content()
        
        #Add movie to the movie list
        movies.append(movie)
    



#Save to json in write mode
    with open("data/movies.json", "w", encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False)
    
    browser.close()