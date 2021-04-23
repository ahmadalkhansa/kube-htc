#/bin/sh

for i in $(ls proteins/); do
        while [ ! -f proteins/$i/"$i"_replacements.fasta ]
        do
                sleep 1
        done
done

