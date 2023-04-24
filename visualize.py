import search
from collections import Counter

data = search.data

prop_dict = {

	"name" : 0,
	"party" : 1,
	"gender" : 2,
	"ethnicity" : 3,
	"birthday" : 4,
	"position" : 5,
	"birthplace" : 7,
	"constituency" : 8
}



def viz_counts(property):
	
	modified_data = [datum[prop_dict[property]] for datum in data  ]

	labels = list(set(modified_data))

	counts = [modified_data.count(label) for label in labels]

	return labels, counts
