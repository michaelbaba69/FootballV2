import random
from time import sleep
from colorama import Fore
from random import randint

#Credits
#Main Game Design and code - Cyaze
#Rating System - deadman
#bug testing - @theoneandon1yhi on twitter


#Team Data
teams = ["AFC Bournemouth", "Arsenal","Aston Villa","Brentford","Brighton","Chelsea","Crystal Palace","Everton","Fulham","Leeds","Leicester City","Liverpool"	,"Manchester City",	"Manchester United","Newcastle United",	"Nottingham Forest"	,"Southampton",	"Tottenham Hotspur","West Ham","Wolves","Watford"]

# Reputation of each team, where higher values indicate a better reputation
teams_reputation = {
  "AFC Bournemouth": 65,
  "Arsenal": 90,
  "Aston Villa": 80,
  "Brentford": 65,
  "Brighton": 85,
  "Chelsea": 60,
  "Crystal Palace": 60,
  "Everton": 50,
  "Fulham": 55,
  "Leeds": 50,
  "Leicester City": 65,
  "Liverpool": 95,
  "Manchester City": 100,
  "Manchester United": 65,
  "Newcastle United": 80,
  "Nottingham Forest": 40,
  "Southampton": 55,
  "Tottenham Hotspur": 90,
  "West Ham": 60,
  "Wolves": 65,
  "Watford": 20
}


#Player Setup
match_played = 0
goal_count = 0
assists = 0
age = randint(18,23)
xp = 0
rating = 71
sim_speed = 0.1
team = random.choice(teams)
player_firstname = input("What is you Player's firstname" "\n")
if player_firstname == "Ze Hang":
  rating += 28
  xp += 9999999
elif player_firstname == "Ollie":
  rating -= 100
  team = "Watford"
player_surename = input("What is you Player's surename" "\n")

#functions for game

def transfer():
  global team
  global rating
  global salary

  # Allow the player to choose which team they want to request a transfer to
  choice = random.choice(teams)
  desired_team = choice

  # Calculate the likelihood of the transfer being accepted based on player's rating and the reputation of the desired team
  transfer_likelihood = rating + teams_reputation[desired_team]
  if transfer_likelihood > 160:  # Transfer is more likely to be accepted if player has high rating and desired team has good reputation
    transfer_accepted = True
  else:
    transfer_accepted = False

  # If the transfer is accepted, negotiate the transfer fee and salary with the new team
  if transfer_accepted:
    transfer_fee = random.randint(1000000, 100000000)
    print(f"{desired_team} has accepted your transfer request and is requesting a transfer fee of £{transfer_fee}")
    salary = random.randint(30000, 100000)
    print(f"{desired_team} is offering a salary of £{salary} per week")
    accept = input("Do you accept the offer? (y/n) ")
    if accept == 'y':
      team = desired_team
      rating += 3  # Transfer to a new team can improve player's rating
      print(f"You have transferred to {team} for a fee of £{transfer_fee} and a salary of £{salary} per week")
    else:
      print("Transfer declined")
  else:
    print("Sorry, your transfer request was not accepted.")

  

import math

def play():
  global match_played
  global goal_count
  global assists
  team_score = 0
  enemy_score = 0
  print("\n")
  sleep(1)
  print("Premier League")
  enemy = random.choice(teams)
  while enemy == team:
    enemy = random.choice(teams)
  print(f"{team} vs " + enemy)
  game_time = True
  time = 0
  while game_time:
    sleep(sim_speed)
    time += 1
    if time == 45:
      print("Half time")
    elif time == 90:
      print("Full Time")
      break
    else:
      # Calculate the probability of the player scoring a goal based on the player's rating
      mean = rating / 30  # Mean of the distribution is the player's rating divided by 10
      stddev = 50  # Standard deviation of the distribution
            # Generate a random value from the Gaussian distribution using the Box-Muller transform
      probability = math.exp(-(mean**2)/(2*stddev**2)) / (stddev * math.sqrt(2*math.pi))

      probability = min(probability, 1)  # Probability cannot be greater than 1
      probability = max(probability, 0)  # Probability cannot be less than 0

      # Roll a random number between 0 and 1 to determine if a goal is scored
      roll = random.random()
      if roll <= probability:
        print(str(time) + Fore.YELLOW + f" GOOOOOAL! scored by {player_surename} ⚽" + Fore.WHITE)
        team_score += 1
        goal_count += 1
      elif roll <= probability * 2:  # Probability of assisting a goal is half the probability of scoring a goal
        print(str(time) + f" {team} scored! Assisted by {player_surename} ⚽" )
        team_score += 1
        assists += 1
      elif roll <= probability * 3:  # Probability of assisting a goal is half the probability of scoring a goal
        print(str(time) + f" {team} scored!⚽" )
        team_score += 1
      else:
        enemy_mean = 70 / 100  # Mean of the distribution is the enemy team's average rating divided by 10
        enemy_stddev = 50  # Standard deviation of the distribution
        enemy_probability = math.exp(-(enemy_mean**2)/(2*enemy_stddev**2)) / (enemy_stddev * math.sqrt(2*math.pi))
        enemy_probability = min(enemy_probability, 1)  # Probability cannot be greater than 1
        enemy_probability = max(enemy_probability, 0)  # Probability cannot be less than 0

        # Roll a random number between 0 and 1 to determine if the enemy team scores a goal
        enemy_roll = random.random()
        if enemy_roll <= enemy_probability:
          print(str(time) + Fore.RED + f" {enemy} scored! ⚽" + Fore.WHITE)
          enemy_score += 1
        else:
          print(time)
  print(f"Score: {team_score} {team} " + ":" + f" {enemy_score} {enemy}")
  match_played += 1


    
    
def train():
  global xp
  global rating

  # Add training activities
  activities = ['agility drills', 'shooting drills', 'passing drills', 'conditioning exercises', 'interactive drill']

  # Let the player choose their activity
  print("Choose an activity to train:")
  for i, activity in enumerate(activities):
    print(f"{i+1}. {activity}")
  choice = int(input()) - 1
  activity = activities[choice]

  # If the player chooses the interactive drill, run a shooting drill
  if activity == 'interactive drill':
    print("Welcome to the shooting drill! You have 10 shots to score as many goals as possible.")
    goals = 0
    for i in range(10):
      shot_power = input("Enter the shot power (1-5): ")
      shot_accuracy = randint(1,5)
      shot_quality = int(shot_power) + int(shot_accuracy)
      if shot_quality > 6:
        goals += 1
        print("GOAL!")
      else:
        print("Missed!")
    print(f"You scored {goals} goals!")
    gain_xp = goals * 2
    xp += gain_xp
  else:
    # Give XP and potentially increase rating for other activities
    gain_xp = random.randint(1,5)
    xp += gain_xp
    if xp % 4 == 0:
      rating += 1
    print(f"You trained {activity} and gained {gain_xp} XP!")

  # Randomly determine if the player gets injured
  if rating >= 99:
    print("Max Level")


    
def setting():
  global sim_speed
  setting_menu = int(input("Menu Setting: 1 Simulation Speed, 2 Retire, 3 Exit "))
  if setting_menu == 1:
    sim_speed = float(input("Enter a sim speed? e.g 0.5 "))
  if setting_menu == 2:
    confirm = input("Are you sure? ")
    if confirm in {"Yes","y","ye","Y","yes"}:
      print("Bro Retired 💀 ")
      print("Career Mode Summary:")
      print(f"Age: {age}")
      print(f"Last team: {team}")
      print(f"Rating: {rating}")
      print(f"Goals:{goal_count}")
      print(f"Assists:{assists}")
      sleep(1)
      exit()
  if setting_menu == 3:
    print("Exited")
  else:
    print("Leaving Settings...")
    

#Game Loop  
while True:
  print("\n")
  if match_played % 10 == 0 and match_played != 0:
    age += 1
    sleep(1)
    match_played = 0
    print(Fore.LIGHTGREEN_EX + "AGED UP!" + Fore.WHITE)
  print(f"Age: {age}")
  print(f"Current team: {team}")
  print(f"Rating: {rating}")
  print(f"XP: {xp}")
  print(f"Goals:{goal_count}")
  print(f"Assists:{assists}" "\n")
  while True:
    try: 
      menu_input = int(input("Menu: 1 = Play, 2 = Transfer 3 = Train , 4 = Setting" "\n"))
      break
    except ValueError:
      print('Please enter a number')
  if menu_input == 1:
    play()
  if menu_input == 2:
    transfer()
  if menu_input == 3:
    train()
  if menu_input == 4:
    setting()
  if menu_input >= 4:
    print(" ")
  