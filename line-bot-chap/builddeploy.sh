LineKey=$(cat ../.line)
sam build --use-container --profile chap &&\
sam deploy --profile chap --parameter-overrides LineKey=$LineKey
