## SNP-Ranger

Given a gbk annotation file and the output of the SNP exporter tool from Mauve **snp_ranger.py** locates if an SNP is within the range of annotated features. This method speeds up the process of identifying SNP's of functional interest and reduces the chance of reporting SNPs from contaminants.

SNP-Ranger takes the reference (or first) gbk input for progressiveMauve alignment and SNP export file as input and outputs a list of SNPs located in annotated regions.  It will exclude anything outside the range of annotated tRNA, rRNA or CDS positions and notify when an SNP in encountered within a region that is not annotated, to enable further investigation.

See details of usage below:

		snp_ranger.py Exported_SNPS.txt  first_gbk_file > snps.txt  


SNP-Ranger produces plan text output, providing a list of SNPs with their parent NODES and relative positions:

	NODE_1: SNP here but no annotations found!
 	-----
	NODE_3:
	Product: hypothetical_protein
	Value: 17
	Range: 13, 210
	-----
	NODE_15:
	Product: Small_toxic_polypeptide_LdrD
	Value: 596
	Range: 596, 723
	-----


The following python modules are required:
- regex, 




Notes on usage:

> This method isn't foolproof, be sure to check the alignment (SNP's can be from eg. the same contaminants from both samples aligning or misannotations between refeence and target genomes).

    
>     sometimes (but not always...)  rRNA entries are like this:
        
        
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
