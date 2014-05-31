#
# Do not Edit! Generated by:
# spectacle version 0.13~pre
#
# >> macros
# << macros

Name:       sharutils
Summary:    The GNU shar utilities for packaging and unpackaging shell archives
Version:    4.7
Release:    4
Group:      Applications/Archiving
License:    GPL
URL:        http://www.gnu.org/software/sharutils/
Source0:    ftp://ftp.gnu.org/gnu/sharutils/REL-%{version}/sharutils-%{version}.tar.bz2
Source1001: packaging/sharutils.manifest 
BuildRequires:  gettext

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
The sharutils package contains the GNU shar utilities, a set of tools
for encoding and decoding packages of files (in binary or text format)
in a special plain text format called shell archives (shar).  This
format can be sent through e-mail (which can be problematic for regular
binary files).  The shar utility supports a wide range of capabilities
(compressing, uuencoding, splitting long files for multi-part
mailings, providing checksums), which make it very flexible at
creating shar files.  After the files have been sent, the unshar tool
scans mail messages looking for shar files.  Unshar automatically
strips off mail headers and introductory text and then unpacks the
shar files.

Install sharutils if you send binary files through e-mail.

%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .

%configure \
        --disable-static \
        --disable-nls \
        --disable-man
# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
chmod 644 AUTHORS ChangeLog COPYING NEWS README THANKS TODO

mkdir -p $RPM_BUILD_ROOT%{_datadir}/license
for keyword in LICENSE COPYING COPYRIGHT;
do
	for file in `find %{_builddir} -name $keyword`;
	do
		cat $file >> $RPM_BUILD_ROOT%{_datadir}/license/%{name};
		echo "";
	done;
done

%remove_docs

%clean
rm -rf %{buildroot}

%files
%manifest sharutils.manifest
%defattr(-,root,root,-)
%{_datadir}/license/%{name}
%exclude /usr/bin/compress-dummy
%exclude /usr/bin/mail-files
%exclude /usr/bin/mailshar
%exclude /usr/bin/remsync
%exclude /usr/bin/shar
%exclude /usr/bin/unshar
/usr/bin/uudecode
/usr/bin/uuencode