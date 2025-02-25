#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: camilla eldridge
"""

import sys
import re
from typing import List, Dict

mauve_SNP_output = sys.argv[1]
first_gbk = sys.argv[2]



''' Get node ids and snp pos for sequence 1 only'''
contig_pos = []

with open(mauve_SNP_output, "r") as snps:
    next(snps)  
    for line in snps:
        if not line.strip():  
            continue

        spline = line.split()
        if len(spline) < 4:  
            continue  

        contig_id = "_".join(spline[1].split("_")[:2])
        contig_pos.append(f"{contig_id},{spline[2]},{spline[3]}") 

        

''' Get set of node ids with SNPS'''
snp_node_ids: set[str] = {node.split(",")[0] for node in contig_pos}

''' Get gbk entries for SNP nodes '''
gbk_snp_entries: List[str] = []

with open(first_gbk, "r") as gbk:
    gbk1 = gbk.read().split("LOCUS")[1:]  

    for entry in gbk1:
        at2 = entry.split("\n", 1)[0].split()[0] 

        if at2 in snp_node_ids:  
            gbk_snp_entries.append(entry)
            
            

''' Find annotated regions for each contig'''
def get_annotations(x: str) -> List[str]:
    contig_cds: List[str] = []
    
    NODEid = x.split()[0]
    contig_cds.append(NODEid)
    
    y = x.split("ORIGIN")[0][1:] 

    for Q in y.split("\n"):
        to_app = ""
     
        if "rRNA  " in Q or " CDS " in Q or " tRNA " in Q:
            to_app = re.sub(r'[^a-zA-Z0-9]', ' ', Q).replace("complement", "")
        
        if "/product=" in Q:
            to_app = to_app + Q.strip().replace(" ", "_").replace("/", "")

        contig_cds.append(to_app)

    return [item.strip() for item in contig_cds if item.strip()]



''' Get annotated entry in each contig '''
all_snp_conts: List[List[str]] = [get_annotations(C) for C in gbk_snp_entries]



''' Print out which nodes have a SNP but no annotation'''
all_snp_conts_replaced: List[str] = []

for E in all_snp_conts:
    nod_id = str(E).split()[0]

    if len(E) < 2:  # If SNP but no annotation found.. print the node id.
        print(f"{''.join(E)}: SNP here but no annotations found!")
    else:
        E = str(E).replace("CDS ", nod_id).replace("tRNA ", nod_id).replace("rRNA ", nod_id).replace("product=", "")
        E = re.sub(r"[',\[\]\"()]", "", E)  
        all_snp_conts_replaced.append([r for r in E.split()[1:]])



''' Remove duplicate node ids from SNP list and add a split term'''
w: List[str] = []

for i in contig_pos:
    i = i.split(",")
    nod_id, nod_pos = i[0], i[1]

    if nod_id not in w:
        w.append("split_me")
        w.append(nod_id)
    w.append(nod_pos)



''' Get all SNP positions for each node '''
snp_node_positions: List[List[str]] = list(filter(None, [k.split() for k in " ".join(w).split("split_me")]))



''' Iterate through SNP positions and annotated regions for each node; a bit loopy - there is probably a better way to do this'''
snps_in_annot: Dict[str, List[Dict[str, str]]] = {}

for snp_val in snp_node_positions:
    node = snp_val[0]
    snps_in_annot[node] = []

    for triplet in all_snp_conts_replaced:
        triplet_node = triplet[0]

        if triplet_node == node:
            values = snp_val[1:]
            for i in range(1, len(triplet), 4):
                product = triplet[i + 2]
                range_values = triplet[i:i + 2]

                for value in values:
                    int_value = int(value)
                    if int(range_values[0]) <= int_value <= int(range_values[1]):
                        snps_in_annot[node].append({'product': product, 'value': value, 'range': range_values})

                        break  
                        


''' Remove entries with empty key or values (SNPs outside annotated range)'''
snps_in_annot = {k: v for k, v in snps_in_annot.items() if k and v}



''' Print out final results '''
for node, entries in snps_in_annot.items():
    print(f"Node: {node}")
    for entry in entries:
        product = entry['product']
        value = entry['value']
        value_range = entry['range']
        print(f"Product: {product}")
        print(f"Value: {value}")
        print(f"Range: {', '.join(value_range)}")
        print("-----")
