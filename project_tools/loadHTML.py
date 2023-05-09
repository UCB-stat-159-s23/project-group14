from IPython.display import HTML

def putHTML(year, avg_sales):
	'''Takes in a year & whether the user wants average sales or median income data, and display the html'''
	if avg_sales:
		return HTML(filename = f'output/avgSales{year}.html')
	else:
		return HTML(filename= f'output/medianIncome{year}.html')