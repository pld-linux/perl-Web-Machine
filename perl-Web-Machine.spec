#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Web
%define		pnam	Machine
Summary:	Web::Machine - A Perl port of Webmachine
Name:		perl-Web-Machine
Version:	0.17
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Web/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f62606a516068b9d889610fc2d51905c
URL:		https://metacpan.org/release/Web-Machine
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(HTTP::Headers::ActionPack) >= 0.07
BuildRequires:	perl(IO::Handle::Util)
BuildRequires:	perl(Test::FailWarnings)
BuildRequires:	perl-HTTP-Message
BuildRequires:	perl-Hash-MultiValue
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Net-HTTP
BuildRequires:	perl-Plack
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Try-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web::Machine provides a RESTful web framework modeled as a state
machine. You define one or more resource classes. Each resource
represents a single RESTful URI end point, such as a user, an email,
etc. The resource class can also be the target for POST requests to
create a new user, email, etc.

Each resource is a state machine, and each request for a resource is
handled by running the request through that state machine.

Web::Machine is built on top of Plack, but it handles the full request
and response cycle.

See Web::Machine::Manual for more details on using Web::Machine in
general, and how Web::Machine and Plack interact.

This is a port of Webmachine, actually it is much closer to the Ruby
version, with a little bit of the JavaScript version and even some of
the Python version thrown in for good measure.



# %description -l pl.UTF-8 # TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL
%{perl_vendorlib}/Web/*.pm
%{perl_vendorlib}/Web/Machine
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
