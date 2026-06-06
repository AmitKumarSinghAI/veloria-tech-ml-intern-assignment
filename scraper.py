import pandas as pd
from bs4 import BeautifulSoup
import requests


match_data = []
team1_name = []
team2_name = []
venue = []
Match_result =[]
Top_Scorer =[]
Top_Score = []


for i in range(2630,2641):
    url = "https://howstat.com/cricket/Statistics/Matches/MatchScorecard_T20.asp?MatchCode={}".format(i)
    response = requests.get(url)
    if response.status_code == 200 :
        soup = BeautifulSoup(response.text,'lxml')
        m_d = soup.find_all("td",class_="ScorecardHeader")
        t1_n = soup.find_all("a",class_="ScorecardCountry2Link")
        t2_n = soup.find_all("a",class_="ScorecardLink1")
        ven = soup.find_all("a",class_="LinkBlack2")
        m_r = soup.find_all("td",class_="ScorecardHeader")
        match_data.append(m_d[2].get_text(strip=True))
        team1_name.append(t1_n[0].get_text(strip=True))
        team2_name.append(t2_n[1].get_text(strip=True))
        #venue.append(ven[8].get_text(strip=True))
        Match_result.append(m_r[3].get_text(strip=True))
        
        table = soup.find_all("table")[5]
        rows = table.find_all("tr")

        top_name = ""
        top_runs = 0

        for row in rows:
            cols = row.find_all("td")

            # batting rows have many columns
            if len(cols) >= 7:
                try:
                    name = cols[0].get_text(strip=True)

                    runs_text = cols[2].get_text(strip=True)

                    if runs_text.isdigit():
                        runs = int(runs_text)

                        if runs > top_runs:
                            top_runs = runs
                            top_name = name

                except:
                    pass

        Top_Scorer.append(top_name)
     
        Top_Score.append(top_runs)
       
        rows = soup.find_all("tr")

        for row in rows:
            cols = row.find_all("td")

            if len(cols) >= 2:
                if cols[0].get_text(strip=True) == "Venue":
                    venue.append(cols[1].get_text(strip=True))
                    break


cricket_df = pd.DataFrame({
    "Match Data" : match_data,
    "Team 1 name" : team1_name,
    "Team 2 name" : team2_name,
    "Venue(stadium_name)" : venue,
    "Top Scorer" : Top_Scorer,
    "Top score" : Top_Score,
    "Match_result" : Match_result
})
        
cricket_df.to_csv("match_data.csv")
print("sucessuflly extract data and convert store in csv file")