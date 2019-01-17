%global		debug_package	%{nil}

%define		pkg_release	2018-10-05
%define		pkg_minor	04
%define		pkg_release_num	%(echo %{pkg_release} | tr -d - )%{pkg_minor}

%define		full_name	stanford-corenlp-full
%define		model_name_en	stanford-english-corenlp-%{pkg_release}-models.jar

Name:		corenlp
Version:	1.0.0
Release:	%{pkg_release_num}%{?dist}
Summary:	Natural Language Processing (NLP) Toolkit

Group:		Development/Libraries/Java
License:	GPL
URL:		https://stanfordnlp.github.io/CoreNLP/
Source0:	https://nlp.stanford.edu/software/stanford-corenlp-full-%{pkg_release}.zip
Source1:	%{name}.service
Source2:	http://nlp.stanford.edu/software/%{model_name_en}

#BuildRequires:	
Requires:	java-1.8.0-openjdk

%description
    Stanford CoreNLP provides a set of natural language analysis tools.
    It can give the base forms of words, their parts of speech, whether
    they are names of companies, people, etc., normalize dates, times,
    and numeric quantities, and mark up the structure of sentences
    in terms of phrases and word dependencies, indicate which noun
    phrases refer to the same entities, indicate sentiment, extract
    open-class relations between mentions, etc. Choose Stanford CoreNLP
    if you need: An integrated toolkit with a good range of grammatical
    analysis tools; Fast, reliable analysis of arbitrary texts; The
    overall highest quality text analytics; Support for a number of
    major (human) languages; Interfaces available for various major
    modern programming languages.

%prep
%setup -qn %{full_name}-%{pkg_release}


%build
#   remove unnecessary files
    rm -f LIBRARY-LICENSES LICENSE.txt Makefile README.txt
    rm -f SemgrexDemo.java ShiftReduceDemo.java StanfordCoreNlpDemo.java StanfordDependenciesManual.pdf build.xml
    rm -f corenlp.sh
    rm -f ejml-0.23-src.zip
    rm -f input.txt input.txt.out input.txt.xml
    rm -f javax.json-api-1.0-sources.jar
    rm -f joda-time-2.9-sources.jar
    rm -f jollyday-0.4.7-sources.jar
    rm -f pom.xml
    rm -f stanford-corenlp-*-javadoc.jar
    rm -f stanford-corenlp-*-sources.jar
    rm -f xom-1.2.10-src.jar

%install
#   create installation hierarchy
    %{__mkdir} -p %{buildroot}%{_sharedstatedir}/%{name}
    %{__mkdir} -p %{buildroot}%{_unitdir}
    %{__cp}   -rp $RPM_BUILD_DIR/%{full_name}-%{pkg_release}/* %{buildroot}%{_sharedstatedir}/%{name}
    %{__cp}   -p %{_sourcedir}/%{name}.service                 %{buildroot}%{_unitdir}/
    %{__cp}   -p %{_sourcedir}/%{model_name_en}                %{buildroot}%{_sharedstatedir}/%{name}/

%files
%{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service

#%doc

%clean
%{__rm} -rf $RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_DIR/%{full_name}-%{pkg_release}

%changelog
* Thu Jan 17 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- init COPR repo

