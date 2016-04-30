echo "beginning rsync"
rsync -r --exclude 'deploy.sh' --exclude '.git' --exclude 'python' \
/home/thor/Code/feminest/* tidepool@tide-pool.ca:/home/tidepool/www/feminest
echo "rsync complete!"
