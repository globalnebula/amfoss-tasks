import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape live cricket score
def scrape_live_score():
    url = "https://www.espncricinfo.com/live-cricket-score"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find HTML elements for team 1, team 2, and their scores
    team1_element = soup.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate')
    team2_element = soup.find('p', class_='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3')
    score1_element = soup.find('div', class_='ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap')
    score2_element = soup.find('div', class_='ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap fadeIn-enter-done')
    result_element = soup.find('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')
    

    # Extract the text values from the elements
    team1 = team1_element.text.strip() if team1_element else ""
    team2 = team2_element.text.strip() if team2_element else ""
    score1 = score1_element.text.strip() if score1_element else ""
    score2 = score2_element.text.strip() if score2_element else ""
    result = result_element.text.strip() if result_element else ""

    # Format the live score message
    live_score_message = ""
    respo = ""

    # Add a conditional statement to execute a command
    if team1 and team2 and (score1 or score2):
        respo = "Fetching live scores...\n"
        if score2:
            live_score_message = f"**{team1}** :\n{score1}\n**---------------------------**\n**{team2}** :\n{score2}"
        elif 'won' or 'lost' in result:
            live_score_message = f"Previous match result: {result}"
        else:
            live_score_message = f"**{team1}** :\n{score1}\n**---------------------------**\n**{team2}** :\n{result}"
    elif result_element:
        respo = "No matches at the current moment."
        result = result_element.text.strip()
        if 'starts' in result:
            live_score_message = f"Next {result}"
        else:
            live_score_message = f"Previous match result: {result}"
    else:
        live_score_message = "No live scores available."

    return respo, live_score_message, team1, team2

def get_stats():
    url = "https://www.espncricinfo.com/ci/engine/match/scores/desktop.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    series_elements = soup.find('p', class_='potMatchSeriesHeading')
    match_elements = soup.find('p', class_='potMatchText mat_scores')
    lastbat_elements = soup.find('p', class_='potMatchText mat_lastbat')
    players_elements = soup.find('p', class_='potMatchText mat_players')
    status_elements = soup.find('p', class_='potMatchText mat_status')

    match = match_elements.text.strip() if match_elements else ""
    series = series_elements.text.strip() if series_elements else ""
    lastbat = lastbat_elements.text.strip() if lastbat_elements else ""
    players = players_elements.text.strip() if players_elements else ""
    status = status_elements.text.strip() if status_elements else ""

    if match or series or lastbat or players or status:
        statistics = f"_**{series}**_\n***{match}***\n**Players** : *{players}*\n**Last Bat** : *{lastbat}*\n***{status}***"
    else:
        statistics = "Sorry, No current match going on for stats"
        
    return statistics


# Function to append the live score to a CSV file
def append_to_csv(score):
    with open('scores.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([score])
