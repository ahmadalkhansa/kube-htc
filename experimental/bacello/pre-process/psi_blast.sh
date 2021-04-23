echo `ls ./*.fasta`
#mkdir ./volume/output/
for file in `ls -1 ./volume/input_fasta/*.fasta` ; do psiblast -query $file -db ./database/*.fasta -evalue 0.01 -num_iterations 2 -out_ascii_pssm "${file%.fasta}.pssm" -num_alignments 50 -out "${file%.fasta}.alns.blast" ; done                
