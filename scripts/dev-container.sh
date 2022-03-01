docker build . --build-arg python_version=3.9.10 \
    -t igormcsouza/pyautotester:dev
docker run -it \
    -v /home/${USER}/.ssh:/home/user/.ssh \
    -v ${PWD}:/home/user/pyautotester \
    -e APP_ENV=dev igormcsouza/pyautotester:dev
