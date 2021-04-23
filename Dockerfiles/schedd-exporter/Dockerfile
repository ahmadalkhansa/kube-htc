FROM htcondor/base:8.9.7-el7

RUN mkdir /home/condor_exporter
RUN mkdir /home/mount_dir
RUN adduser submitter

RUN yum install -y python36-pip python3-devel gcc
RUN pip3 install htcondor==8.9.7 prometheus-client==0.0.20 uWSGI==2.0.15
COPY exporter /home/condor_exporter/exporter
COPY CondorExporter.py /home/condor_exporter/CondorExporter.py
COPY wsgi.py /home/condor_exporter/wsgi.py
COPY exporter_run.sh /home/condor_exporter/exporter_run.sh
RUN chmod +x /home/condor_exporter/exporter_run.sh

RUN echo -e ' \n\
[program:uwsgi] \n\
command= uwsgi -w exporter --http-socket :9118 --logger file:/home/exporter.log \n\
startretries= 0 \n\
directory=/home/condor_exporter' >> /etc/supervisord.conf

ENTRYPOINT ["/bin/sh"]
CMD ["-c", "/home/condor_exporter/exporter_run.sh"]