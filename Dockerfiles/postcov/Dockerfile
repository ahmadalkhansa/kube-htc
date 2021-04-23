FROM ubuntu

RUN apt update -y
RUN apt install -y time
RUN apt install -y xz-utils
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install pandas

RUN mkdir /home/bin
WORKDIR /home/bin

COPY bin/fasta_mutations.py fasta_mutations.py
RUN chmod +x fasta_mutations.py
COPY bin/pre_mutational_assignment.py pre_mutational_assignment.py
RUN chmod +x pre_mutational_assignment.py
COPY bin/mutational_assignment.py mutational_assignment.py
RUN chmod +x mutational_assignment.py
COPY bin/wrapper.sh wrapper.sh
RUN chmod +x wrapper.sh

ENV PATH="/home/bin:/bin:/usr/bin:$PATH"
ENTRYPOINT ["/bin/bash", "-c", "wrapper.sh"]