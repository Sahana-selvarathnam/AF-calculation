# importing python packages
import csv
import pandas as pd
import os
import sys

# defining genes and population count and validating the dataset
dataset = input("Dataset_id:").upper()
if dataset == "STARGAZER":
	population = 1029
	gene_list = ["CYP2A6","CYP2B6","CYP2C8","CYP2C9","CYP2C19","CYP3A4","CYP3A5","GSTM1","NAT2","NUDT15","SLCO1B1","TPMT","UGT1A1"]
elif dataset == "CYRIUS":
	population = 950
	gene_list = ["CYP2D6"]
elif dataset == "HLA-A":
	population = 845
	gene_list = ["HLA-A"]
elif dataset == "HLA-B":
	population = 900
	gene_list = ["HLA-B"]
elif dataset == "HLA-C":
	population = 836
	gene_list = ["HLA-C"]
elif dataset == "HLA-DQB1":
	population = 1012
	gene_list = ["HLA-DQB1"]
elif dataset == "HLA-DPB1":
	population = 1015
	gene_list = ["HLA-DPB1"]
elif dataset == "HLA-DRB1":
	population = 1006
	gene_list = ["HLA-DRB1"]
else:
	print("PROVIDE VALID DATASET") 

# calculating the total allele count
total_allele_count = population*2

# opening each dataset the dataset
f=open(dataset+".txt", "w")
sys.stdout = f
print("IndiGen")

# calculating allele frequency based on the formula
for gene in gene_list:
	gene1 = gene + "_1"
	gene2 = gene + "_2"

	df=pd.read_csv(dataset+".tsv", delimiter="\t")
	list_1 = df[gene1].tolist()
	list_2 = df[gene2].tolist()
	uniq_list_1 = df[gene1].unique().tolist()
	uniq_list_2 = df[gene2].unique().tolist()

	set_1 = set(uniq_list_1)
	set_2 = set(uniq_list_2)

	list_2_without_list_1 = list(set_2 - set_1)
	final_list = uniq_list_1 + list_2_without_list_1
	print("\n")
	print(gene,final_list)

	for i in final_list:
		count1 = list_1.count(i)
		count2 = list_2.count(i)
		AF = (count1+count2)/total_allele_count
		print(gene+i,"=",AF)
#		print(i,"=",AF)
f.close()
