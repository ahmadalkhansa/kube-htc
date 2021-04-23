FROM bacello_ubuntu1:latest
WORKDIR /home
COPY wrapper.sh wrapper.sh
COPY OS.py OS.py
COPY recognition.sh recognition.sh
COPY wait_for.sh wait_for.sh
RUN chmod +x wrapper.sh
RUN chmod +x OS.py
RUN chmod +x recognition.sh
RUN chmod +x wait_for.sh
ENV LANG en_US.UTF-8
ENV BACELLO_HOME='/home/bacello'
ENTRYPOINT ["/bin/bash", "-c", "./wait_for.sh -s -n psi_blast -- ./wrapper.sh"]
