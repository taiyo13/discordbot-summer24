import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# DynamoDBにアクセスするためのクライアントを作成
dynamodb = boto3.resource('dynamodb', region_name='your-region')

# データを取得するための関数
def get_discord_id_and_api_key(user_id):
    try:
        # DynamoDBテーブルを指定
        table = dynamodb.Table('your-table-name')

        # DynamoDBからデータを取得（キーとしてuser_idを使用）
        response = table.get_item(
            Key={
                'user_id': user_id
            }
        )

        # レスポンスからDiscord IDとAPIキーを取得
        if 'Item' in response:
            discord_id = response['Item'].get('DiscordID')
            api_key = response['Item'].get('ApiKey')
            return discord_id, api_key
        else:
            return None, None

    except NoCredentialsError:
        print("AWS credentials are not available.")
        return None, None
    except PartialCredentialsError:
        print("Incomplete AWS credentials provided.")
        return None, None

# 取得したデータを使って処理を行う
user_id = 'sample-user-id'
discord_id, api_key = get_discord_id_and_api_key(user_id)

if discord_id and api_key:
    print(f"Discord ID: {discord_id}, API Key: {api_key}")
else:
    print("Data not found.")
