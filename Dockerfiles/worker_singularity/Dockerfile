FROM htcondor/base:8.9.7-el7

RUN yum update -y
RUN yum groupinstall -y 'Development Tools'
RUN	yum install -y \
	openssl-devel \
	libuuid-devel \
	libseccomp-devel \
	wget \
	squashfs-tools \
	cryptsetup

ENV VERSION=1.14.12 OS=linux ARCH=amd64
RUN	wget https://dl.google.com/go/go$VERSION.$OS-$ARCH.tar.gz && \
	tar -C /usr/local -xzvf go$VERSION.$OS-$ARCH.tar.gz && \
	rm go$VERSION.$OS-$ARCH.tar.gz

ENV PATH="/usr/local/go/bin:$PATH"

ENV VERSION=3.7.0
RUN	wget https://github.com/hpcng/singularity/releases/download/v${VERSION}/singularity-${VERSION}.tar.gz && \
	tar -xzf singularity-${VERSION}.tar.gz && \
	cd singularity && \
	./mconfig && \
	make -C builddir && \
	make -C builddir install

RUN mkdir /home/simages

RUN yum install -y nfs-utils

