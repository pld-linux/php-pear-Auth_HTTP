%include	/usr/lib/rpm/macros.php
%define		_class		Auth_HTTP
%define		_pearname	%{_class}
Summary:	%{_class} - HTTP authentication system using PHP
Summary(pl):	%{_class} - system uwierzytelniania HTTP przy u¿yciu PHP
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Methods for creating an HTTP authentication system using PHP.

%description -l pl
Metody do tworzenia systemu uwierzytelniania HTTP przy u¿yciu PHP.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
