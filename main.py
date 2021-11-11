import os
# os.system('python ./crawler/crawler.py')
# os.system('python ./crawler/parser.py')
os.system('python cp ./crawler/guilds.md ./')
os.system('git commit -am "update"')
os.system('git pull')
os.system('git push')