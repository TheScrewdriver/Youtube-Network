from googleapiclient.discovery import build
import network as nt
from tqdm import tqdm

api_key = 'AIzaSyAWbRMM-15W9u0wKCJkHoCtMVRbCrn7h4U'
youtube_api = build('youtube', 'v3', developerKey=api_key)
SNIPPET: str = "snippet"

# Youtube Channel

def	init_channel_sub(channel: str) -> list[dict]:

	stat = youtube_api.channels().list(
			part = 'snippet',
			forUsername = channel
	)
	stat = stat.execute()
	if (stat['pageInfo']['totalResults'] > 0):
		init = {'name': stat['items'][0][SNIPPET]['title'],
			'id': stat['items'][0]['id']}
		init_list = []
		init_list.append(init)
		return init_list
	return None

def	get_subscriptions(ch_ID: str):

		if ch_ID is not None:
			subscriptions = youtube_api.subscriptions() \
							.list(part = 'snippet',
									channelId = ch_ID,
									maxResults = 50
							)
			subscriptions = subscriptions.execute()
			return [{'name': sub['snippet']['title'],
					'id': sub['snippet']['resourceId']['channelId']}
					 for sub in subscriptions['items']]
		return (None)

def	get_all_subscriptions(graph, sub_list, max_depth, curr_depth = 0):

	if curr_depth < max_depth and sub_list is not None:
		for sub in tqdm(sub_list):
			for i in range(curr_depth):
				print("\t", end='')
			try:
				new_sub_list = get_subscriptions(sub['id'])
				nt.add_sub_list(graph, sub, new_sub_list)
				get_all_subscriptions(graph, new_sub_list, max_depth, curr_depth + 1)
			except Exception:
				pass

