LineKey=$(cat ../.line)
sam build --profile chap &&\
sam deploy --profile chap --parameter-overrides LineKey=$LineKey
