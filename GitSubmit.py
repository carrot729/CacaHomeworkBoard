import os
from git.repo import Repo
import time
print('''
*************************************
 ######     ###     ######     ###    
##    ##   ## ##   ##    ##   ## ##   
##        ##   ##  ##        ##   ##  
##       ##     ## ##       ##     ## 
##       ######### ##       ######### 
##    ## ##     ## ##    ## ##     ## 
 ######  ##     ##  ######  ##     ## 
*************************************
    ''')
print('Welcome to CacaGitSubmit.')
repo=Repo('.')
git=repo.git
git.add('.')
git.commit('-m', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
remote = repo.remote()
remote.push()