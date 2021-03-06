all:    help

help:
	@echo "make install [DESTDIR=/path/to/destdir]"

install: clean
	install -m 0755 -d ${DESTDIR}/usr/local/share/openstack-core-test
	install -m 0755	-d  ${DESTDIR}/usr/local/share/openstack-core-test/integration-tests/ubuntu-essex
	install -m 0755 -t  ${DESTDIR}/usr/local/share/openstack-core-test/integration-tests/ubuntu-essex integration-tests/ubuntu-essex/*

clean:
	 @printf "Cleaning up files that are already in .gitignore... "
	@for pattern in `cat .gitignore | grep -v idea`; do find . -name "$$pattern" -delete; done
	@echo "OK!"
