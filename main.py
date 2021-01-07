from scraper import JobScrape

mon = JobScrape("monster")

mon_results = mon.get_jobs("Dublin", "IE", "Python, Django")