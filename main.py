import youtube_network as sub
import network as nt
import scipy as sp

### MAIN

if __name__ == '__main__':
	channel = input("Youtube Channel : ")
	nb = int(input("How many times : "))
	init_sub = sub.init_channel_sub(channel)

	G = nt.create_graph()

	print(f"\n\n{init_sub[0]['name']}")

	if (nb == 0):
		G.add_node(init_sub[0]['name'])
	elif (nb > 0):
		sub_list = sub.get_subscriptions(init_sub[0]['id'])
		nt.add_sub_list(G, init_sub[0], sub_list)
		sub.get_all_subscriptions(G, sub_list, nb - 1)

	print("Nodes : ", G.number_of_nodes())

	sub.youtube_api.close()
	nt.display_graph(G)
