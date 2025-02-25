SNp Ranger

Given a gbk annotation file and the output of the SNP exporter tool from Mauve **snp_ranger.py** locates if an SNP is within the range of annotated features. This method speeds up the process of identifying SNP's of functional interest in coding regions.

The script takes the reference (or first) gbk input for progressiveMauve alignment and SNP export file as input, the script will use only the first column of the SNP file.

The output is a list of SNPS found in annotated regions and will exclude anything outside the range of annotated tRNA, rRNA or CDS positions. It will also notify when it encouters a SNP in region with no annotation to aid further investigation.


		USAGE: mauve_to_snps.py Exported_SNPS.txt  first_gbk_file > snps.txt  


Note that this method isn't foolproof, always check the alignment as SNP's can be from eg. the same contaminants from both samples aligning or misannotations between refeence and target genomes.


Example of output:

	NODE_1: SNP here but no annotations found!
	Node: NODE_3
	Product: hypothetical_protein
	Value: 17
	Range: 13, 210
	-----
	Node: NODE_15
	Product: Small_toxic_polypeptide_LdrD
	Value: 596
	Range: 596, 723
	-----


    Notes:
    
    sometimes (but not always...)  rRNA entries are like this:
        
        
        so ignored specific feature labels....and located products after....
    
    rRNA            complement(285468..285578)
                     /locus_tag="10580_EscherichiacoliMG1655Sensitive_00595"
                     /product="5S ribosomal RNA"
                     
                     
                     
    sometimes like this:
        
             CDS             complement(267396..268268)
                     /gene="rluF"
                     /locus_tag="10580_EscherichiacoliMG1655Sensitive_00583"
                     /EC_number="5.4.99.21"
                     /inference="ab initio prediction:Prodigal:2.6"
                     /inference="similar to AA sequence:UniProtKB:P32684"
                     /codon_start=1
                     /transl_table=11
                     /product="23S rRNA pseudouridine(2604) synthase"
                     /translation="MLPDSSVRLNKYISESGICSRREADRYIEQGNVFLNGKRATIGD
                     QVKPGDVVKVNGQLIEPREAEDLVLIALNKPVGIVSTTEDGERDNIVDFVNHSKRVFP
                     IGRLDKDSQGLIFLTNHGDLVNKILRAGNDHEKEYLVTVDKPITEEFIRGMSAGVPIL
                     GTVTKKCKVKKEAPFVFRITLVQGLNRQIRRMCEHFGYEVKKLERTRIMNVSLSGIPL
                     GEWRDLTDDELIDLFKLIENSSSEVKPKAKAKPKTAGIKRPVVKMEKTAEKGGRPASN
                     GKRFTSPGRKKKGR"
        
        '''
