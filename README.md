# replurk-bot
This is a script which search Plurk by keyword and replurk.

# Get Start

Copy `.env.example` to `.env`

Input keys from plurk, set the keyword.

# How to add package and deploy
required npm.

- install serverless
```
npm install -g serverless
```

- install virtualenv
```
pip install virtualenv
```

- make virtual environments
```
$ virtualenv venv --python=python3
```

```
$ source venv/bin/activate 
```

## install new package 
```
(venv) $ pip install {your_package}
```

## deploy

config AWS key and secret
```
(venv) $ serverless config credentials --provider provider --key key --secret secret
```

deploy
```
(venv) $ serverless deploy
```
