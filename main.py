import os

if not os.path.exists("npc13.csv"):
	print("please standby, scraping data...")
	import SI_507_junfang_data_access


import argparse

parser = argparse.ArgumentParser()


parser.add_argument('job', help = 'search or visualize', choices = ('search', 'visualize'))

parser.add_argument('--name', type = str, required = False)

parser.add_argument('--party', type = str, required = False)

parser.add_argument('--gender', type = str, required = False)

parser.add_argument('--ethnicity', type = str, required = False)

parser.add_argument('--birthday', type = str, required = False)

parser.add_argument('--position', type = str, required = False)

parser.add_argument('--birthplace', type = str, required = False)

parser.add_argument('--constituency', type = str, required = False)

parser.add_argument('--graphic', choices = ('table', 'barplot', 'piechart'))

parser.add_argument('--graphic_property', choices = ('name', 'party', 'gender', 'ethnicity', 'birthday', 'position', 'birthplace', 'constituency'))

args = parser.parse_args()



import search



if args.job == "search":

	if args.name is not None:
		found, person = search.name_search(args.name)

		if not found:
			print("\n\nThe person " + args.name + " could not be found in the collected data.\n\n")

		else:
			output = "\n\n\n" + person[0] + " is a congressperson\n" + "\tbelonging to party " + person[1] +  ",\n\twith gender " + person[2] + \
				",\n\twith ethnicity " + person[3] + \
                                ",\n\twith birthday " + person[4] + \
                                ",\n\twith position " + person[5] + \
                                ",\n\twith birthplace " + person[7] + \
                                ",\n\twith constituency " + person[8] + ".\n\n\n"

			print(output)			

	else:

		people = search.general_search(party = args.party, gender = args.gender, ethnicity = args.ethnicity, birthday = args.birthday, position = args.position, birthplace = args.birthplace, constituency = args.constituency)


		if not people:
			print("\n\nNo people satisfying the search criteria were found.\n\n")

		else:

			print("\n\n\nHere are the list of people who satisfy the search criteria:\n")

			for person in people:
				print("\t" + person[0] + "\n")


			print("\nSearch a specific name in this list for a more detailed view of that congressperson.\n\n")
			
		

elif args.job == "visualize":

	
	if not args.graphic:
		raise Exception("Please specify a type of graphic for your visualization.")

	elif not args.graphic_property:
		raise Exception("Please specify a data property to examine in your visualization.") 

	else:
		
		import visualize

		labels, counts = visualize.viz_counts(args.graphic_property)

		import plotly.graph_objects as go

		if args.graphic == "piechart":

			fig = go.Figure(data = [go.Pie(labels = labels, values = counts)])

			fig.show()

		elif args.graphic == "barplot":

			fig = go.Figure(data = [go.Bar(x = labels, y = counts)])

			fig.show()

		elif args.graphic == "table":

			header = dict(values = labels,
				fill_color = 'paleturquoise',
				align='left')

			cells = dict(values= [[x] for x in counts],
			fill_color='lavender',
			align='left')

			fig = go.Figure(data = [go.Table(header = header, cells = cells)])

			fig.show()
