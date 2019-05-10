import wolframalpha
client=wolframalpha.Client('UGKH5V-3L5K2E3EHX')

while True:
	query=str(input('Query'))
	res=client.query(query)
	output=next(res.results).text
	print(output)
