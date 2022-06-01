from googleapiclient.discovery import build

api_key = 'AIzaSyAWbRMM-15W9u0wKCJkHoCtMVRbCrn7h4U'
youtube_api = build('youtube', 'v3', developerKey=api_key)

#Youtube Channel

def	get_channel_id(channel):

	stat = youtube_api.channels().list(
			part = 'snippet',
			forUsername = channel
	)
	stat = stat.execute()
	if (stat['pageInfo']['totalResults'] > 0):
		return(stat['items'][0]['id'])
	else:
		return (None)

def	get_subscriptions(ch_ID):

		if (ch_ID != None):
			subscriptions = youtube_api.subscriptions().list(
							part = 'snippet',
							channelId = ch_ID,
							maxResults = 50
			)
			subscriptions = subscriptions.execute()
			sub_list = []
			for	sub in subscriptions['items']:
				new_sub = {'name': sub['snippet']['title'], 'id': sub['snippet']['resourceId']['channelId']}
				sub_list.append(new_sub)
			return (sub_list)
		return (None)

def	get_all_subscriptions(sub_list, max_depth, curr_depth = 0):

	if (curr_depth < max_depth and sub_list != None):
		for sub in sub_list:
			for i in range(curr_depth):
				print("\t", end='')
			print(sub['name'])
			try:
				new_sub_list = get_subscriptions(sub['id'])
				get_all_subscriptions(new_sub_list, max_depth, curr_depth + 1)
			except Exception:
				pass

### MAIN

channel = input("Youtube Channel : ")
nb = int(input("How many times : "))
ch_ID = get_channel_id(channel)
print("\n\n", channel)
sub_list = get_subscriptions(ch_ID)
get_all_subscriptions(sub_list, nb)

youtube_api.close()
