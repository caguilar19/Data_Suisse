import pygal

import csv

ans = [1800]
mariages = [None]

with open('Data_Suisse.csv') as CSVfile:
	data = csv.reader(CSVfile)
	for row in data:
		ans.append(str(row[0]))
		mariages.append(int(row[1]))

line_chart = pygal.Line(
	x_label_rotation=1,
	show_minor_x_labels=False,
	stroke_style={'width': 2},
	dots_size=2)
line_chart.title = 'Nombre de Nouveaux Mariages en Suisse:\n1801-2016'
line_chart.x_labels = ans
line_chart.x_labels_major = ans[::24]
line_chart.add('Mariages', mariages)
line_chart.render_to_file('Data_Suisse.svg')

ans = []
hommes = []
femmes = []
with open('Data_Suisse_Age.csv') as CSVfile:
	data = csv.reader(CSVfile)
	for row in data:
		ans.append(str(row[0]))
		hommes.append(float(row[1]))
		femmes.append(float(row[2]))

line_chart = pygal.Line(
	x_label_rotation=1,
	show_minor_x_labels=False,
	stroke_style={'width': 2},
	dots_size=2)
line_chart.title = 'Moyenne Âge à Se Marier en Suisse:\n1855-2016'
line_chart.x_labels = ans
line_chart.x_labels_major = ans[::20]
line_chart.add('Hommes', hommes)
line_chart.add("Femmes", femmes)
line_chart.render_to_file('Data_Suisse_Age.svg')

ans = []
divorces = []
with open('Data_Suisse_Divorce.csv') as CSVfile:
	data = csv.reader(CSVfile)
	for row in data:
		ans.append(str(row[0]))
		divorces.append(float(row[1]))

line_chart = pygal.Line(
	x_label_rotation=1,
	show_minor_x_labels=False,
	stroke_style={'width': 2},
	dots_size=2)
line_chart.title = 'Nombre de Divorces en Suisse:\n1876-2016'
line_chart.x_labels = ans
line_chart.x_labels_major = ans[::20]
line_chart.add('Divorces', divorces)
line_chart.render_to_file('Data_Suisse_Divorce.svg')

ans = []
moins_que_un = []
un = []
deux = []
trois_a_cinq = []
six_a_dix = []
onze_a_vingt = []
vingt_et_un_a_trente = []
trent_et_un_et_plus = []
with open('Data_Suisse_Divorce_Durée_1.csv') as CSVfile:
	data = csv.reader(CSVfile)
	for row in data:
		ans.append(str(row[0]))
		moins_que_un.append(float(row[1]))
		un.append(float(row[2]))
		deux.append(float(row[3]))
		trois_a_cinq.append(float(row[4]))
		six_a_dix.append(float(row[5]))
		onze_a_vingt.append(float(row[6]))
		vingt_et_un_a_trente.append(float(row[7]))
		trent_et_un_et_plus.append(float(row[8]))

line_chart = pygal.Line(
	x_label_rotation=1,
	show_minor_x_labels=False,
	stroke_style={'width': 2},
	dots_size=2)
line_chart.title = 'Durée de Mariage avant de Divorce en Suisse:\n1876-2016'
line_chart.x_labels = ans
line_chart.x_labels_major = ans[::20]
line_chart.add('Moins Que Un An', moins_que_un)
line_chart.add('Un An', un)
line_chart.add('Deux Ans', deux)
line_chart.add('3-5 Ans', trois_a_cinq)
line_chart.add('6-10 Ans', six_a_dix)
line_chart.add('11-20 Ans', onze_a_vingt)
line_chart.add('21-30 Ans', vingt_et_un_a_trente)
line_chart.add('31 Ans et Plus', trent_et_un_et_plus)
line_chart.render_to_file('Data_Suisse_Duree_1.svg')

ans = []
duree = []
with open('Data_Suisse_Divorce_Durée_2.csv') as CSVfile:
	data = csv.reader(CSVfile)
	for row in data:
		ans.append(str(row[0]))
		duree.append(float(row[1]))

line_chart = pygal.Line(
	x_label_rotation=1,
	show_minor_x_labels=False,
	stroke_style={'width': 2},
	dots_size=2)
line_chart.title = 'Moyenne Durée de Mariage avant de Divorce en Suisse:\n1920-2016'
line_chart.x_labels = ans
line_chart.x_labels_major = ans[::32]
line_chart.add('Durée', duree)
line_chart.render_to_file('Data_Suisse_Duree_2.svg')
