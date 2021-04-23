FROM mapoferri/traineership:bacello_ubuntu

RUN apt update -y
RUN apt install -y ncbi-blast+

RUN mkdir /database
RUN chmod 777 -R /database
COPY uniprot_sprot.fasta.gz /database/uniprot_sprot.fasta.gz
RUN gunzip /database/uniprot_sprot.fasta.gz
RUN for sprot in `ls /database/*.fasta`; do makeblastdb -in $sprot -dbtype prot ; done

WORKDIR /home/preprocess
# preprocess
COPY pre-process/db_index.sh db_index.sh
RUN chmod +x db_index.sh
COPY pre-process/separator.py separator.py
RUN chmod +x separator.py
COPY pre-process/elimination.sh elimination.sh
RUN chmod +x elimination.sh
COPY pre-process/singleline.sh singleline.sh
RUN chmod +x singleline.sh
COPY pre-process/rotation.sh rotation.sh
COPY pre-process/check_lenght.sh check_lenght.sh
COPY pre-process/psi_blast.sh psi_blast.sh
RUN chmod +x psi_blast.sh
COPY pre-process/pre_wrapper.sh pre_wrapper.sh
RUN chmod +x rotation.sh
RUN chmod +x check_lenght.sh
RUN chmod +x pre_wrapper.sh
# bacello
WORKDIR /home/bac_app
COPY bac_app/wrapper.sh wrapper.sh
COPY bac_app/OS.py OS.py
COPY bac_app/recognition.sh recognition.sh
COPY bac_app/wait_for.sh wait_for.sh
RUN chmod +x wrapper.sh
RUN chmod +x OS.py
RUN chmod +x recognition.sh
RUN chmod +x wait_for.sh
ENV LANG en_US.UTF-8
ENV BACELLO_HOME='/home/bacello'
ENV PATH="/home/preprocess:/home/bac_app:/bacello:/bin:/usr/bin:$PATH"
ENTRYPOINT ["/bin/bash", "-c", "time pre_wrapper.sh"]

