PKG_NAME := jdk-janino
URL := http://janino.unkrig.de/download/janino-2.7.8.zip
ARCHIVES := http://repo1.maven.org/maven2/org/codehaus/janino/janino-parent/2.7.8/janino-parent-2.7.8.pom %{buildroot} \
	http://repo1.maven.org/maven2/org/codehaus/janino/commons-compiler/2.7.8/commons-compiler-2.7.8.pom %{buildroot} \
	http://repo1.maven.org/maven2/org/codehaus/janino/commons-compiler-jdk/2.7.8/commons-compiler-jdk-2.7.8.pom %{buildroot} \
	http://repo1.maven.org/maven2/org/codehaus/janino/janino/2.7.8/janino-2.7.8.pom %{buildroot}
include ../common/Makefile.common
