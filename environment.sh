
set +o errexit
createuser -s publictitles
createdb -U publictitles -O publictitles publictitles -T template0
