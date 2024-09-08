import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# DynamoDBにアクセスするためのクライアントを作成
dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2')

# データを取得するための関数
def get_discord_id_and_time(discord_id):
    try:
        # DynamoDBテーブルを指定
        table = dynamodb.Table('dev_insight')

        # DynamoDBからデータを取得（キーとしてdiscord_idを使用）
        response = table.get_item(
            Key={
                'discord_id': discord_id
            }
        )

        # レスポンスからDiscord IDとtimeを取得
        if 'Item' in response:
            discord_id = response['Item'].get('discord_ID')
            time = response['Item'].get('timestamp')
            return discord_id, time
        else:
            return None, None

    except NoCredentialsError:
        print("AWS credentials are not available.")
        return None, None
    except PartialCredentialsError:
        print("Incomplete AWS credentials provided.")
        return None, None

# 取得したデータを使って処理を行う
discord_id = 'sample-user-id'
discord_id, time = get_discord_id_and_time(discord_id)

if discord_id and time:
    print(f"Discord ID: {discord_id}, Time: {time}")
else:
    print("Data not found.")
