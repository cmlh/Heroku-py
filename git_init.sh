rm -rf .git
git init
git add .slugignore
git add Procfile
git add runtime.txt
sh requirements.sh
git add requirements.txt
git add example_gunicorn.py
echo "$ heroku create --ssh-git"
echo "Add Heroku Git Remote"
echo "$ git config --global url.ssh://git@heroku.com/.insteadOf https://git.heroku.com/"
