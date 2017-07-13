# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo1 = git.Repo("D:/__Dev/_Projects/_Chefpoo/_WorkingProject")
repo2 = git.Repo("D:/__Dev/_Projects/BantamHost/bantamhost")
repo3 = git.Repo("D:/__Dev/_Projects/Challenger/challenger-frontend")
repo4 = git.Repo("D:/__Dev/_Projects/Challenger/challenger-frontend-NoMo")
repo5 = git.Repo("D:/__Dev/_Projects/Dixit/DixBoardless")
repo6 = git.Repo("D:/__Dev/_Projects/DoctorMailing/APIServer")
repo7 = git.Repo("D:/__Dev/_Projects/DoctorMailing/ChadDoctorSearch")
repo8 = git.Repo("D:/__Dev/_Projects/DoctorMailing/healthcareapi")
repo9 = git.Repo("D:/__Dev/_Projects/Greenstr/node_server")
repo10 = git.Repo("D:/__Dev/_Projects/Greenstr/reactnativeboiler")
repo11 = git.Repo("D:/__Dev/_Projects/Highlight/_frontend")
repo12 = git.Repo("D:/__Dev/_Projects/Highlight/_backend")
repo13 = git.Repo("D:/__Dev/_Projects/Highlight/_app")
repo14 = git.Repo("D:/__Dev/_Projects/Highlight/thm_backend")
repo15 = git.Repo("D:/__Dev/_Projects/Highlight/react-spark-scroll")
repo16 = git.Repo("D:/__Dev/_Projects/Resize.Me")
repo17 = git.Repo("D:/__Dev/_Projects/SupportNotStigma")
repo18 = git.Repo("D:/__Dev/_Projects/TripBook/frontend")
repo19 = git.Repo("D:/__Dev/_Projects/YoutubeWithTranslation/youtube-player-advancedCSS")
repo20 = git.Repo("D:/__Dev/_Projects/Zuva/frontend-react")
repo21 = git.Repo("D:/__Dev/_Projects/Zuva/Scraper/LinkedInScraper")
repo22 = git.Repo("D:/__Dev/_Projects/Zuva/Serverless/zuva-firestore-backend")
repo23 = git.Repo("D:/__Dev/_Projects/Zuva/Serverless/zuva-oi-aws-backend")
repo24 = git.Repo("D:/__Dev/_Projects/Zuva/standalones/chat")
repo25 = git.Repo("D:/__Dev/_Projects/Zuva/standalones/news-map")
# Your mock repo
mock_repo = git.Repo("D:/__Dev/_Projects/_BitbucketProjectsCommits")
importer = Importer([repo1,repo2,repo3,repo4,repo5,repo6,repo7,repo8,repo9,repo10,repo11,repo12,repo13,repo14,repo15,repo16,repo17,repo18,repo19,repo20,repo21,repo22,repo23,repo24,repo25], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['julzhoben@gmail.com'])
importer.import_repository()
