/db_index.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to build database, so can't start the application Psi_Blast: $status"
        exit $status
fi

mkdir ./volume/input_fasta
mkdir ./volume/input_pssm

./rotation.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to split fasta file, so can't start the application Bacello: $status"
        exit $status
fi

for file in `ls *.fasta` ; do mv $file ./volume/input_fasta/ ;  done
echo 'After rotation:'
ls ./volume/input_fasta/
echo 'On home:'; ls .

./elimination.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to eliminate multi-fasta file, so can't start the application Bacello: $status"
        exit $status
fi
./check_lenght.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to check lenght of the file, so can't start the application Bacello: $status"
echo 'Afer checking lenght:'
ls ./volume/input_fasta/
ls /home/

./singleline.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to lining up the fasta files, so can't start the application Bacello: $status"
        exit $status
fi

echo 'After singleline:'
ls ./volume/input_fasta/
ls /home/

#starting second process, only if the first has been coming out good.
./psi_blast.sh -D
status=$?
if [ $status -ne 0 ]; then
        echo "Failed to run PsiBlast, so can't start the application Psi_Blast: $status"
        exit $status
fi

for file in `ls ./volume/input_fasta/*.pssm`; do mv $file ./volume/input_pssm/ ;  done
echo 'Showing results:'
ls ./volume/input_pssm/
