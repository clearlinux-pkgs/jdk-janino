Name     : jdk-janino
Version  : 2.7.8
Release  : 2
URL      : http://janino.unkrig.de/download/janino-2.7.8.zip
Source0  : http://janino.unkrig.de/download/janino-2.7.8.zip
Source1  : http://repo1.maven.org/maven2/org/codehaus/janino/janino-parent/2.7.8/janino-parent-2.7.8.pom
Source2  : http://repo1.maven.org/maven2/org/codehaus/janino/commons-compiler/2.7.8/commons-compiler-2.7.8.pom
Source3  : http://repo1.maven.org/maven2/org/codehaus/janino/commons-compiler-jdk/2.7.8/commons-compiler-jdk-2.7.8.pom
Source4  : http://repo1.maven.org/maven2/org/codehaus/janino/janino/2.7.8/janino-2.7.8.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-atinject
BuildRequires : jdk-bsh
BuildRequires : jdk-cdi-api
BuildRequires : jdk-codehaus-parent
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-parent
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-enforcer
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-hamcrest
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-junit4
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-testing
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : jdk-xz
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Patch0   : janino-2.7.8-remove-nullanalysis-annotations.patch

%description
Quick start for JANINO users:
(1) Put "commons-compiler.jar" and "janino.jar" on your class path.

%prep
%setup -q -n janino-2.7.8

find . -name "*.jar" -delete
find . -name "*.class" -delete
for m in commons-compiler commons-compiler-jdk janino
do
mkdir -p ${m}/src
(
cd ${m}/src/
unzip -qq  ../../${m}-src.zip
if [ -f org.codehaus.commons.compiler.properties ]; then
mkdir -p main/resources
mv org.codehaus.commons.compiler.properties main/resources
fi
)
done

%patch0 -p1

cp %{SOURCE1} pom.xml
cp %{SOURCE2} commons-compiler/pom.xml
cp %{SOURCE3} commons-compiler-jdk/pom.xml
cp %{SOURCE4} janino/pom.xml

python3 /usr/share/java-utils/pom_editor.py pom_change_dep    -r :ant-nodeps :ant
python3 /usr/share/java-utils/pom_editor.py pom_xpath_set "pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:source" 1.6
python3 /usr/share/java-utils/pom_editor.py pom_xpath_set "pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:target" 1.6
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :buildnumber-maven-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :maven-clean-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :maven-deploy-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :maven-site-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :maven-source-plugin

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n janino -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/janino/commons-compiler-jdk.jar
/usr/share/java/janino/commons-compiler.jar
/usr/share/java/janino/janino.jar
/usr/share/maven-metadata/janino.xml
/usr/share/maven-poms/janino/commons-compiler-jdk.pom
/usr/share/maven-poms/janino/commons-compiler.pom
/usr/share/maven-poms/janino/janino-parent.pom
/usr/share/maven-poms/janino/janino.pom
